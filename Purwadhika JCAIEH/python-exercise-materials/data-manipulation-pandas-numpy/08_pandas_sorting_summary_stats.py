"""
DEMO 8: Pandas DataFrame - Sorting and Summary Statistics
=============================================================
Goal: order rows with sort_values/sort_index, and get quick
statistics about a DataFrame's columns.
"""

import pandas as pd

df = pd.DataFrame({
    "name": ["Raven Bierman", "Valter Havers", "Marko Mendell", "Takahiro Momota", "Yahiko Tilemans", "Dina Rebaine"],
    "gender": ["Female", "Male", "Male", "Male", "Male", "Female"],
    "hire_date": ["2016-12-04", "2018-04-13", "2018-07-04", "2016-11-18", "2017-05-26", "2015-03-20"],
    "gross_salary": [7000000, 7000000, 15000000, 12000000, 20000000, 15000000],
}, index=[100111, 100112, 200210, 200211, 200312, 300207])
print(df)

print("-" * 40)

# -------------------------------------------------
# 1. sort_values - order by a column's values
# -------------------------------------------------
print("sort_values('name'):\n", df.sort_values("name"))
print("sort_values('name', ascending=False):\n", df.sort_values("name", ascending=False))
# not in place by default - use inplace=True to overwrite df itself

print("sort by two columns (gender first, then name):\n",
      df.sort_values(by=["gender", "name"]))

print("-" * 40)

# -------------------------------------------------
# 2. sort_index - order by the row labels instead
# -------------------------------------------------
print("sort_index():\n", df.sort_index())

print("-" * 40)

# -------------------------------------------------
# 3. Quick-look methods
# -------------------------------------------------
print("df.info():")
df.info()

print("\ndf.describe() - numeric columns only:\n", df.describe())

print("\ndf['gross_salary'].mean():", df["gross_salary"].mean())
print("df['gross_salary'].median():", df["gross_salary"].median())
print("df['gross_salary'].std():", df["gross_salary"].std())

print("\ndf['gender'].unique():", df["gender"].unique())
print("df['gender'].nunique():", df["gender"].nunique())
print("df['gender'].value_counts():\n", df["gender"].value_counts())
