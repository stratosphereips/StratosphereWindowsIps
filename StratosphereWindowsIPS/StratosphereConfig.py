__author__ = 'Frenky'

import ConfigParser
import datetime


class StratosphereConfig:

    def __init__(self):
        # STRATOSPHERE_WINDOW
        self.days_update_again = 3
        self.is_forbidden = False
        self.date_string = str(datetime.date.today())
        self.check_if_process_work = 10
        self.url_to_classes = 'https://raw.githubusercontent.com/stratosphereips/StratosphereIps/Frenky/StratosphereWindowsIPS/StratosphereWindow.py'
        self.url_to_modules = 'http://mcfp.felk.cvut.cz/stratosphere/stratospherewindowsips/modules/modules.zip'
        self.url_to_models = 'http://mcfp.felk.cvut.cz/stratosphere/stratospherewindowsips/models/models.zip'
        self.length_of_state = 100
        self.time_windows_length = 300
        self.printAllLabels = False
        self.path_to_source_folder = 'C:\\Users\\frenk\\Documents\\Skola\\Stratosphere\\StratosphereWindowsIPS\\'
        # STRATOSPHERE_WATCHER
        self.run_on_start = True
        # STRATOSPHERE OUTPUT
        self.verbose_option = 3
        self.config = ConfigParser.ConfigParser(allow_no_value = True)
        self.check_config()

    def check_config(self):
        file_name = 'configfile.cfg'

        self.config.read(file_name)
        try:
            self.days_update_again = self.config.getint('STRATOSPHERE_WINDOW', 'DAYS_UPDATE_AGAIN')
            self.is_forbidden = self.config.getboolean('STRATOSPHERE_WINDOW', 'DONT_UPDATE')
            self.date_string = self.config.get('STRATOSPHERE_WINDOW', 'DATE_OF_NEXT_UPDATE')
            self.url_to_classes = self.config.get('STRATOSPHERE_WINDOW', 'UPDATE_URL_CLASSES')
            self.check_if_process_work = self.config.getint('STRATOSPHERE_WINDOW', 'CHECK_IF_UP_EVERY')
            self.length_of_state = self.config.getint('STRATOSPHERE_WINDOW', 'LENGTH_OF_STATE')
            self.time_windows_length = self.config.getint('STRATOSPHERE_WINDOW', 'TIME_WINDOWS_LENGTH')
            self.printAllLabels = self.config.getboolean('STRATOSPHERE_WINDOW', 'PRINT_ALL_LABELS')
            self.verbose_option = self.config.getint('STRATOSPHERE_OUTPUT', 'VERBOSE_OPTION')
            self.url_to_modules = self.config.get('STRATOSPHERE_WINDOW', 'UPDATE_URL_MODULES')
            self.url_to_models = self.config.get('STRATOSPHERE_WINDOW', 'UPDATE_URL_MODELS')
            self.path_to_source_folder = self.config.get('STRATOSPHERE_WINDOW', 'PATH_TO_SOURCE_FOLDER')

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
            self.config.set('STRATOSPHERE_WINDOW', '; PRINT ALL LABELS -> TRUE; PRINT LABELS, ONLY WHEN SOMETHING IS DETECTED -> FALSE')
            self.config.set('STRATOSPHERE_WINDOW', 'PRINT_ALL_LABELS', self.printAllLabels)
            self.config.set('STRATOSPHERE_WINDOW', '; PATH TO FOLDER, WHERE ALL FILES ARE LOCATED.')
            self.config.set('STRATOSPHERE_WINDOW', 'PATH_TO_SOURCE_FOLDER', self.path_to_source_folder)

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

    # Get days_update_again
    def get_int_days_update_again(self):
        return self.days_update_again

    def get_bool_forbidden(self):
        return self.is_forbidden

    def get_string_date_string(self):
        return self.date_string

    def get_int_check_if_process_work(self):
        return self.check_if_process_work

    def get_string_url_to_classes(self):
        return self.url_to_classes

    def get_string_url_to_modules(self):
        return self.url_to_modules

    def get_string_url_to_models(self):
        return self.url_to_models

    def get_int_length_of_state(self):
        return self.length_of_state

    def get_int_time_windows_length(self):
        return self.time_windows_length

    def get_bool_run_on_start(self):
        return self.run_on_start

    def get_int_verbose_option(self):
        return self.verbose_option

    def get_bool_print_all_labels(self):
        return self.printAllLabels

    def get_path_to_source_folder(self):
        return self.path_to_source_folder

__StratosphereConfig__ = StratosphereConfig()
