__author__ = 'Frenky'
import random


def detect(state):
    label_number = random.randint(1,4)
    if label_number is 1:
        return 'NETBOT'
    return 'NORMAL'
