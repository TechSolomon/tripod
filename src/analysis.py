# analysis.py
# Solomon Himelbloom
# 2022-04-05
#
# For CS 405 Spring 2022

# TODO: Date and time processing (NOAA weather data API).

import random
# import numpy as np
import pandas as pd

def read_data(filename):
    """Read the data file and return a pandas dataframe."""
    df = pd.read_csv(filename, header=None, names=date_processing())
    return df

def date_processing():
    """Return a list of the column names for the dataframe."""
    # return ['Date', 'Time', 'Temp', 'DewPt', 'Pressure', 'WindDir', 'WindSpeed', 'Sky', 'Precip', 'Events']
    return 0
