"""
DEMO 12: Accessing and Updating Values in a Dictionary
=============================================================
Goal: two ways to read a value ([] vs .get()) and how updating
a value works - the same syntax whether you're adding a brand
new key or overwriting an existing one.
"""

student_data = {
    "name": "andi",
    "age": 20,
    "major": "physics",
    "gpa": 3.2,
    "is_graduated": False,
    "courses": ["calculus", "classical mechanics"],
}

# -------------------------------------------------
# 1. Accessing with [] -> fast, but crashes if the key is missing
# -------------------------------------------------
age = student_data["age"]
print("student_data['age']:", age)  # 20

try:
    is_active = student_data["is_active"]
except KeyError as e:
    print("Error:", e)  # KeyError: 'is_active' - key doesn't exist!

print("-" * 40)

# -------------------------------------------------
# 2. Accessing with .get() -> safe, returns a default instead of crashing
# -------------------------------------------------
is_active = student_data.get("is_active", False)
print("student_data.get('is_active', False):", is_active)  # False (the default we gave)

# If no default is given, .get() just returns None
missing = student_data.get("scholarship")
print("student_data.get('scholarship') (no default):", missing)  # None

print("-" * 40)

# -------------------------------------------------
# 3. Updating a value: same syntax as accessing, just assign to it
# -------------------------------------------------
student_data["is_graduated"] = True  # overwrites the existing value
print("after student_data['is_graduated'] = True:", student_data["is_graduated"])

# The SAME syntax also ADDS a new key if it doesn't exist yet
student_data["scholarship"] = "Bright Scholars"
print("after adding a new key:", student_data)
