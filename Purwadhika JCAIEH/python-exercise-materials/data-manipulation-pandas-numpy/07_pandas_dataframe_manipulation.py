"""
DEMO 7: Pandas DataFrame - Adding/Removing Rows & Columns, Index
=============================================================
Goal: modify the shape of a DataFrame - add or drop rows/columns,
and reset/replace the index (including a multi-level index).
"""

import numpy as np
import pandas as pd

np.random.seed(101)
df = pd.DataFrame(np.random.randn(5, 4), index="A B C D E".split(), columns="W X Y Z".split())
print(df)

print("-" * 40)

# -------------------------------------------------
# 1. Adding a new column
# -------------------------------------------------
df["new"] = df["W"] + df["Y"]      # arithmetic between existing columns
print("after df['new'] = df['W'] + df['Y']:\n", df)

df.insert(2, "inserted", [1, 2, 3, 4, 5])  # insert at a specific position
print("after .insert(2, 'inserted', ...):\n", df)

print("-" * 40)

# -------------------------------------------------
# 2. Dropping columns / rows - NOT in place unless you say so
# -------------------------------------------------
print("df.drop('new', axis=1) - a NEW DataFrame, original untouched:\n",
      df.drop("new", axis=1))
print("original df still has 'new':\n", "new" in df.columns)

df.drop(["new", "inserted"], axis=1, inplace=True)  # axis=1 -> columns
print("after inplace=True drop:\n", df)

print("df.drop('E', axis=0) - axis=0 drops a ROW:\n", df.drop("E", axis=0))

print("-" * 40)

# -------------------------------------------------
# 3. Adding a new row with .loc
# -------------------------------------------------
df.loc["F"] = [1, 2, 3, 4]
print("after df.loc['F'] = [...]:\n", df)

print("-" * 40)

# -------------------------------------------------
# 4. Resetting and setting the index
# -------------------------------------------------
print("df.reset_index() - old labels become a column, new 0..n index:\n",
      df.reset_index())

df["States"] = "CA NY WY OR CO NV".split()
print("after adding a States column:\n", df)

print("df.set_index('States') - NOT in place by default:\n",
      df.set_index("States"))
print("original df unchanged:\n", df.index.tolist())

print("-" * 40)

# -------------------------------------------------
# 5. Multi-level index
# -------------------------------------------------
outside = ["Jakarta", "Jakarta", "Jakarta", "Surabaya", "Surabaya", "Surabaya"]
inside = [1, 2, 3, 1, 2, 3]
hier_index = pd.MultiIndex.from_tuples(list(zip(outside, inside)))

sales = pd.DataFrame(np.random.randint(1, 100, (6, 2)), index=hier_index, columns=["Restaurant A", "Restaurant B"])
print("multi-index DataFrame:\n", sales)

print("sales.loc['Jakarta'] (outer level):\n", sales.loc["Jakarta"])
print("sales.loc['Jakarta'].loc[1] (drill into inner level):\n", sales.loc["Jakarta"].loc[1])
print("sales.xs('Jakarta') (same as .loc for the outer level):\n", sales.xs("Jakarta"))
print("sales.xs(2, level=1) (every branch at inner level == 2):\n", sales.xs(2, level=1))
