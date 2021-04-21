"""
Remove Some Label

"""
import pandas as pd
import numpy as np

# Takes a csv name, writes the csv to the directory 
def removeSomeLabel(df):
    cont = 'z'

    defaultLabel = "deleteFish"

    #labels = df[9].unique()
    labels = df[9].unique()

    # show the labels
    for i in labels:
        print(i)
    print("")

    cont2 = 'n'
    while cont2 != 'y':
        try:
            defaultLabel = str(input("Enter a label to remove (for example 'YFT' or 'YFT_HEAD' or 'deleteFish'): ")).strip()
            if defaultLabel in labels:
                cont2 = 'y'
            else:
                print("...That 'label' doesn't exist in the CSV")
        except TypeError:
            pass

    print("")

    if defaultLabel in labels:
        #dfFinal = df[df[9] != defaultLabel]
        dfFinal = df[df[9] != defaultLabel]

        print(str(len(df) - len(dfFinal)) + " items were removed")
        print("")

        return dfFinal

    else:
        print("...That 'label' doesn't exist in the CSV\n")
        removeSomeLabel(df)

        print("\nThere isn't a file with that name in this directory...\n")