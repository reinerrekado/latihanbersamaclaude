"""
DEMO 5: Pandas DataFrame - Creation
=============================================================
Goal: meet the DataFrame - a 2D table made of Series that all
share the same index - and see the different ways to build one.
"""

import numpy as np
import pandas as pd

# -------------------------------------------------
# 1. A DataFrame is a bunch of Series sharing one index
# -------------------------------------------------
np.random.seed(101)
df = pd.DataFrame(np.random.randn(5, 4), index="A B C D E".split(), columns="W X Y Z".split())
print(df)
# Each COLUMN (W, X, Y, Z) is its own Series. They all share the
# same row index (A, B, C, D, E), which is what makes it a table.

print("-" * 40)

# -------------------------------------------------
# 2. From a dictionary - the most common way in real code
# -------------------------------------------------
# dict keys become column names, each value list becomes a column
my_dict = {
    "a": [1, 2, 3, 4],
    "b": [5, 6, 7, 8],
    "c": [9, 10, 11, 12],
}
df_dict = pd.DataFrame(my_dict, index="w x y z".split())
print(df_dict)

print("-" * 40)

# -------------------------------------------------
# 3. From plain lists
# -------------------------------------------------
a = [i for i in range(1, 5)]
b = [i for i in range(5, 9)]
c = [i for i in range(9, 13)]

# each inner list becomes a ROW when zipped together first
df_list = pd.DataFrame(data=list(zip(a, b, c)), index="w x y z".split(), columns="a b c".split())
print(df_list)

print("-" * 40)

# -------------------------------------------------
# 4. Quick exploration methods every DataFrame has
# -------------------------------------------------
print("df.shape:", df.shape)          # (rows, columns)
print("df.columns:", list(df.columns))
print("df.index:", list(df.index))
print("df.dtypes:\n", df.dtypes)
print("df.head(3):\n", df.head(3))    # first 3 rows
print("df.tail(2):\n", df.tail(2))    # last 2 rows
