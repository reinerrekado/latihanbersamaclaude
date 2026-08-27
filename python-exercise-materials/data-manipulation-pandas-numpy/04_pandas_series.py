"""
DEMO 4: Pandas Series
=============================================================
Goal: meet the Series - a 1D array that also carries a label for
each value, and see the different ways to build one.

(Install pandas first if you haven't: pip install pandas)
"""

import numpy as np
import pandas as pd

# -------------------------------------------------
# 1. A Series looks like an array, but has an index label attached
# -------------------------------------------------
arr = np.array([10, 20, 30])
print("plain array:", arr)

series = pd.Series(arr)
print("pandas Series:\n", series)
print("type:", type(series))
# Notice the 0, 1, 2 on the left - that's the index label, not part
# of the data. It defaults to 0, 1, 2... just like list positions.

print("-" * 40)

# -------------------------------------------------
# 2. Creating a Series from a list
# -------------------------------------------------
my_list = [10, 20, 30]
print(pd.Series(data=my_list))

print("-" * 40)

# -------------------------------------------------
# 3. Giving it custom labels instead of 0, 1, 2
# -------------------------------------------------
labels = ["a", "b", "c"]
custom_series = pd.Series(data=my_list, index=labels)
print(custom_series)
print("custom_series['b']:", custom_series["b"])  # look up BY LABEL

print("-" * 40)

# -------------------------------------------------
# 4. Creating a Series from a dictionary
# -------------------------------------------------
# pandas uses the dict keys as the index automatically
prices = {"apple": 15000, "banana": 8000, "cherry": 45000}
price_series = pd.Series(prices)
print(price_series)

print("-" * 40)

# -------------------------------------------------
# 5. A Series can hold any object, not just numbers
# -------------------------------------------------
text_series = pd.Series(["andi", "budi", "citra"])
print(text_series)
print("text_series.dtype:", text_series.dtype)  # 'object' for strings
