"""
DEMO 10: Pandas DataFrame - merge(), join(), and concat()
=============================================================
Goal: combine two or more DataFrames together, and understand the
difference between inner/outer/left/right joins.
"""

import pandas as pd

# -------------------------------------------------
# 1. pd.merge() - combine on a shared KEY COLUMN (like a SQL join)
# -------------------------------------------------
left = pd.DataFrame({
    "key": ["K0", "K1", "K2", "K3"],
    "A": ["A0", "A1", "A2", "A3"],
    "B": ["B0", "B1", "B2", "B3"],
})
right = pd.DataFrame({
    "key": ["K0", "K1", "K3", "K4"],
    "C": ["C0", "C1", "C2", "C3"],
    "D": ["D0", "D1", "D2", "D3"],
})
print("left:\n", left)
print("right:\n", right)

print("\nhow='inner' (default) - only keys present in BOTH:\n",
      pd.merge(left, right, how="inner", on="key"))

print("\nhow='outer' - every key from both, NaN where missing:\n",
      pd.merge(left, right, how="outer", on="key"))

print("\nhow='left' - every key from left, matching data from right:\n",
      pd.merge(left, right, how="left", on="key"))

print("\nhow='right' - every key from right, matching data from left:\n",
      pd.merge(left, right, how="right", on="key"))

print("-" * 40)

# -------------------------------------------------
# 2. .join() - like merge, but combines on the INDEX instead of a column
# -------------------------------------------------
left2 = pd.DataFrame({"A": ["A0", "A1", "A2", "A3"], "B": ["B0", "B1", "B2", "B3"]}, index=["K0", "K1", "K2", "K3"])
right2 = pd.DataFrame({"C": ["C0", "C1", "C2", "C3"], "D": ["D0", "D1", "D2", "D3"]}, index=["K0", "K1", "K3", "K4"])
print("left2.join(right2, how='outer'):\n", left2.join(right2, how="outer"))

print("-" * 40)

# -------------------------------------------------
# 3. pd.concat() - stack DataFrames without matching on a key
# -------------------------------------------------
df1 = pd.DataFrame({"A": ["A0", "A1"], "B": ["B0", "B1"]})
df2 = pd.DataFrame({"A": ["A2", "A3"], "B": ["B2", "B3"]})

print("axis=0 (default) - stacked on top of each other, more ROWS:\n",
      pd.concat([df1, df2]))
print("axis=0, ignore_index=True (re-numbers the rows):\n",
      pd.concat([df1, df2], ignore_index=True))

print("axis=1 - placed side by side, more COLUMNS:\n",
      pd.concat([df1, df2], axis=1))
