# Code by Joshua Rudaitis

import numpy as np


# takes in final grades and data for students, prints out all grades for all assignments per student as well as
# prints out (alphabetically sorted by name) the final grades for each student
def printGrades(grades, rawData):

    studentFinal = np.zeros([len(rawData)-1, 2]).astype(str)
    print("\nAll Grades: ")
    for i in range(2, len(rawData[0])):  # prints grades for all students

        for j in range(0, len(rawData)):

            if j < len(rawData)-1:

                studentFinal[j][0] = rawData[j+1][1]  # add name to final grades display
                studentFinal[j][1] = grades[j]  # add grade to final grades display

            print(rawData[j][i], end=", ")

        print("")  # formatting

    studentFinal = studentFinal[studentFinal[:, 0].argsort()]  # sorts grades alphabetically
    print("\nFinal Grades:")

    for i in range(0, len(studentFinal)):

        print(studentFinal[i][0] + ", " + studentFinal[i][1])

    # used to for spacing when printing menu
    print("")