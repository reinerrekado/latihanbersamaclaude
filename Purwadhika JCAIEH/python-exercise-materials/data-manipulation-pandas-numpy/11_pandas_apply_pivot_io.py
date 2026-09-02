"""
DEMO 11: Pandas DataFrame - apply(), Pivot Tables, and File I/O
=============================================================
Goal: transform column values with .apply()/lambda, reshape a
DataFrame with pivot_table(), and read/write CSV files.

Running this file creates demo_export.csv in this folder - that's
expected, it's just this demo's output (see .gitignore).
"""

import pandas as pd

# -------------------------------------------------
# 1. Arithmetic directly between columns
# -------------------------------------------------
df = pd.DataFrame({"col1": [1, 2, 3, 4], "col2": [444, 555, 666, 444], "col3": ["abc", "def", "ghi", "xyz"]})
print(df)

df["col4"] = df["col1"] + df["col2"]
df["col5"] = df["col2"] / df["col1"]
print("with derived columns:\n", df)

print("-" * 40)

# -------------------------------------------------
# 2. .apply() - run a function on every value in a column
# -------------------------------------------------
def times2(x):
    return x * 2

print("df['col1'].apply(times2):\n", df["col1"].apply(times2))
print("df['col3'].apply(len) (works on strings too):\n", df["col3"].apply(len))

print("-" * 40)

# -------------------------------------------------
# 3. Same thing with a lambda - handy for short, one-off logic
# -------------------------------------------------
print("df['col1'].apply(lambda x: x * 2):\n", df["col1"].apply(lambda x: x * 2))
print("df['col3'].apply(lambda x: x.upper()):\n", df["col3"].apply(lambda x: x.upper()))

print("-" * 40)

# -------------------------------------------------
# 4. Pivot table - summarize by turning row values into columns
# -------------------------------------------------
sales = pd.DataFrame({
    "Region": ["West", "West", "West", "East", "East", "East"],
    "Size": ["Small", "Small", "Large", "Large", "Small", "Small"],
    "Channel": ["Online", "Store", "Online", "Store", "Online", "Store"],
    "Revenue": [120, 90, 300, 250, 80, 60],
})
print(sales)

print("\npivot_table(values='Revenue', index=['Region','Size'], columns='Channel'):\n",
      sales.pivot_table(values="Revenue", index=["Region", "Size"], columns="Channel"))

print("-" * 40)

# -------------------------------------------------
# 5. Reading and writing files
# -------------------------------------------------
df.to_csv("demo_export.csv", index=False)
print("wrote demo_export.csv")

reloaded = pd.read_csv("demo_export.csv")
print("read back from disk:\n", reloaded)
# index=False on export keeps pandas from writing an extra "0,1,2.."
# column - without it, read_csv would bring that column back as data
