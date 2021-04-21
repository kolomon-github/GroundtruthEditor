import pandas as pd
import os

def getDf():
    cont = False

    while cont == False:
        print("---------------------------------------------------------")
        print("Let's edit a CSV!")
        print("")

        csvName = str(input("What is the name of the csv file?: "))

        tempList = os.listdir()

        if csvName in tempList:
            cont = True

            # instantialize
            df = pd.read_csv(csvName, header=None)

            # maybe remove the header
            if df[1][0] == "  2: Video or Image Identifier":
                df.drop([0, 1], inplace=True)
                df[7] = df[7].apply(float)
                print(df.values.shape)

            return df, csvName

        else:
            print("\n...There isn't a file with that name in this directory...\n")


def getChoice():
    cont = False

    while cont == False:
        print("----------------------------------------------------------------")
        print("What would you like to do?")
        print("    1. Remove duplicates")
        print("    2. Remove a label")
        print("    3. Filter a confidence interval")
        print("    4. Make all multi-frame tracks single frame (reset track ID))")
        print("    5. * Automatically process a csv")

        choice = str(input("Enter your choice (1-5): ")).strip()
        print("")

        choices = ["1", "2", "3", "4", "5"]

        if choice in choices:
            cont = True
            return choice
        else:
            print("\n... invalid choice\n")


def youShallPass(somePrompt):  # returns 'y' or 'n'
    temp = "z"

    while (temp != "y") and (temp != "n"):
        try:
            temp = str(input(somePrompt)).strip().lower()
        except ValueError:
            pass

    return temp


def modifyCsv(someFun, df):
    cont_mc = youShallPass("Are you sure (y/n)?: ")
    print("")

    if cont_mc == 'y':
        out = someFun(df)
        return out