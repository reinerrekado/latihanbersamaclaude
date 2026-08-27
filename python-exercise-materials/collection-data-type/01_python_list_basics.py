"""
DEMO 1: Python List - Creating Lists
=============================================================
Goal: see why we use a list instead of many separate variables,
and learn the different ways to create one.
"""

# -------------------------------------------------
# 1. The problem: one variable per student doesn't scale
# -------------------------------------------------
student_A = "andi"
student_B = "budi"
student_C = "cinta"
print("Not practical:", student_A, student_B, student_C)
# Imagine doing this for 100 students... 100 variables to manage!

print("-" * 40)

# -------------------------------------------------
# 2. The solution: a list stores multiple values in ONE variable
# -------------------------------------------------
students = ["andi", "budi", "cinta"]
print("students:", students)
print("type(students):", type(students))

# Every item has an index, starting from 0 (NOT 1)
print("students[0]:", students[0])  # "andi"
print("students[1]:", students[1])  # "budi"
print("students[2]:", students[2])  # "cinta"

print("-" * 40)

# -------------------------------------------------
# 3. Empty lists - two equivalent ways to write one
# -------------------------------------------------
empty_list_a = list()
empty_list_b = []
print("empty_list_a:", empty_list_a)
print("empty_list_b:", empty_list_b)
print("empty_list_a == empty_list_b:", empty_list_a == empty_list_b)

print("-" * 40)

# -------------------------------------------------
# 4. A list can hold ANY type, even another list
# -------------------------------------------------
mixed_list = [1, "andi", [2.5, range(10)]]
print("mixed_list:", mixed_list)
print("mixed_list[0]:", mixed_list[0], "->", type(mixed_list[0]))
print("mixed_list[1]:", mixed_list[1], "->", type(mixed_list[1]))
print("mixed_list[2]:", mixed_list[2], "->", type(mixed_list[2]))
# mixed_list[2] is itself a list, so we can index into it again:
print("mixed_list[2][0]:", mixed_list[2][0])  # 2.5
