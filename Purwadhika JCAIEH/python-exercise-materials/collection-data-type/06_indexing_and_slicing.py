"""
DEMO 6: Indexing and Slicing in List and Tuple
=============================================================
Goal: access a single element (indexing) or a portion
(slicing) of a list or tuple - the same rules apply to both.
"""

students = ["andi", "budi", "cinta", "doni"]
coordinate = (-6.2, 106.8)

# -------------------------------------------------
# 1. Indexing -> one element at a time
# -------------------------------------------------
# list_or_tuple[index]
nama = students[0]
print("students[0]:", nama)  # "andi"

longitude = coordinate[1]
print("coordinate[1]:", longitude)  # 106.8

# Negative index counts from the END
print("students[-1] (last item):", students[-1])  # "doni"

print("-" * 40)

# -------------------------------------------------
# 2. Slicing -> a portion of the list/tuple
# -------------------------------------------------
# list_or_tuple[start:stop:step]
# - start: index to begin at (included)
# - stop:  index to stop BEFORE (excluded)
# - step:  how many items to skip (default 1)

some_students = students[2:]
print("students[2:]   :", some_students)  # ["cinta", "doni"]

some_students = students[:2]
print("students[:2]   :", some_students)  # ["andi", "budi"]

some_students = students[0:3:2]
print("students[0:3:2]:", some_students)  # ["andi", "cinta"]

location = coordinate[:]
print("coordinate[:]  :", location)  # (-6.2, 106.8) - a full copy

print("-" * 40)

# -------------------------------------------------
# 3. Common gotcha: indexing out of range vs slicing out of range
# -------------------------------------------------
try:
    print(students[10])
except IndexError as e:
    print("Error:", e)  # indexing a position that doesn't exist crashes

print("students[10:]:", students[10:])  # [] - slicing out of range just returns empty
