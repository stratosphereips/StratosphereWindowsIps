__author__ = 'Frenky'





import Queue
import StratosphereDetector
import sys,os,time
from threading import Thread,RLock


flow_queue = Queue.Queue()

class ct(Thread):
    def __init__(self,name,i):
        Thread.__init__(self)

        self.i = i
        self.name = name

    def run(self):
        # Thread 1
        if self.name is "t1":
            for line in sys.stdin:
                print 'Flow', line
                flow_queue.put(line)
                # time.sleep(1)

        # Thread 2 - getting flow from quene and calling functin from Stratospehre Detector
        if self.name is "t2":
            while (True):
                flow = flow_queue.get()
                print 'Getting flow from quene...'
                StratosphereDetector.analyze_flow(flow)
                time.sleep(1)



if __name__ == "__main__":

    t1 = ct("t1",5)
    t2 = ct("t2",5)

    t1.start()
    t2.start()












