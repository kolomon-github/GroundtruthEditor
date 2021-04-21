"""
Remove Confidence Interval

"""
import pandas as pd
import numpy as np

# Takes a csv name, writes the csv to the directory
def filterConfidenceInterval(df):
    def filterRatingInput(someInput):
        temp = ""

        for i in someInput:
            if i in "0123456789":
                temp += i

        if "." in someInput:
            return -1
            
        elif int(temp) > -1:
            return int(temp)
        else:
            return -1

    confRating = -1
    cont2 = False

    while cont2 == False:
        confRating = str(input("Enter some confidence minimum (i.e 80%): "))

        if 101 > filterRatingInput(confRating) > -1:
            cont2 = True

    intervalClean = filterRatingInput(confRating)/100
    
    dfFinal = df[df[7] >= intervalClean]

    print("")
    print(str(len(df) - len(dfFinal)) + " items were removed")
    print("")

    return dfFinal
