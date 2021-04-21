"""
Make All Tracks Single Frame (Reset TrackID)

"""
import pandas as pd
import numpy as np

# Takes a csv name, writes the csv to the directory 
def makeAllTracksSingleFrame(df):
    a = np.arange(1, len(df)+1)
    
    df[0] = a

    return df
