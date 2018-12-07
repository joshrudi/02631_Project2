# Code by Jakub Reha
# Used from course documentation

import numpy as np
from inputNumber import inputNumber


def displayMenu(options):

    for i in range(len(options)):

        print("{:d}. {:s}".format(i+1, options[i]))
    choice = 0
    while not(np.any(choice == np.arange(len(options))+1)):

        choice = inputNumber("Please choose a menu item (1, 2, 3, etc): ")
    return choice
