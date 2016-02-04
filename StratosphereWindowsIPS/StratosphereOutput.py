__author__ = 'Frenky'
config_instance = __import__('StratosphereConfig').StratosphereConfig.config_instance


def show(text1, option):
    if option <= config_instance.verbose_option:
        print text1