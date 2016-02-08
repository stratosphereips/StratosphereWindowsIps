__author__ = 'Frenky'

import ConfigParser
import datetime
import warnings


class StratosphereConfig:

    config_instance = None

    def __init__(self):
        if StratosphereConfig.config_instance is None:
            StratosphereConfig.config_instance = StratosphereConfig.SingletonConfig()
        else:
            warnings.warn('Another instance of ConfigFile is running.')

    class SingletonConfig:

        def __init__(self):
            # STRATOSPHERE_WINDOW
            self.days_update_again = 3
            self.is_forbidden = False
            self.date_string = str(datetime.date.today())
            self.check_if_process_work = 3
            self.url_to_classes = 'https://raw.githubusercontent.com/stratosphereips/StratosphereIps/Frenky/StratosphereWindowsIPS/StratosphereWindow.py'
            self.url_to_modules = 'http://mcfp.felk.cvut.cz/stratosphere/stratospherewindowsips/modules/modules.zip'
            self.url_to_models = 'http://mcfp.felk.cvut.cz/stratosphere/stratospherewindowsips/models/models.zip'
            self.length_of_state = 100
            self.time_windows_length = 300
            # STRATOSPHERE_WATCHER
            self.run_on_start = True
            # STRATOSPHERE OUTPUT
            self.verbose_option = 3
            self.config = None

        def check_config(self):
            file_name = 'configfile.cfg'
            self.config = ConfigParser.ConfigParser(allow_no_value = True)

            self.config.read(file_name)
            try:
                self.days_update_again = self.config.getint('STRATOSPHERE_WINDOW', 'DAYS_UPDATE_AGAIN')
                self.is_forbidden = self.config.getboolean('STRATOSPHERE_WINDOW', 'DONT_UPDATE')
                self.date_string = self.config.get('STRATOSPHERE_WINDOW', 'DATE_OF_NEXT_UPDATE')
                self.url_to_classes = self.config.get('STRATOSPHERE_WINDOW', 'UPDATE_URL_CLASSES')
                self.check_if_process_work = self.config.getint('STRATOSPHERE_WINDOW', 'CHECK_IF_UP_EVERY')
                self.length_of_state = self.config.getint('STRATOSPHERE_WINDOW', 'LENGTH_OF_STATE')
                self.time_windows_length = self.config.getint('STRATOSPHERE_WINDOW', 'TIME_WINDOWS_LENGTH')
                self.verbose_option = self.config.getint('STRATOSPHERE_OUTPUT', 'VERBOSE_OPTION')
                self.url_to_modules = self.config.get('STRATOSPHERE_WINDOW', 'UPDATE_URL_MODULES')
                self.url_to_models = self.config.get('STRATOSPHERE_WINDOW', 'UPDATE_URL_MODELS')

            except:
                # FIRST SECTION
                self.config.add_section('STRATOSPHERE_WINDOW')

                self.config.set('STRATOSPHERE_WINDOW', '; IF YOU WANT TO UPDATE THIS APPLICATION DONT_UPDATE = False, OTHERWISE DONT_UPDATE = True.')
                self.config.set('STRATOSPHERE_WINDOW', 'DONT_UPDATE',  self.is_forbidden)
                self.config.set('STRATOSPHERE_WINDOW', '; DATE OF NEXT UPDATE (MODULES, MODELS, APPLICATION).')
                self.config.set('STRATOSPHERE_WINDOW', 'DATE_OF_NEXT_UPDATE', self.date_string)
                self.config.set('STRATOSPHERE_WINDOW', '; NUMBER OF DAYS, WHEN NEXT UPADTE WILL BE.')
                self.config.set('STRATOSPHERE_WINDOW', 'DAYS_UPDATE_AGAIN', self.days_update_again)
                self.config.set('STRATOSPHERE_WINDOW', '; NUMBER IN SECONDS, WHICH CHECK IF THE PROCESS FOR DETECTING RUNS.')
                self.config.set('STRATOSPHERE_WINDOW', 'CHECK_IF_UP_EVERY', self.check_if_process_work)
                self.config.set('STRATOSPHERE_WINDOW', '; URL FOR UPDATING.')
                self.config.set('STRATOSPHERE_WINDOW', 'UPDATE_URL_CLASSES', self.url_to_classes)
                self.config.set('STRATOSPHERE_WINDOW', 'UPDATE_URL_MODULES', self.url_to_modules)
                self.config.set('STRATOSPHERE_WINDOW', 'UPDATE_URL_MODELS', self.url_to_models)
                self.config.set('STRATOSPHERE_WINDOW', '; LENGTH OF STATE FOR EACH TUPLE.')
                self.config.set('STRATOSPHERE_WINDOW', 'LENGTH_OF_STATE', self.length_of_state)
                self.config.set('STRATOSPHERE_WINDOW', '; TIME IN SECONDS FOR ANALYZE TUPLES')
                self.config.set('STRATOSPHERE_WINDOW', 'TIME_WINDOWS_LENGTH', self.time_windows_length)

                # SECOND SECTION
                self.config.add_section('STRATOSPHERE_WATCHER')
                self.config.set('STRATOSPHERE_WATCHER', 'RUN_ON_START_UP', self.run_on_start)
                # THIRD SECTION
                self.config.add_section('STRATOSPHERE_OUTPUT')
                self.config.set('STRATOSPHERE_OUTPUT', '; IT IS NUMBER FROM 0 TO 3. 0=NOTHING PRINTED TO CONSOL, 3=EVERYTHING IS PRINTED TO CONSOL.')
                self.config.set('STRATOSPHERE_OUTPUT', 'VERBOSE_OPTION', self.verbose_option)

                with open(file_name, 'wb') as configfile:
                    self.config.write(configfile)

        # Set new date for uodate (default is today + 3 days)
        def set_config(self):
            # StratosphereOutput.show('Setting Config file.', 2)
            next_update = datetime.date.today() + datetime.timedelta(self.days_update_again)

            file_name = 'configfile.cfg'
            self.config.read(file_name)
            self.config.set('STRATOSPHERE_WINDOW', 'DATE_OF_NEXT_UPDATE', next_update)
            with open(file_name, 'wb') as configfile:
                self.config.write(configfile)














