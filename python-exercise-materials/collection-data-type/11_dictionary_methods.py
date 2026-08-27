"""
DEMO 11: Python Dictionary - Methods and Functions
=============================================================
Goal: the most commonly used dictionary methods for adding,
removing, and retrieving key-value pairs.
"""

student_data = {
    "name": "andi",
    "age": 20,
    "major": "physics",
    "gpa": 3.2,
    "is_graduated": False,
}
print("student_data:", student_data)

# -------------------------------------------------
# 1. Adding / updating items
# -------------------------------------------------
student_data.update({"gpa": 3.5, "is_active": True})  # updates gpa, adds is_active
print("after update(...):", student_data)

student_data.setdefault("minor", "mathematics")  # only adds if key doesn't exist
print("after setdefault('minor', ...):", student_data)

student_data.setdefault("name", "someone else")  # "name" already exists, so no change
print("setdefault on existing key (no change):", student_data["name"])

print("-" * 40)

# -------------------------------------------------
# 2. Retrieving data
# -------------------------------------------------
print("student_data.get('age'):", student_data.get("age"))  # 20
print("student_data.keys()    :", student_data.keys())
print("student_data.values()  :", student_data.values())
print("student_data.items()   :", student_data.items())

print("-" * 40)

# -------------------------------------------------
# 3. Functions
# -------------------------------------------------
print("len(student_data):", len(student_data))         # number of key-value pairs
print("sorted(student_data):", sorted(student_data))    # sorted list of KEYS only

print("-" * 40)

# -------------------------------------------------
# 4. Removing items
# -------------------------------------------------
removed_value = student_data.pop("is_graduated")  # remove by key, get its value back
print("popped value:", removed_value, "| student_data now:", student_data)

last_item = student_data.popitem()  # removes the LAST inserted key-value pair
print("popitem() (last inserted):", last_item, "| student_data now:", student_data)

student_data_backup = student_data.copy()
student_data.clear()
print("student_data after clear():", student_data)
print("student_data_backup (independent copy):", student_data_backup)
