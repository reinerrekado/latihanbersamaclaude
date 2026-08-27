"""
EXERCISE SKELETON - Python Collection Data Types
=============================================================
Fill in the TODO sections for each exercise. Each function has:
- A docstring explaining what it should do
- Example inputs/outputs
- A hint
- TODO comments marking where your code goes

At the bottom, uncomment ONE exercise call at a time to test it.
"""


# =================================================================
# EXERCISE 1: Unique Attendance
# =================================================================
# A list of event registrations has duplicate names in it. Print
# the unique attendees as a SORTED list.
#   Example: ["andi", "budi", "andi", "citra"] -> ['andi', 'budi', 'citra']
#
# HINT: set(some_list) removes duplicates. sorted() turns any
#       collection into a sorted list.
def unique_attendance():
    registrations = ["andi", "budi", "citra", "andi", "doni", "efraim", "citra"]

    # TODO: convert registrations to a set to drop duplicates,
    #       then print a SORTED list of the unique names
    pass


# =================================================================
# EXERCISE 2: Student ID Lookup
# =================================================================
# Given a dictionary mapping student IDs to names, ask the user
# for an ID and safely print the matching name - or "not found"
# if the ID doesn't exist. Do NOT let the program crash.
#   Example: id = "UG10217002" -> "budi"
#   Example: id = "XXXXXXXXXX" -> "not found"
#
# HINT: dictionary.get(key, default) never raises a KeyError.
def student_lookup():
    students_by_id = {
        "UG10217092": "andi",
        "UG10217002": "budi",
        "G10217009": "citra",
    }
    student_id = input("Enter a student ID to look up: ")

    # TODO: use .get() to safely print the student's name,
    #       or "not found" if the ID isn't in students_by_id
    pass


# =================================================================
# EXERCISE 3: Filter and Format Fruit Names
# =================================================================
# Using a list comprehension, build a new list containing only the
# fruits with MORE than 4 letters, each one capitalized.
#   Example: "banana" (6 letters) -> "Banana"  (kept, > 4 letters)
#   Example: "fig" (3 letters)    -> excluded  (not > 4 letters)
#
# HINT: "banana".capitalize() -> "Banana". A list comprehension
#       looks like: [expression for item in iterable if condition]
def filter_fruits():
    fruits = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]

    # TODO: build long_fruits using a list comprehension, then print it
    # long_fruits = [... for fruit in fruits if ...]
    pass


# =================================================================
# EXERCISE 4: Course Enrollment Overlap
# =================================================================
# Two sets hold the students enrolled in a Python class and a SQL
# class. Using set operations, print:
#   1. Students enrolled in BOTH classes
#   2. Students enrolled in ONLY ONE of the two classes
#   3. Students enrolled in python_class but NOT sql_class
#
# HINT: intersection() for "both", symmetric_difference() for
#       "only one", difference() for "in A but not B".
def course_enrollment():
    python_class = {"andi", "budi", "citra", "doni"}
    sql_class = {"citra", "doni", "efraim", "fajar"}

    # TODO 1: print students enrolled in BOTH classes
    # TODO 2: print students enrolled in ONLY ONE of the classes
    # TODO 3: print students in python_class but NOT in sql_class
    pass


# =================================================================
# Uncomment ONE line at a time to test each exercise
# =================================================================
if __name__ == "__main__":
    unique_attendance()
    # student_lookup()
    # filter_fruits()
    # course_enrollment()
