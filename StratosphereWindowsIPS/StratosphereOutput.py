__author__ = 'Frenky'
import StratosphereConfig

# verbose_option = ConfigFile.verbose_option
verbose_option = StratosphereConfig.verbose_option

def show(text1, option):
    if option <= verbose_option:
        print text1