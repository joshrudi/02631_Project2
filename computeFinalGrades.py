# Code by Jakub Reha

import numpy as np
from roundGrade import roundGrade


def computeFinalGrades(grades):

    gradesFinal = np.array([])

    if grades.shape[1] == 1:

       gradesFinal = grades 
    else:

        # the function separates the input matrix into particular lines and deals each one individually
        for i in range(0,grades.shape[0]):

            line = grades[i,:]
            if np.isin(-3,line) == True:
                gradesFinal = np.append(gradesFinal, -3)
            else:
                index = line.argmin()
                line = np.delete(line, index)
                gradesFinal = np.append(gradesFinal, np.mean(line))

    return roundGrade(gradesFinal)
