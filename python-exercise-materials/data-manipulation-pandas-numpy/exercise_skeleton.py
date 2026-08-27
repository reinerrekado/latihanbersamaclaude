"""
EXERCISE SKELETON - Pandas & NumPy Data Manipulation
=============================================================
6 exercises: 2 with NumPy, 4 with Pandas (using titanic_sample.csv,
which sits next to this file - read it with a relative path like
pd.read_csv("titanic_sample.csv")).

Figure out the approach yourself before checking the demo files.
At the bottom, uncomment ONE exercise call at a time to test it.
"""

import numpy as np
import pandas as pd


# =================================================================
# EXERCISE 1: Bordered Grid
# =================================================================
# Build a 10x10 2D array. The outer ring (first/last row, first/last
# column) should all be 4. Everything inside the ring should be 0.
def border_array():
    pass


# =================================================================
# EXERCISE 2: Random Matrix, Rows Reversed
# =================================================================
# Ask the user for three things: how many numbers to generate, and
# the low/high bounds for a random integer range. Generate a 1D
# array of that many random integers, reshape it into a 2D matrix,
# then reverse the order of values WITHIN each row.
#   e.g. a row [1, 2, 3] becomes [3, 2, 1]
# Pick a row count that evenly divides the total - or figure out a
# way to reshape that doesn't require you to know it in advance.
def random_matrix_reverse():
    pass


# =================================================================
# EXERCISE 3: Surviving Passengers
# =================================================================
# From titanic_sample.csv, show only the passengers who were female
# AND survived.
def filter_female_survivors():
    pass


# =================================================================
# EXERCISE 4: Fare by Age Group
# =================================================================
# Add a column that labels each passenger "Child" if their Age is
# under 18, otherwise "Adult". Then show the average Fare paid by
# each of those two groups.
def age_group_avg_fare():
    pass


# =================================================================
# EXERCISE 5: Class Summary
# =================================================================
# For each passenger class (Pclass), show how many passengers are
# in it and the average Fare they paid.
def class_summary():
    pass


# =================================================================
# EXERCISE 6: Survival Rate by Class and Gender
# =================================================================
# For every combination of Pclass and Sex, find the average survival
# rate. Show the results ordered from highest survival rate to
# lowest.
def survival_by_class_and_gender():
    pass


# =================================================================
# Uncomment ONE line at a time to test each exercise
# =================================================================
if __name__ == "__main__":
    border_array()
    # random_matrix_reverse()
    # filter_female_survivors()
    # age_group_avg_fare()
    # class_summary()
    # survival_by_class_and_gender()
