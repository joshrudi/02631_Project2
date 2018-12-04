# Code by Jakub Reha

import numpy as np

#function takes in an array of grades and returns an array with those grades rounded to the scale grades
def roundGrade(grades):
    #scale grades
    scale = np.array([-3, 0, 2, 4, 7, 10, 12])
    # initializing an empty array which we will append the rounded grades to
    gradesRounded = ([])
    # we will go through the scale array (while loop) for each of the input grades (for loop) and determine which one is the closest
    for i in range(np.size(grades)):

        k = 0
        # if we already assign a rounded value to a grade, we end the while loop
        notAssigned = True
        while notAssigned:
            #first we treat special cases
            if grades[i] <= -3:

                    gradesRounded = np.append(gradesRounded, -3)
                    notAssigned = False
            elif grades[i] >= 12:

                    gradesRounded = np.append(gradesRounded, 12)
                    notAssigned = False
            #determines between which two scale grades the input grade lies        
            elif grades[i] < scale[k]:
                #then compute which scale grade is the closer one
                if abs(grades[i] - scale[k-1]) < abs(grades[i] - scale[k]):

                   gradesRounded = np.append(gradesRounded, scale[k-1])
                   notAssigned = False
                else:

                    gradesRounded = np.append(gradesRounded, scale[k])
                    notAssigned = False
            k = k+1

    return gradesRounded