# # STRATOSPHERE_WINDOW
# days_update_again = 3
# is_forbidden = False
# date_string = str(datetime.date.today())
# check_if_process_work = 3
# url_to_classes = 'https://raw.githubusercontent.com/stratosphereips/StratosphereIps/Frenky/StratosphereWindowsIPS/StratosphereWindow.py'
# url_to_modules = 'http://mcfp.felk.cvut.cz/stratosphere/stratospherewindowsips/modules/modules.zip'
# url_to_models = 'http://mcfp.felk.cvut.cz/stratosphere/stratospherewindowsips/models/models.zip'
# length_of_state = 100
# time_for_check_flows = 300
# # STRATOSPHERE_WATCHER
# run_on_start = True
# # STRATOSPHERE OUTPUT
# verbose_option = 3
#
#
# def check_config():
#     global days_update_again
#     global is_forbidden
#     global date_string
#     global check_if_process_work
#     global url_to_classes
#     global length_of_state
#     global time_for_check_flows
#     global run_on_start
#     global verbose_option
#     global url_to_modules
#     global url_to_models
#
#     file_name = 'configfile.cfg'
#     ConfigParser.ConfigParser.add_comment = lambda self, section, option, value: self.set(section, '; '+option, value)
#     config = ConfigParser.ConfigParser()
#     config.read(file_name)
#     try:
#         days_update_again = config.getint('STRATOSPHERE_WINDOW', 'DAYS_UPDATE_AGAIN')
#         is_forbidden = config.getboolean('STRATOSPHERE_WINDOW', 'DONT_UPDATE')
#         date_string = config.get('STRATOSPHERE_WINDOW', 'DATE_OF_NEXT_UPDATE')
#         url_to_classes = config.get('STRATOSPHERE_WINDOW', 'UPDATE_URL_CLASSES')
#         check_if_process_work = config.getint('STRATOSPHERE_WINDOW', 'CHECK_IF_UP_EVERY')
#         length_of_state = config.getint('STRATOSPHERE_WINDOW', 'LENGTH_OF_STATE')
#         time_for_check_flows = config.getint('STRATOSPHERE_WINDOW', 'TIME_FOR_CHECK_FLOWS')
#         verbose_option = config.getint('STRATOSPHERE_OUTPUT', 'VERBOSE_OPTION')
#         url_to_modules = config.get('STRATOSPHERE_WINDOW', 'UPDATE_URL_MODULES')
#         url_to_models = config.get('STRATOSPHERE_WINDOW', 'UPDATE_URL_MODELS')
#
#     except:
#         # FIRST SECTION
#         config.add_section('STRATOSPHERE_WINDOW')
#         # config.add_comment('STRATOSPHERE_WINDOW', 'Updating (True or False)', 3)
#         config.set('STRATOSPHERE_WINDOW', 'DONT_UPDATE',  is_forbidden)
#         config.set('STRATOSPHERE_WINDOW', 'DATE_OF_NEXT_UPDATE', date_string)
#         config.set('STRATOSPHERE_WINDOW', 'DAYS_UPDATE_AGAIN', days_update_again)
#         config.set('STRATOSPHERE_WINDOW', 'CHECK_IF_UP_EVERY', check_if_process_work)
#         config.set('STRATOSPHERE_WINDOW', 'UPDATE_URL_CLASSES', url_to_classes)
#         config.set('STRATOSPHERE_WINDOW', 'LENGTH_OF_STATE', length_of_state)
#         config.set('STRATOSPHERE_WINDOW', 'TIME_FOR_CHECK_FLOWS', time_for_check_flows)
#         config.set('STRATOSPHERE_WINDOW', 'UPDATE_URL_MODULES', url_to_modules)
#         config.set('STRATOSPHERE_WINDOW', 'UPDATE_URL_MODELS', url_to_models)
#         # SECOND SECTION
#         config.add_section('STRATOSPHERE_WATCHER')
#         config.set('STRATOSPHERE_WATCHER', 'RUN_ON_START_UP', run_on_start)
#         # THIRD SECTION
#         config.add_section('STRATOSPHERE_OUTPUT')
#         config.set('STRATOSPHERE_OUTPUT', 'VERBOSE_OPTION', verbose_option)
#
#         with open(file_name, 'wb') as configfile:
#             config.write(configfile)
#
#
# def set_config():
#     # StratosphereOutput.show('Setting Config file.', 2)
#     next_update = datetime.date.today() + datetime.timedelta(days_update_again)
#
#     file_name = 'configfile.cfg'
#     config = ConfigParser.RawConfigParser()
#     config.read(file_name)
#     config.set('STRATOSPHERE_WINDOW', 'DATE_OF_NEXT_UPDATE', next_update)
#     with open(file_name, 'wb') as configfile:
#         config.write(configfile)
