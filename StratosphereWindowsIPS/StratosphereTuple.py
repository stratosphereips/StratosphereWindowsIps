__author__ = 'Frenky'

import datetime
import StratosphereOutput

# Tuple: SRC IP, DST IP, DST PORT, PROTOCOL


class Tuple:

    letter_table = [['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'],
                     ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'],
                     ['r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],
                     ['R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'],
                     ['1', '2', '3', '4', '5', '6', '7', '8', '9']]

    def __init__(self, tuple, protocol):
        self.state = ''
        self.tuple = tuple
        self.protocol = protocol
        self.time_1 = None
        self.time_2 = None
        self.time_3 = None
        self.list = []

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
        # take protocol from
        # time_1 from flow
        self.time_1 = datetime.datetime.strptime(split[0], '%Y/%m/%d %H:%M:%S.%f')

        # Computing of periodicity
        symbol = ''
        is_zero = False
        if self.time_2 is not None:
            T2 = (self.time_1 - self.time_2).total_seconds()

        if (self.time_2 is not None) and (self.time_3 is not None):
            T1 = (self.time_2 - self.time_3).total_seconds()

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
            # No data
            row = 4

        # -----------------------------
        # ----- First part: zeros -----
        # -----------------------------
        zeros = ''
        if (self.time_2 is not None) and (T2 > 3600):
            temp = int(T2 / 3600)
            for i in range(temp):
                zeros += '0'
        else:
            if (self.time_2 is not None) and (self.time_3 is not None) and (T1 > 3600):
                temp = int(T1 / 3600)
                for i in range(temp):
                    zeros += '0'

        # --------------------------------------
        # ---- Third part: Create symbol -------
        # --------------------------------------
        if self.time_2 is not None:
            # Symbols (0 , . + *)
            if (T2 > 0) and (T2 <= 5):
                symbol = '.'
            elif (T2 > 5) and (T2 <= 60):
                symbol = ','
            elif (T2 > 60) and (T2 <= 300):
                symbol = '+'
            elif (T2 > 300) and (T2 <= 3600):
                # isZero = True
                symbol = '*'

        # -------------------------------------------
        # ------- Second part: Create letter --------
        # -------------------------------------------
        if size <= 250:
            if duration <= 0.1:
                column = 0
            elif (duration > 0.1) and (duration <= 10):
                column = 1
            elif duration > 10:
                column = 2
        elif (size > 250) and (size <= 1100):
             if duration <= 0.1:
                column = 3
             elif (duration > 0.1) and (duration <= 10):
                column = 4
             elif duration > 10:
                column = 5
        elif size > 1100:
             if duration <= 0.1:
                column = 6
             elif (duration > 0.1) and (duration <= 10):
                column = 7
             elif duration > 10:
                column = 8

        # Append 3 parts together -> "zeros + letter + symbol."
        result = zeros + self.letter_table[row][column] + symbol

        # Add result to state
        self.state += result

        # switch time
        self.time_3 = self.time_2
        self.time_2 = self.time_1

        StratosphereOutput.show('Flow = ' + str(split), 4)
        StratosphereOutput.log('Flow = ' + str(split))

        StratosphereOutput.show('State: ' + self.state, 4)
        StratosphereOutput.log('State: ' + self.state)

    def get_id(self):
        return self.tuple

    def get_protocol(self):
        return self.protocol

    def get_state(self):
        return self.state

    def set_state(self, new_state):
        self.state = new_state

    def set_list(self):
        self.list = []

    def set_times(self):
        self.time_1 = None
        self.time_2 = None
        self.time_3 = None



