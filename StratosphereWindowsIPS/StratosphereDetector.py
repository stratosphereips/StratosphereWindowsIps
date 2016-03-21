__author__ = 'Frenky'
import random
from modules.markov_models_1 import __markov_models__


def detect(tuple):
    __markov_models__.set_models_folder('C:\\Users\\frenk\\Documents\\Skola\\Stratosphere\\StratosphereWindowsIPS\\models')
    #----------------------------------------
    #----------- Real option -------------------
    # Analyze state a return name of the result.
    (detected, label, matching_len) = __markov_models__.detect(tuple, 50)
    return (detected, label, matching_len)

    # # ----------------------------------------
    # # ------------ Test option ---------------
    # # Random label
    # label_number = random.randint(1, 16)
    # if label_number is 1:
    #     return ('', 'Botnet', '')
    # elif label_number is 2:
    #     return ('', 'Attack', '')
    # elif label_number is 3:
    #     return ('', 'Malware', '')
    # return ('', 'Normal', '')
