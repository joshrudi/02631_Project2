# Code by Joshua Rudaitis

# takes in a row (1d array), and prints error if grade is not a '7-step-scale' grade
def verifyScale(row):

    for i in range(2, len(row)):

        if (row[i] != "12" and row[i] != "10" and row[i] != "7" and row[i] != "4" and row[i] != "02"
                and row[i] != "00" and row[i] != "-3"):

            print("\n! Error: Grade not a '7-Step-Scale' grade, " + row[0] + " " + row[1] +
                  "; Assignment " + str(i-1) + "; Invalid Grade [" + row[i] + "]\n")


# takes in 2d array of values, and handles printing any errors (conflicting IDs or invalid grade)
def checkError(data):

    hashMap = dict()

    # for each row in 2d array, checks if conflicting IDs exist (via hashMap) and uses above helper function
    # to see if grades are valid '7-step-scale' grades
    for i in range(1, len(data)):

        # if we have encountered this ID before, print error
        if data[i][0] in hashMap: print("\n! Error: Duplicate student ID found, " + data[i][0] + "; " + data[i][1] +
                                        " | " + data[i][0] + "; " + hashMap[data[i][0]] + "\n")

        # else add it to the hashMap
        else: hashMap[data[i][0]] = data[i][1]

        verifyScale(data[i])
