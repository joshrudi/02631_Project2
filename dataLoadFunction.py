import csv
from pathlib import Path


# takes in file path and, if path is valid, returns the data from the csv in a 2d array
# if path is valid, also prints number of students and number of assignments
# if path is invalid, prints error and returns []
def dataLoad(filename):

    if not Path(filename).is_file():

        print("Error: Invalid File Name/Path!\n")
        return []

    f = open(filename)
    csv_f = csv.reader(f)

    data = []

    for row in csv_f: data.append(row)

    f.close()

    print("\nFile: \"" + filename + "\" Loaded\nNumber of Students: " + str(len(data)-1) +
          "\nNumber of Assignments: " + str(len(data[0])-2) + "\n")

    return data
