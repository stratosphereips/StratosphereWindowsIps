__author__ = 'Frenky'
import Queue
import StratosphereDetector
import Tuple
import sys, time
from threading import Thread

flow_queue = Queue.Queue()


# Thread - getting flow from quene and calling functin from Stratospehre Detector
class ThreadQuene(Thread):

    def __init__(self):
        Thread.__init__(self)
        self.dictionary = dict()

    def run(self):
        while True:
            flow = flow_queue.get()
            split = flow.split(',')
            # Tuple: SRC IP, DST IP, DST PORT, PROTOCOL
            tuple_index = split[3], split[6], split[7], split[2]
            if tuple_index in self.dictionary.keys():
                self.dictionary[tuple_index].add_flow(flow)
            else:
                self.dictionary[tuple_index] = Tuple.Tuple([split[3], split[6], split[7], split[2]])
                self.dictionary[tuple_index].add_flow(flow)

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
    for i in t2.dictionary:
        print ('[%s]: %s' % (', '.join(map(str, i)), t2.dictionary[i].state))
        f.write('[%s]:     %s\n' % (t2.dictionary[i].state, ', '.join(map(str, i))))
    f.close()