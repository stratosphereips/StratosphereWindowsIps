__author__ = 'Frenky'
import Queue
import StratosphereDetector
import Tuple
import sys
import time
import datetime
from threading import Thread

flow_queue = Queue.Queue()


# Thread - getting flow from quene and calling functin from Stratospehre Detector
class ThreadQuene(Thread):

    def __init__(self):
        Thread.__init__(self)
        self.tuples_dict = dict()
        self.ips_dict = dict()

    def run(self):
        # READING FROM QUEUE
        last_time_dt = datetime.datetime.now()
        while True:
            if flow_queue.empty() is False:
                flow = flow_queue.get()
                split = flow.split(',')
                # Tuple: SRC IP, DST IP, DST PORT, PROTOCOL
                tuple_index = split[3], split[6], split[7], split[2]
                if tuple_index in self.tuples_dict.keys():
                    self.tuples_dict[tuple_index].add_flow(flow)
                else:
                    self.tuples_dict[tuple_index] = Tuple.Tuple([split[3], split[6], split[7], split[2]])
                    self.tuples_dict[tuple_index].add_flow(flow)

            # EVERY 5 SECONDS CHECK THE TUPLES
            now = datetime.datetime.now()
            if (now - last_time_dt).seconds > 5:
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
                last_time_dt = datetime.datetime.now()

    def check_malicious(self):
        for i in self.ips_dict:
            split = self.ips_dict[i].split('-')
            normal = 0
            spam = 0
            for j in range(len(split)-1):
                # print 'split:', split[j]
                if split[j] == 'NORMAL':
                    normal += 1
                else:
                    spam += 1
            print 'normal:', normal
            print 'spam:', spam
            if normal > spam:
                print 'IP: ' + i + ' : ' + 'Everything is ok.'
            elif normal <= spam:
                print 'IP: ' + i + ' : ' + 'Spam is recognized!'
        print '---------------------'

if __name__ == "__main__":

    t2 = ThreadQuene()
    t2.start()

    # Reading Flows from STDIN
    for line in sys.stdin:
        # print 'Flow', line
        flow_queue.put(line)

    # Wait for end of analyze
    time.sleep(2)

    # Print Dictionary
    f = open('TupleFile', 'w')
    for i in t2.tuples_dict:
        print ('[%s]: %s' % (', '.join(map(str, i)), t2.tuples_dict[i].state))
        f.write('[%s]:     %s\n' % (t2.tuples_dict[i].state, ', '.join(map(str, i))))
    f.close()