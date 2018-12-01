import numpy as np


# takes in 2d array, and removes the title row, id column and name column.  Returns this modified array
def convertArray(studentStats):

    data = np.copy(studentStats)
    data = np.delete(data, 0, 0)  # remove first row  (StudentID, Name, Assignment1, etc...)
    data = np.delete(data, 0, 1)  # remove first col  (sXXXXXX, sXXXXXX, etc...)
    data = np.delete(data, 0, 1)  # remove second col (Michael Andersen, Bettina Petersen, etc...)
    data = np.array(data).astype(int)
    return data
