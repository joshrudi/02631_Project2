# Code by Joshua Rudaitis

import numpy as np


# takes in final grades and data for students, prints out all grades for all assignments per student as well as
# prints out (alphabetically sorted by name) the final grades for each student
def printGrades(grades, rawData):

    studentFinal = np.zeros([len(rawData)-1, 2]).astype(str)
    print("\nAll Grades: ")
    for i in range(1, len(rawData)):  # prints grades for all students

        studentFinal[i-1][0] = rawData[i][1]  # add name to final grades display
        studentFinal[i-1][1] = grades[i-1]    # add grade to final grades display
        for j in range(0, len(rawData[0])):

            print(rawData[i][j], end=" ")

        print("")  # formatting

    studentFinal = studentFinal[studentFinal[:, 0].argsort()]  # sorts grades alphabetically
    print("\nFinal Grades:")

    for i in range(0, len(studentFinal)):

        print(studentFinal[i][0] + ", " + studentFinal[i][1])

    # used to for spacing when printing menu
    print("")