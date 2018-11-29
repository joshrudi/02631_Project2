import numpy as np
from dataLoadFunction import dataLoad
from displayMenu import displayMenu


menuItems = np.array(["Load new data", "Check for data errors", "Generate plots", "Display list of grades", "Quit"])
isDataLoaded = False
isRunning = True
data = np.array([])

while isRunning:

    choice = displayMenu(menuItems)

    # ------------------------------------------------------------------
    if choice == 1:
        data = dataLoad(input("Please enter the name of the file including file extension (.csv): "))
        isDataLoaded = True
    # ------------------------------------------------------------------
    elif choice == 2:
        if isDataLoaded:
            print("todo: implement")
        else:
            print("Please Load new data first!")
    # ------------------------------------------------------------------
    elif choice == 3:
        if isDataLoaded:
            print("todo: implement")
        else:
            print("Please Load new data first!")
    # ------------------------------------------------------------------
    elif choice == 4:
        if isDataLoaded:
            print("todo: implement")
        else:
            print("Please Load new data first!")
    # ------------------------------------------------------------------
    elif choice == 5:
        isRunning = False
