"""
DEMO 9: Pandas DataFrame - Missing Values and groupby()
=============================================================
Goal: find and handle NaN (missing) values, then summarize a
DataFrame by category using groupby().
"""

import numpy as np
import pandas as pd

# -------------------------------------------------
# 1. Spotting missing values
# -------------------------------------------------
df = pd.DataFrame({
    "A": [1, 2, np.nan],
    "B": [5, np.nan, np.nan],
    "C": [1, 2, 3],
})
print(df)

print("df.isna():\n", df.isna())
print("df.isna().sum() (missing count per column):\n", df.isna().sum())

print("-" * 40)

# -------------------------------------------------
# 2. dropna() - remove rows/columns that have missing values
# -------------------------------------------------
print("df.dropna() (default axis=0, drops any ROW with a NaN):\n", df.dropna())
print("df.dropna(axis=1) (drops any COLUMN with a NaN):\n", df.dropna(axis=1))
print("df.dropna(thresh=2) (keep rows with at least 2 real values):\n", df.dropna(thresh=2))

print("-" * 40)

# -------------------------------------------------
# 3. fillna() - replace missing values instead of dropping them
# -------------------------------------------------
print("df.fillna(value='FILL VALUE'):\n", df.fillna(value="FILL VALUE"))
print("filling column A with its own mean:\n", df["A"].fillna(value=df["A"].mean()))
# still not in place - df itself is unchanged unless you reassign it
# or pass inplace=True

print("-" * 40)

# -------------------------------------------------
# 4. groupby() - split into groups, then aggregate each group
# -------------------------------------------------
sales_df = pd.DataFrame({
    "Company": ["GOOG", "GOOG", "MSFT", "MSFT", "FB", "FB"],
    "Person": ["Sam", "Charlie", "Amy", "Vanessa", "Carl", "Sarah"],
    "Sales": [200, 120, 340, 124, 243, 350],
})
print(sales_df)

by_company = sales_df.groupby("Company")
print("by_company.mean(numeric_only=True):\n", by_company.mean(numeric_only=True))
print("by_company.sum(numeric_only=True):\n", by_company.sum(numeric_only=True))
print("by_company['Sales'].describe():\n", by_company["Sales"].describe())

# .agg() runs several statistics at once
print("count + mean together:\n", sales_df.groupby("Company")["Sales"].agg(["count", "mean"]))
