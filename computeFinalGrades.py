# Code by Jakub Reha

import numpy as np
from roundGrade import roundGrade


def computeFinalGrades(grades):
    #input is a matrix
    gradesFinal = np.array([])
    #special case of having only one assignment
    if grades.shape[1] == 1:

       gradesFinal = grades 
    else:

        # the function separates the input matrix into particular lines and deals each one individually
        for i in range(0,grades.shape[0]):
            line = grades[i,:]
            #special case
            if np.isin(-3,line) == True:
                gradesFinal = np.append(gradesFinal, -3)
            else:
                #computes the unrounded final grade for each line (student)
                index = line.argmin()
                line = np.delete(line, index)
                gradesFinal = np.append(gradesFinal, np.mean(line))
    #output is an array, using a separate function to round the values
    return roundGrade(gradesFinal)
