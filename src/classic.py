# classic.py
# Solomon Himelbloom
# 2022-02-26
#
# For CS 405 Spring 2022

# TODO:
# - Dataset function to generate a random number guess
# - Add image processing functions
# - Connection to the data pipeline
# - GUI via website user interface
# - Utilize notebook for data analysis

import random
# import numpy as np
import pandas as pd


def read_data(filename):
    """Read the data file and return a pandas dataframe."""
    df = pd.read_csv(filename, header=None, names=date_processing())
    return df


def random_guess():
    """Pick a random day as a starting point for the data set."""
    lower_bound, upper_bound = 104.0146, 141.4868
    random_day = random.randrange(int(lower_bound), int(upper_bound))
    print("Random Guess: " + str(random_day))


def date_processing():
    """Process the existing date data."""
    header = "Year,Decimal Day of Year,Month,Day,Time"
    header = header.split(",")
    return header


# Main program
if __name__ == "__main__":
    print("UAF CS 405: Nenana Ice Classic")
    # read_data("data/NenanaIceClassic_1917-2021.csv")
    print(date_processing())
    random_guess()
