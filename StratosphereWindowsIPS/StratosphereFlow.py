import Queue
import sys
import time
import datetime
from threading import Thread
from StratosphereConfig import StratosphereConfig
import StratosphereDetector
import StratosphereTuple
import StratosphereOutput

config_instance = None

flow_queue = Queue.Queue()


# Thread - getting flow from quene and calling functin from Stratospehre Detector
class ThreadQuene(Thread):

    def __init__(self):
        Thread.__init__(self)
        self.tuples_dict = dict()
        self.ips_dict = dict()
        self.last_flow_time = None

    def run(self):
        self.read_from_queue()

    def read_from_queue(self):
        while True:
            if flow_queue.empty() is False:
                flow = flow_queue.get()
                split = flow.split(',')
                # Tuple: SRC IP, DST IP, DST PORT, PROTOCOL
                tuple_index = split[3], split[6], split[7], split[2]
                if tuple_index in self.tuples_dict.keys():
                    self.tuples_dict[tuple_index].add_flow(flow)
                else:
                    self.tuples_dict[tuple_index] = StratosphereTuple.Tuple([split[3], split[6], split[7], split[2]])
                    self.tuples_dict[tuple_index].add_flow(flow)

                # EVERY 5 SECONDS CHECK THE TUPLES
                now = datetime.datetime.strptime(split[0], '%Y/%m/%d %H:%M:%S.%f')
                if self.last_flow_time is not None:
                    if (now - self.last_flow_time).seconds > config_instance.time_windows_length:
                        # put the tuple label in to the ips dictionary according to ap
                        for i in self.tuples_dict:
                            # get label: netbot, normal, spam ...
                            label = StratosphereDetector.detect(self.tuples_dict[i].state)
                            ip = self.tuples_dict[i].tuple[0]
                            label_state = label
                            if self.ips_dict.has_key(ip):
                                label_state = self.ips_dict[ip] + label
                            self.ips_dict[ip] = label_state + '-'

                        # check if we recognize malicious
                        self.check_malicious()
                        # check lengths of tuple state
                        self.check_tuple_size()
                        # set new time
                        self.last_flow_time = now
                else:
                    self.last_flow_time = now

    def check_malicious(self):
        for i in self.ips_dict:
            split = self.ips_dict[i].split('-')
            normal = 0
            spam = 0
            for j in range(len(split)-1):
                # print 'split:', split[j]
                if split[j] == 'Normal':
                    normal += 1
                else:
                    spam += 1
            # print 'normal:', normal
            # print 'spam:', spam
            if normal > spam:
                StratosphereOutput.show('IP: ' + i + ' : ' + 'Everything is ok.', 3)
            elif normal <= spam:
                StratosphereOutput.show(('IP: ' + i + ' : ' + 'Something is recognized!'), 3)
        StratosphereOutput.show('Checking...', 3)

    def check_tuple_size(self):
        for i in self.tuples_dict:
            if len(self.tuples_dict[i].state) > config_instance.time_windows_length:
                self.tuples_dict[i].state = ''
                self.tuples_dict[i].list = []


def set_config_instance():
    StratosphereConfig()
    global config_instance
    config_instance = __import__('StratosphereConfig').StratosphereConfig.config_instance
    config_instance.check_config()

    # import config instance in 'StratosphereOutput'
    StratosphereOutput.import_instance()


if __name__ == "__main__":

    # import the config instance to the "config_instance".
    set_config_instance()

    t2 = ThreadQuene()
    t2.start()

    # Reading Flows from STDIN
    for line in sys.stdin:
        # print 'Flow', line
        flow_queue.put(line)

    # Wait for end of analyze
    while flow_queue.empty() is False:
        time.sleep(3)

    # Print Dictionary
    f = open('TupleFile', 'w')
    for i in t2.tuples_dict:
        StratosphereOutput.show(('- [%s]: %s' % (', '.join(map(str, i)), t2.tuples_dict[i].state)), 3)
        f.write('[%s]:     %s\n' % (t2.tuples_dict[i].state, ', '.join(map(str, i))))
    f.close()

    StratosphereOutput.show('Results:', 3)
    print len(t2.ips_dict)
    for i in t2.ips_dict:
        StratosphereOutput.show(('state: ', t2.ips_dict[i]), 3)