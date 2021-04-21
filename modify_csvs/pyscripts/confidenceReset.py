"""
Confidence Reset (Reset to 1)

"""
import pandas as pd
import numpy as np


# Takes a csv name, writes the csv to the directory
def confidenceReset(df):
    a = np.ones(len(df))

    df[7] = a

    return df
