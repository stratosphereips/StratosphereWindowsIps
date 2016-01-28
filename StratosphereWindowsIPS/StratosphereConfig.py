__author__ = 'Frenky'

import ConfigParser
import datetime


# STRATOSPHERE_WINDOW
days_update_again = 3
is_forbidden = False
date_string = str(datetime.date.today())
check_if_process_work = 3
url_string = 'https://raw.githubusercontent.com/stratosphereips/StratosphereIps/Frenky/StratosphereWindowsIPS/StratosphereWindow.py'
length_of_state = 100
time_for_check_flows = 300
# STRATOSPHERE_WATCHER
run_on_start = True
# STRATOSPHERE OUTPUT
verbose_option = 3


def check_config():
    global days_update_again
    global is_forbidden
    global date_string
    global check_if_process_work
    global url_string
    global length_of_state
    global time_for_check_flows
    global run_on_start
    global verbose_option

    file_name = 'configfile.cfg'
    ConfigParser.ConfigParser.add_comment = lambda self, section, option, value: self.set(section, '; '+option, value)
    config = ConfigParser.ConfigParser()
    config.read(file_name)
    try:
        days_update_again = config.getint('STRATOSPHERE_WINDOW', 'DAYS_UPDATE_AGAIN')
        is_forbidden = config.getboolean('STRATOSPHERE_WINDOW', 'DONT_UPDATE')
        date_string = config.get('STRATOSPHERE_WINDOW', 'DATE_OF_NEXT_UPDATE')
        url_string = config.get('STRATOSPHERE_WINDOW', 'UPDATE_URL')
        check_if_process_work = config.getint('STRATOSPHERE_WINDOW', 'CHECK_IF_UP_EVERY')
        length_of_state = config.getint('STRATOSPHERE_WINDOW', 'LENGTH_OF_STATE')
        time_for_check_flows = config.getint('STRATOSPHERE_WINDOW', 'TIME_FOR_CHECK_FLOWS')
        verbose_option = config.getint('STRATOSPHERE_OUTPUT', 'VERBOSE_OPTION')

    except:
        # FIRST SECTION
        config.add_section('STRATOSPHERE_WINDOW')
        config.add_comment('STRATOSPHERE_WINDOW', 'Updating (True or False)', 3)
        config.set('STRATOSPHERE_WINDOW', 'DONT_UPDATE',  is_forbidden)
        config.set('STRATOSPHERE_WINDOW', 'DATE_OF_NEXT_UPDATE', date_string)
        config.set('STRATOSPHERE_WINDOW', 'DAYS_UPDATE_AGAIN', days_update_again)
        config.set('STRATOSPHERE_WINDOW', 'CHECK_IF_UP_EVERY', check_if_process_work)
        config.set('STRATOSPHERE_WINDOW', 'UPDATE_URL', url_string)
        config.set('STRATOSPHERE_WINDOW', 'LENGTH_OF_STATE', length_of_state)
        config.set('STRATOSPHERE_WINDOW', 'TIME_FOR_CHECK_FLOWS', time_for_check_flows)
        # SECOND SECTION
        config.add_section('STRATOSPHERE_WATCHER')
        config.set('STRATOSPHERE_WATCHER', 'RUN_ON_START_UP', run_on_start)
        # THIRD SECTION
        config.add_section('STRATOSPHERE_OUTPUT')
        config.set('STRATOSPHERE_OUTPUT', 'VERBOSE_OPTION', verbose_option)

        with open(file_name, 'wb') as configfile:
            config.write(configfile)


def set_config():
    # StratosphereOutput.show('Setting Config file.', 2)
    next_update = datetime.date.today() + datetime.timedelta(days_update_again)

    file_name = 'configfile.cfg'
    config = ConfigParser.RawConfigParser()
    config.read(file_name)
    config.set('STRATOSPHERE_WINDOW', 'DATE_OF_NEXT_UPDATE', next_update)
    with open(file_name, 'wb') as configfile:
        config.write(configfile)










