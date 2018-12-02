# Code by Joshua Rudaitis

import numpy as np
from dataLoadFunction import dataLoad
from displayMenu import displayMenu
from errorCheck import checkError
from computeFinalGrades import computeFinalGrades
from convertArray import convertArray
from printData import printGrades


menuItems = np.array(["Load new data", "Check for data errors", "Generate plots", "Display list of grades", "Quit\n"])
isDataLoaded = False
isRunning = True
data = np.array([])

while isRunning:

    choice = displayMenu(menuItems)

    # ------------------------------------------------------------------
    # Load Data
    if choice == 1:

        data = dataLoad(input("Please enter the name of the file, including file extension (.csv): "))
        if len(data) > 0: isDataLoaded = True
        else: isDataLoaded = False
    # ------------------------------------------------------------------
    # Check data for errors
    elif choice == 2:

        if isDataLoaded:

            checkError(data)
        else:

            print("Please Load new data first!\n")
    # ------------------------------------------------------------------
    # Generate Plots
    elif choice == 3:

        if isDataLoaded:

            print("todo: implement")
        else:

            print("Please Load new data first!\n")
    # ------------------------------------------------------------------
    # Display Grades
    elif choice == 4:

        if isDataLoaded:

            printGrades(computeFinalGrades(convertArray(data)), data)
        else:

            print("Please Load new data first!\n")
    # ------------------------------------------------------------------
    # Quit
    elif choice == 5:

        isRunning = False
