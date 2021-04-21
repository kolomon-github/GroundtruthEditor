"""
Remove Duplicate Frames

"""
import pandas as pd
import numpy as np


# Takes a csv name, writes the csv to the directory 
def removeDuplicatesFrames(df):
    pixelDif = 20  # TOGGLE

    print("Pixel Difference: The bounds that specify how close two boxes need to be before one is removed " +
          "(large numbers are less forgiving).")

    #cont2 = 'n'
    #while cont2 != 'y':
    try:
        pixelDif = int(input("\nEnter a pixel difference (default is 20): "))
            #cont2 = 'y'
    except ValueError:
        pixelDif = 20
        print("\nGoing with default of 20")
            #pass

    print("\n...may take a few minutes\n")

    indexsList = []
    loopString = df[1].values
    
    for frame in loopString:
        tempList = []
        for i, row in df[df[1] == frame].iterrows():
            tempList.append((i, row[3], row[4], row[5], row[6]))
        
        for l in tempList:
            for m in tempList:
                if l != m:
                    if (abs(m[1] - l[1]) < pixelDif) and (abs(m[2] - l[2]) < pixelDif) and (abs(m[3] - l[3]) < pixelDif) and (abs(m[4] - l[4])< pixelDif):
                        if (l[0] not in indexsList) and (m[0] not in indexsList):
                            indexsList.append(l[0])

    objectList = []

    for k in indexsList:
        objectList.append(df.index[k])
        
    df2 = df.drop(objectList)

    print(str(len(indexsList)) + " items were removed\n")

    return df2

