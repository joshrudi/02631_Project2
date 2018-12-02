# Code by Jakub Reha

import numpy as np


def roundGrade(grades):

    scale = np.array([-3, 0, 2, 4, 7, 10, 12])
    # initializing an empty array which we will append the rounded grades to
    gradesRounded = ([])
    # we will go through the scale array and compare if the input grade to the scale grades
    for i in range(np.size(grades)):

        k = 0
        # if we already assign a rounded value to a grade, we end the while loop
        notAssigned = True
        while notAssigned:

            if grades[i] <= -3:

                    gradesRounded = np.append(gradesRounded, -3)
                    notAssigned = False
            elif grades[i] >= 12:

                    gradesRounded = np.append(gradesRounded, 12)
                    notAssigned = False
            elif grades[i] < scale[k]:

                if abs(grades[i] - scale[k-1]) < abs(grades[i] - scale[k]):

                   gradesRounded = np.append(gradesRounded, scale[k-1])
                   notAssigned = False
                else:

                    gradesRounded = np.append(gradesRounded, scale[k])
                    notAssigned = False
            k = k+1

    return gradesRounded
