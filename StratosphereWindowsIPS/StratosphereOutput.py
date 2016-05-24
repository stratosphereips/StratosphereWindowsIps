__author__ = 'Frenky'

import logging
import datetime
from StratosphereConfig import __StratosphereConfig__

logging.basicConfig(filename='LogFile.log', level=logging.DEBUG)


def show(text1, option):
    if option <= __StratosphereConfig__.get_int_verbose_option():
        if option == 1:
            print text1
        elif option == 2:
            print '      ', text1
        elif option == 3:
            print '             ', text1


# Wrtite to log file next message.
def log(message):
    logging.debug(str(datetime.datetime.now()) + ' -- ' + message)
