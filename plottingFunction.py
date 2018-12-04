# Code by Shiyu Zhou

import numpy as np
import matplotlib.pyplot as plt
from computeFinalGrades import computeFinalGrades

#2-plot function,input is a matrix of grades for each student and each assignment
def GradesPerAssignment(grades):
    #bar plot displaying what amount of each particular grade was received
    x = np.array([-3,0,2,4,7,10,12])
    y = np.array([])
    finalgrades = computeFinalGrades(grades)
    for i in range(np.size(x)):
        y = np.append(y,list(finalgrades).count(x[i]))  
    plt.bar(x,y,width=1,align='center', label = "Number of students who received \n corresponding final grade")
    plt.xticks(x)
    plt.legend(loc="best")
    plt.show()
    #------------------------------------------------------------------------------------------------------------------
    #line plot displaying the average grade for each assignment
    x = np.array(range(1,grades.shape[1]+1))
    y = np.array([])
    for i in range(grades.shape[1]):
        y = np.append(y,np.mean(grades[:,i]))
    plt.plot(x,y, color = "red",label = "The average grade \n for each assignment")
    x=np.array(range(1,grades.shape[1]+1))
    
    #point plot showing all the grades given, plotted row by a row, first row is outside the loop, in order to have just one label in the legend
    plt.plot(x+np.random.uniform(-0.1,0.1,1), grades[0,:]+np.random.uniform(-0.1,0.1,1), "b*",label="Grade points")
    for i in range(1,grades.shape[0]):
       plt.plot(x+np.random.uniform(-0.1,0.1,1), grades[i,:]+np.random.uniform(-0.1,0.1,1), "b*")
    plt.title("GradesPerAssignment")
    plt.xlabel("Assignment number")
    plt.ylabel("Grades")
    plt.xticks(x)
    plt.xlim([0, grades.shape[1]+1])
    plt.ylim([-4,np.amax(grades)+1])
    plt.legend(loc="best")
    plt.show()
