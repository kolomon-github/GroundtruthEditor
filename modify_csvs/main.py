
'''see readMe.txt'''

import time
import calendar
#import sys
#sys.path.append('/python_scripts')

# custom scripts
from pyscripts.removeDuplicatesFrames import removeDuplicatesFrames
from pyscripts.makeAllTracksSingleFrame import makeAllTracksSingleFrame
from pyscripts.removeSomeLabel import removeSomeLabel
from pyscripts.filterConfidenceInterval import filterConfidenceInterval
from pyscripts.confidenceReset import confidenceReset

# helper functions
from pyscripts.helperFunctions import getDf, getChoice, youShallPass, modifyCsv


# -----------------------------------------------------------------------------------------------------
# Mainloop
# ------------------------------------------------------------------------------------------------------
bigCont = False
newDf = 1
df = None
dfName = None

while bigCont == False:
    # 1. Should we get a new df?
    if newDf == 1:
        df, dfName = getDf()

    # 2. Lay out the choices
    choice = getChoice()

    # 3. Execute a choice
    if choice == "1":
        df = modifyCsv(removeDuplicatesFrames, df)
    elif choice == "2":
        df = modifyCsv(removeSomeLabel, df)
    elif choice == "3":
        df = modifyCsv(filterConfidenceInterval, df)
    elif choice == "4":
        df = modifyCsv(makeAllTracksSingleFrame, df)
        print("Great!\n")
    elif choice == "5":
        df = modifyCsv(makeAllTracksSingleFrame, df)
        df = confidenceReset(df)
        print("Great!\n")
    else:
        pass

    # continue? -----------------------------------------------------------------------------------
    same_df_cont = youShallPass("Would you like to keep editing this csv (y/n)?: ")

    if same_df_cont == 'y':
        newDf = 0

    else:
        # 4. write csv
        ts = calendar.timegm(time.gmtime())
        outputName = "{}_{}.csv".format(dfName[:-4], ts)
        df.to_csv(outputName, header=False, index=False)

        # continue?? -----------------------------------------------------------------------------------
        new_df_cont = youShallPass("\nWould you like to edit another csv (y/n)?: ")

        if new_df_cont == 'y':
            newDf = 1
            print("")
        else:
            print("\nThanks for using!\n")
            newDf = 0
            bigCont = True