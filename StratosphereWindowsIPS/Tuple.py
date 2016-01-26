__author__ = 'Frenky'

import datetime

#
# Tuple: SRC IP, DST IP, DST PORT, PROTOCOL
#


class Tuple:

    letter_table = [['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'],
                     ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'],
                     ['r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],
                     ['R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'],
                     ['1', '2', '3', '4', '5', '6', '7', '8', '9']]

    list = []

    def __init__(self, tuple):
        self.state = ''
        self.tuple = tuple
        self.time_1 = None
        self.time_2 = None
        self.time_3 = None

    def add_flow(self, flow):
        self.list.append(flow)
        self.compute_state(flow)

    def compute_state(self, flow):
        # Devide the Flow
        split = flow.split(',')
        # Get size of the Flow
        size = float(split[12])
        # Get the duration
        duration = float(split[1])
        # time_1 from flow
        self.time_1 = datetime.datetime.strptime(split[0], '%Y/%m/%d %H:%M:%S.%f')

        # Computing of periodicity
        symbol = ''
        isZero = False

        if self.time_2 is not None:
            T2 = (self.time_1 - self.time_2).total_seconds()

        if (self.time_2 is not None) and (self.time_3 is not None):
            T1 = (self.time_2 - self.time_3).total_seconds()
            # T2 = (self.time_1 - self.time_2).total_seconds()

            # print 'T1:', T1
            # print 'T2:', T2

            if T1 > T2:
                TD = T1/T2
            else:
                TD = T2/T1

            if TD <= 1.05:
                row = 0
            elif (TD > 1.05) and (TD <= 1.3):
                row = 1
            elif (TD > 1.3) and (TD <= 5):
                row = 2
            elif TD > 5:
                row = 3

        else:
            row = 4
        # print 'ROW:',row
        if self.time_2 is not None:
              # Symbols (0 , . + *)
            if (T2 > 0) and (T2 <= 5):
                symbol = '.'
            elif (T2 > 5) and (T2 <= 60):
                symbol = ','
            elif (T2 > 60) and (T2 <= 300):
                symbol = '+'
            elif (T2 > 300) and (T2 <= 3600):
                isZero = True
                symbol = '0'
            elif T2 > 3600:
                isZero = True
                temp = int(T2 / 3600)
                symbol = ''
                for i in range(temp):
                    symbol += '0'


        # size and duration of flow
        if size <= 250:
            if duration <= 0.1:
                column = 0
            elif (duration > 0.1) and (duration <= 10):
                column = 1
            elif(duration >10):
                column = 2
        elif (size > 250) and (size <= 1100):
             if duration <= 0.1:
                column = 3
             elif (duration > 0.1) and (duration <= 10):
                column = 4
             elif(duration >10):
                column = 5
        elif size > 1100:
             if duration <= 0.1:
                column = 6
             elif (duration > 0.1) and (duration <= 10):
                column = 7
             elif(duration >10):
                column = 8
        # print 'COLUMN', column

        if isZero is False:
            result = self.letter_table[row][column] + symbol
        else:
            result = symbol + self.letter_table[row][column]

        # Add result to state
        self.state += result
        # print 'STAV:', self.state

        # switch time
        self.time_3 = self.time_2
        self.time_2 = self.time_1


# if __name__ == "__main__":
#
#     tup = Tuple('tuple')
#
#     flow = '2015/12/10 10:34:58.324494,0.000000,udp,147.32.83.157,57621,   ->,147.32.83.255,57621,REQ,0,,1,86,86,PF'
#     tup.add_flow(flow)
#     flow = '2015/12/10 10:35:00.324494,0.000000,udp,147.32.83.157,57621,   ->,147.32.83.255,57621,REQ,0,,1,86,86,PF'
#     tup.add_flow(flow)
#     flow = '2015/12/10 10:35:02.324494,0.000000,udp,147.32.83.157,57621,   ->,147.32.83.255,57621,REQ,0,,1,86,86,PF'
#     tup.add_flow(flow)
#     flow = '2015/12/10 10:35:20.324494,0.000000,udp,147.32.83.157,57621,   ->,147.32.83.255,57621,REQ,0,,1,86,86,PF'
#     tup.add_flow(flow)




