# Code by Joshua Rudaitis

import csv
from pathlib import Path


# takes in file path and, if path is valid, returns the data from the csv in a 2d array
# if path is valid, also prints number of students and number of assignments
# if path is invalid, prints error and returns []
def dataLoad(filename):

    if not Path(filename).is_file():  # if invalid file, print error

        print("Error: Invalid File Name/Path!\n")
        return []

    # open file
    f = open(filename)
    csvFile = csv.reader(f)

    data = []

    # load data from file
    for row in csvFile: data.append(row)

    f.close()

    # print information about file based on known characteristics
    print("\nFile: \"" + filename + "\" Loaded\nNumber of Students: " + str(len(data)-1) +
          "\nNumber of Assignments: " + str(len(data[0])-2) + "\n")

    return data
