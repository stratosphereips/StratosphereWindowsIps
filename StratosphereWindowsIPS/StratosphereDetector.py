__author__ = 'Frenky'
import random


def detect(state):
    # Analyze state a return name of the result.
    label_number = random.randint(1, 16)
    if label_number is 1:
        return 'Botnet'
    elif label_number is 2:
        return 'Attack'
    elif label_number is 3:
        return 'Malware'
    return 'Normal'
