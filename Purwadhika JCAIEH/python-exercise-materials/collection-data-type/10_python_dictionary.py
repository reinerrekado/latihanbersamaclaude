"""
DEMO 10: Python Dictionary - Creating Dictionaries
=============================================================
Goal: see why a dictionary (key-value pairs) beats a list when
you need to look something up quickly, like finding a
student's name from their ID.
"""

# -------------------------------------------------
# 1. The problem: hard to look up a name by ID with a list
# -------------------------------------------------
student_names = ["andi", "budi", "citra"]
print("Which one is UG10217002?", student_names)  # no way to tell just from the list!

print("-" * 40)

# -------------------------------------------------
# 2. The solution: a dictionary maps each key to a value
# -------------------------------------------------
students_by_id = {"UG10217092": "andi", "UG10217002": "budi", "G10217009": "citra"}
print("students_by_id:", students_by_id)
print("type(students_by_id):", type(students_by_id))

# Look up a value directly by its key - no searching needed!
print("students_by_id['UG10217002']:", students_by_id["UG10217002"])  # "budi"

print("-" * 40)

# -------------------------------------------------
# 3. Keys must be unique, but VALUES can repeat
# -------------------------------------------------
more_students = {"a1": "andi", "a2": "andi", "a3": "budi"}
print("more_students (duplicate values are fine):", more_students)
# Two students named "andi" is fine - but you could never have two "a1" keys

print("-" * 40)

# -------------------------------------------------
# 4. Empty dictionaries - two equivalent ways to write one
# -------------------------------------------------
empty_dict_a = dict()
empty_dict_b = {}
print("empty_dict_a:", empty_dict_a)
print("empty_dict_b:", empty_dict_b)

print("-" * 40)

# -------------------------------------------------
# 5. A dictionary value can be ANY type - even a list or another dict
# -------------------------------------------------
sample = {
    "text": "hello",
    "num": 3.14,
    "flag": True,
    "list": [1, 2],
    "dict": {"x": 10},
}
print("sample:", sample)
print("sample['list']:", sample["list"])
print("sample['dict']['x']:", sample["dict"]["x"])
