"""
DEMO 6: Pandas DataFrame - Selection and Indexing
=============================================================
Goal: pull data out of a DataFrame by column, by label (.loc),
by position (.iloc), and by condition (boolean filtering).
"""

import numpy as np
import pandas as pd

np.random.seed(101)
df = pd.DataFrame(np.random.randn(5, 4), index="A B C D E".split(), columns="W X Y Z".split())
print(df)

print("-" * 40)

# -------------------------------------------------
# 1. Selecting a column -> returns a Series
# -------------------------------------------------
print("df['W']:\n", df["W"])
print("type(df['W']):", type(df["W"]))

print("df[['W', 'Z']] (multiple columns -> DataFrame):\n", df[["W", "Z"]])
# df.W also works (attribute access) but is NOT recommended - it
# breaks if the column name matches a DataFrame method, e.g. df.count

print("-" * 40)

# -------------------------------------------------
# 2. .loc - select by LABEL
# -------------------------------------------------
print("df.loc['A'] (row A as a Series):\n", df.loc["A"])
print("df.loc['B', 'Y'] (single cell):", df.loc["B", "Y"])
print("df.loc['A':'C'] (label slice - end IS included):\n", df.loc["A":"C"])
print("df.loc[['A', 'C'], ['W', 'Y']] (subset of rows and columns):\n",
      df.loc[["A", "C"], ["W", "Y"]])

print("-" * 40)

# -------------------------------------------------
# 3. .iloc - select by integer POSITION (like a plain list/array)
# -------------------------------------------------
print("df.iloc[0] (first row):\n", df.iloc[0])
print("df.iloc[0:3] (position slice - end is EXCLUDED):\n", df.iloc[0:3])
print("df.iloc[0:4:2] (every other row):\n", df.iloc[0:4:2])

print("-" * 40)

# -------------------------------------------------
# 4. Conditional (boolean) selection
# -------------------------------------------------
print("df > 0 (boolean mask):\n", df > 0)
print("df[df > 0] (matches keep value, others become NaN):\n", df[df > 0])

print("df[df['W'] > 0] (keep ROWS where W is positive):\n", df[df["W"] > 0])
print("df[df['W'] > 0]['Y'] (chain to pull one column from the filtered rows):\n",
      df[df["W"] > 0]["Y"])

# combining conditions needs & / | (not 'and'/'or') and each side in ()
print("df[(df['W'] > 0) & (df['Y'] > 0)]:\n", df[(df["W"] > 0) & (df["Y"] > 0)])
