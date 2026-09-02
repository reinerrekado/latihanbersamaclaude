"""
DEMO 6: enumerate() vs range(len(...))
=============================================================
Students often ask: "why not just use range(len(list)) and index
into the list myself?" This file shows both side by side so the
difference is concrete, not abstract.
"""

fruits = ["apple", "banana", "cherry"]

# -------------------------------------------------
# METHOD 1: range(len(list)) + manual indexing
# Works, but it's more to type AND more places to make a mistake
# (e.g. off-by-one errors, forgetting to index the list at all).
# -------------------------------------------------
print("Using range(len(fruits)):")
for i in range(len(fruits)):
    print(f"Index {i} -> {fruits[i]}")   # have to manually index into fruits

print("-" * 40)

# -------------------------------------------------
# METHOD 2: enumerate(list)
# Gives you BOTH the index and the value directly, no manual
# indexing needed, and no risk of an IndexError from a typo.
# -------------------------------------------------
print("Using enumerate(fruits):")
for i, fruit in enumerate(fruits):
    print(f"Index {i} -> {fruit}")

print("-" * 40)

# -------------------------------------------------
# enumerate() also accepts a custom start number
# Handy for "human-friendly" numbering (1st, 2nd, 3rd... instead of 0th)
# -------------------------------------------------
print("Using enumerate(fruits, start=1):")
for position, fruit in enumerate(fruits, start=10):
    print(f"{position}. {fruit}")

print("=" * 40)

# -------------------------------------------------
# RULE OF THUMB for students:
# - Need ONLY the values?              -> for item in list
# - Need the index AND the value?      -> for i, item in enumerate(list)
# - Need ONLY a counter (no list)?     -> for i in range(n)
# range(len(list)) is rarely the best choice - it's a sign you
# probably want enumerate() instead.
# -------------------------------------------------
