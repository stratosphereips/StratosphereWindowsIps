__author__ = 'Frenky'


import win32event
import win32service
import win32serviceutil
import win32service
import win32serviceutil
import win32event
import win32con
import win32api
import subprocess
import time
import datetime
import sys
import random
import Queue




#######################################3
#PIPE
######################################

f = open('textTemp.txt', 'wb')
index = 0

while(index < 10):
    rand_number = random.randint(0, 100)

    tempText = '{}'.format(rand_number)
    space = ' '
    index_str = '{}\n'.format(index)

    text = tempText + space + index_str

    print text

    f.write(text)
    index += 1


f.write('Finish.......\n')
f.close()



###########################################
# Queue
##########################################

# q = Queue.Queue()
#
# f = open('textTemp.txt', 'wb')
# index = 0
#
# while(index < 10000):
#     rand_number = random.randint(0, 100)
#
#     tempText = '{}'.format(rand_number)
#     space = ' '
#     index_str = '{}\n'.format(index)
#
#     text = tempText + space + index_str
#
#     q.put(text)
#
#     f.write(text)
#     index += 1
#
#
# f.write('Finish.......\n')
# f.close()
#
# print "size of Queue: ", q.qsize()


