import Queue
import sys
import time
import datetime
from threading import Thread
from StratosphereConfig import __StratosphereConfig__
import StratosphereDetector
import StratosphereTuple
import StratosphereOutput

flow_queue = Queue.Queue()


# Thread - getting flow from quene and calling functin from Stratospehre Detector
class ThreadQuene(Thread):

    def __init__(self):
        Thread.__init__(self)
        self.tuples_dict = dict()
        self.ips_dict = dict()
        self.first_flow_in_time_window = None
        self.number_of_trying =0

    def run(self):
        #
        # while True:
        #     if self.number_of_trying > 3:
        #         break
        #     self.read_from_queue()
        #     time.sleep(1)
        #     self.number_of_trying += 1

        self.read_from_queue()
        StratosphereOutput.show('Finish.', 1)
        print(flow_queue.empty())

    def read_from_queue(self):
        time.sleep(1)
        while True:
            if flow_queue.empty() is False:
                # varible for ending this process. If it is bigger then 3, so this process will be finished.
                # So here, when queue is not empty we will put this to 0 again.
                self.number_of_trying = 0
                # Get fow from queue
                flow = flow_queue.get()

                # In each binetflow file first line is describtion
                if 'StartTime' in flow:
                    continue

                split = flow.split(',')
                # Tuple: SRC IP, DST IP, DST PORT, PROTOCOL
                tuple_index = split[3], split[6], split[7], split[2]

                # The variable "current_flow_time" is time from this new flow.
                current_flow_time = datetime.datetime.strptime(split[0], '%Y/%m/%d %H:%M:%S.%f')

                if self.first_flow_in_time_window is not None:

                    time_difference = (current_flow_time - self.first_flow_in_time_window).seconds

                    if time_difference >= __StratosphereConfig__.get_int_time_windows_length():

                        self.print_time_window(last_flow_in_time_window)

                        for i in self.tuples_dict:
                            # The Function return labels: "Normal" or "Botnet" or "Attack" or "Malware".
                            # Right current_flow_time we are not using the detected variable. Maybe we should in the future.
                            # print 'prd', self.tuples_dict[i].state
                            (detected, label, matching_len) = StratosphereDetector.detect(self.tuples_dict[i])

                            # The label is False, when the detector has a little information
                            if label is not False:
                                ip = self.tuples_dict[i].tuple[0]
                                label_state = label
                                # Add the label to IP address dictionary.
                                if self.ips_dict.has_key(ip):
                                    label_state = self.ips_dict[ip] + label
                                self.ips_dict[ip] = label_state + ';'

                                # check if we recognize malicious
                                state = self.tuples_dict[i].state
                                # matching_len gives number from all letters in label, you should count like this:
                                # 11,a,a,a,a,a,a ... so here one letter is 1 and 1, and a, a, so on and it is same
                                self.check_malicious(ip, label_state + ';', state, str(len(state.split(','))))

                        # check lengths of tuple state
                        self.check_tuple_size()
                        # set new time
                        self.first_flow_in_time_window = current_flow_time

                else:
                    self.first_flow_in_time_window = current_flow_time

                # Add flow to exist tuple object or crete new tuple object and add flow.
                if tuple_index in self.tuples_dict.keys():
                    self.tuples_dict[tuple_index].add_flow(flow)
                else:
                    self.tuples_dict[tuple_index] = StratosphereTuple.Tuple([split[3], split[6], split[7], split[2]], split[2]) # tuple, protocol, id
                    self.tuples_dict[tuple_index].add_flow(flow)

                last_flow_in_time_window = current_flow_time

            else:
                # This case is just for testing, when queue is empty. It creates 2 files. First one is about tuples
                # and second one is about ip source and their labels.
                # self.save_to_file()
                # time.sleep(1)
                break


    def print_time_window(self, last_flow_in_time_window):
        # PRINT START TIME, FINISH TIME AND LAST FLOW Of WINDOW TIME
        StratosphereOutput.show('Time_window started: ' + str(self.first_flow_in_time_window) + ' Finished: ' + str(self.first_flow_in_time_window + datetime.timedelta(seconds =__StratosphereConfig__.get_int_time_windows_length()))
                                + ' Last flow: ' + str(last_flow_in_time_window), 1)
        StratosphereOutput.show('=============================================================================', 1)

        StratosphereOutput.log('Time_window started: ' + str(self.first_flow_in_time_window) + ' Finished: ' + str(self.first_flow_in_time_window + datetime.timedelta(seconds =__StratosphereConfig__.get_int_time_windows_length()))
                                + ' Last flow: ' + str(last_flow_in_time_window))
        StratosphereOutput.log('==============================================================================')

    def check_malicious(self, ip, labels, state, len_of_state):
        split = labels.split(';')
        normal = 0
        malicious = 0
        for j in range(len(split)-1):
            # Compare labels and decide, if we find malicious.
            temp_label = split[j]
            # To lower cases.
            temp_label_lower = temp_label.lower()
            if 'normal' in temp_label_lower:
                normal += 1
            elif 'botnet' in temp_label_lower or 'attack' in temp_label_lower or 'malware' in temp_label_lower:
                malicious += 1

        if normal >= malicious:
            self.resolve(False, ip, labels, state, len_of_state, 'Detected as normal. -> IP: ')

        elif normal < malicious:
            self.resolve(True, ip, labels, state, len_of_state, 'Threat was detected!. -> IP: ')

    def check_tuple_size(self):
        for i in self.tuples_dict:
              # print 'lenght of tuple: ', self.tuples_dict[i].get_len_list()
              # print 'len for 100: ',len(self.tuples_dict[i].get_state())
              if self.tuples_dict[i].get_len_list() > __StratosphereConfig__.get_int_length_of_state():
             # if len(self.tuples_dict[i].get_state()) >= 216:
                self.tuples_dict[i].set_state('')
                self.tuples_dict[i].set_list()
                self.tuples_dict[i].set_times()

    # Resolve the result about malicious or not.
    def resolve(self, is_malicious, i, labels, state, len, text):
        if is_malicious or __StratosphereConfig__.get_bool_print_all_labels():
            StratosphereOutput.show(text + i + ' -> tuple(' + len + '): ' + state + ' -> ' + labels, 2)
            StratosphereOutput.show('=============================================================================', 2)
            StratosphereOutput.log(text + i + ' -> tuple(' + len + '): ' + state + ' -> ' + labels)
            StratosphereOutput.log('==============================================================================')

    # This function is temporary just for printing
    # the information about tuples and ips and their labels.
    def save_to_file(self):
        f = open('test_TupleFile', 'w')
        for i in self.tuples_dict:
            # StratosphereOutput.show(('[%s]: %s' % (', '.join(map(str, i)), tuples_dict[i].state)), 3)
            f.write(('[%s]: %s' % (', '.join(map(str, i)), self.tuples_dict[i].state) + '\n'))
        f.close()

        f = open('test_IPsFile', 'w')
        for i in self.ips_dict:
            # StratosphereOutput.show(i + ' -> ' + ips_dict[i], 3)
            f.write(i + ' -> ' + self.ips_dict[i] + '\n')
        f.close()


if __name__ == "__main__":

    t2 = ThreadQuene()
    t2.start()

    # Reading Flows from STDIN
    StratosphereOutput.log('Reading flows from Queue.')
    for line in sys.stdin:
        # print 'Flow', line
        flow_queue.put(line)