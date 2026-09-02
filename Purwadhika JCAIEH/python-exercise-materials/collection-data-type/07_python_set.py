"""
DEMO 7: Python Set - Creating Sets
=============================================================
Goal: see how a set automatically removes duplicates, and why
it has no index (its elements are unordered).
"""

# -------------------------------------------------
# 1. The problem: duplicate registrations in a list
# -------------------------------------------------
registrations = ["andi", "budi", "citra", "andi", "doni", "efraim", "citra"]
print("registrations (list, has duplicates):", registrations)

# -------------------------------------------------
# 2. The solution: convert to a set to keep only unique values
# -------------------------------------------------
unique_registrations = set(registrations)
print("unique_registrations (set):", unique_registrations)
print("type(unique_registrations):", type(unique_registrations))

print("-" * 40)

# -------------------------------------------------
# 3. Sets can also be written directly with {...}
# -------------------------------------------------
attendance = {"andi", "efraim", "cinta", "budi"}
print("attendance:", attendance)

# A set has NO index - elements are unordered
try:
    print(attendance[0])
except TypeError as e:
    print("Error:", e)  # 'set' object is not subscriptable

print("-" * 40)

# -------------------------------------------------
# 4. Empty sets - careful, {} is an empty DICT, not a set!
# -------------------------------------------------
empty_set = set()
print("empty_set:", empty_set, "| type:", type(empty_set))

not_empty_set = {}
print("{} is actually a:", type(not_empty_set))  # dict, not set!

print("-" * 40)

# -------------------------------------------------
# 5. A set can't directly contain another set (sets are unhashable)
#    -> use frozenset() to nest one
# -------------------------------------------------
groups = {
    frozenset({"andi", "budi"}),    # Group A
    frozenset({"cinta", "doni"}),   # Group B
    frozenset({"efraim"}),          # Group C
}
print("groups:", groups)
