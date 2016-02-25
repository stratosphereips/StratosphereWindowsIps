__author__ = 'Frenky'

import logging
import datetime

config_instance = None


def import_instance():
    # import 'config_instance', because we need to know verbose option from config file.
    global config_instance
    config_instance = __import__('StratosphereConfig').StratosphereConfig.config_instance
    # Logging
    logging.basicConfig(filename='LogFile.log', level=logging.DEBUG)


def show(text1, option):
    if option <= config_instance.verbose_option:
        if option == 1:
            print text1
        elif option == 2:
            print '      ', text1
        elif option == 3:
            print '             ', text1


# Wrtite to log file next message.
def log(message):
    logging.debug(str(datetime.datetime.now()) + ' -- ' + message)