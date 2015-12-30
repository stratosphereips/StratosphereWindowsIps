__author__ = 'Frenky'
import Queue
import StratosphereDetector
import sys, time
from threading import Thread

flow_queue = Queue.Queue()


# Thread - getting flow from quene and calling functin from Stratospehre Detector
class ThreadQuene(Thread):

    def __init__(self):
        Thread.__init__(self)

    def run(self):
        while True:
            flow = flow_queue.get()
            print 'Getting flow from quene...'
            StratosphereDetector.analyze_flow(flow)
            # time.sleep(1)

if __name__ == "__main__":

    t2 = ThreadQuene()
    t2.start()

    # Reading Flows from STDIN
    for line in sys.stdin:
        print 'Flow', line
        flow_queue.put(line)
        # time.sleep(1)