#
#
# class ConfigFile:
#
#     # STRATOSPHERE_WINDOW
#     days_update_again = 3
#     is_forbidden = False
#     date_string = str(datetime.date.today())
#     check_if_process_work = 3
#     url_string = 'https://raw.githubusercontent.com/stratosphereips/StratosphereIps/Frenky/StratosphereWindowsIPS/StratosphereWindow.py'
#     length_of_state = 100
#     time_for_check_flows = 300
#     # STRATOSPHERE_WATCHER
#     run_on_start = True
#     # STRATOSPHERE OUTPUT
#     verbose_option = 3
#
#
#
#     def __init__(self):
#         self.check_config()
#
#     def check_config(self):
#         global days_update_again
#         global is_forbidden
#         global date_string
#         global check_if_process_work
#         global url_string
#         global length_of_state
#         global time_for_check_flows
#         global run_on_start
#         global verbose_option
#
#         file_name = 'configfile.cfg'
#         config = ConfigParser.RawConfigParser()
#         config.read(file_name)
#         try:
#             self.days_update_again = config.getint('STRATOSPHERE_WINDOW', 'DAYS_UPDATE_AGAIN')
#             self.is_forbidden = config.getboolean('STRATOSPHERE_WINDOW', 'DONT_UPDATE')
#             self.date_string = config.get('STRATOSPHERE_WINDOW', 'DATE_OF_NEXT_UPDATE')
#             self.url_string = config.get('STRATOSPHERE_WINDOW', 'UPDATE_URL')
#             self.check_if_process_work = config.getint('STRATOSPHERE_WINDOW', 'CHECK_IF_UP_EVERY')
#             self.length_of_state = config.getint('STRATOSPHERE_WINDOW', 'LENGTH_OF_STATE')
#             self.time_for_check_flows = config.getint('STRATOSPHERE_WINDOW', 'TIME_FOR_CHECK_FLOWS')
#             self.verbose_option = config.getint('STRATOSPHERE_OUTPUT', 'VERBOSE_OPTION')
#
#         except:
#             # StratosphereOutput.show("There is no config file or config file is not valid.", 1)
#             # StratosphereOutput.show('Creating new config file.', 1)
#
#             # FIRST SECTION
#             config.add_section('STRATOSPHERE_WINDOW')
#             config.set('STRATOSPHERE_WINDOW', '; Updating (True or False)', '')
#             config.set('STRATOSPHERE_WINDOW', 'DONT_UPDATE', self.is_forbidden)
#             config.set('STRATOSPHERE_WINDOW', 'DATE_OF_NEXT_UPDATE', self.date_string)
#             config.set('STRATOSPHERE_WINDOW', 'DAYS_UPDATE_AGAIN', self.days_update_again)
#             config.set('STRATOSPHERE_WINDOW', 'CHECK_IF_UP_EVERY', self.check_if_process_work)
#             config.set('STRATOSPHERE_WINDOW', 'UPDATE_URL', self.url_string)
#             config.set('STRATOSPHERE_WINDOW', 'LENGTH_OF_STATE', self.length_of_state)
#             config.set('STRATOSPHERE_WINDOW', 'TIME_FOR_CHECK_FLOWS', self.time_for_check_flows)
#             # SECOND SECTION
#             config.add_section('STRATOSPHERE_WATCHER')
#             config.set('STRATOSPHERE_WATCHER', 'RUN_ON_START_UP', self.run_on_start)
#             # THIRD SECTION
#             config.add_section('STRATOSPHERE_OUTPUT')
#             config.set('STRATOSPHERE_OUTPUT', 'VERBOSE_OPTION', self.verbose_option)
#
#             with open(file_name, 'wb') as configfile:
#                 config.write(configfile)
#
#
# def set_config():
#     global days_update_again
#     global date_string
#     # StratosphereOutput.show('Setting Config file.', 2)
#     next_update = datetime.date.today() + datetime.timedelta(days_update_again)
#     date_string = next_update
#
#     file_name = 'configfile.cfg'
#     config = ConfigParser.RawConfigParser()
#     config.read(file_name)
#     config.set('STRATOSPHERE_WINDOW', 'DATE_OF_NEXT_UPDATE', next_update)
#     with open(file_name, 'wb') as configfile:
#         config.write(configfile)
#
