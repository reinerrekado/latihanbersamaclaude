"""
DEMO 5: Iterable Data Types
=============================================================
An "iterable" is anything you can loop over with `for ... in ...`.
Slide 24 lists the common ones - here's each one running for real.
"""

# -------------------------------------------------
# String -> iterates character by character
# -------------------------------------------------
print("Looping over a string:")
for char in "Python":
    print(char, end="-")
print()

# -------------------------------------------------
# List -> iterates element by element, in order
# -------------------------------------------------
print("\nLooping over a list:")
fruits = ["Apple", "Banana", "Orange"]
for buah in fruits:
    print(buah, end=" ")
print()

# -------------------------------------------------
# Tuple -> same as list, but the tuple itself can't be changed
# -------------------------------------------------
print("\nLooping over a tuple:")
numbers = (10, 20, 30)
for num in numbers:
    print(num, end=" ")
print()

# -------------------------------------------------
# Dictionary -> by default, looping gives you the KEYS only
# -------------------------------------------------
print("\nLooping over a dictionary (keys only):")
person = {
            "name": "John", 
            "age": 20,
            "weight": 73,
            "height": 173
        }
for key in person:
    print(key, end=" ")
print()

print("Looping over a dictionary's values:")
for value in person.values():
    print(value, end=" ")
print()

print("Looping over a dictionary's key-value pairs:")
for k, v in person.items():
    print(f"{key} -> {value}", end="  ")
print()

# -------------------------------------------------
# Set -> iterates over elements, but order is NOT guaranteed
# -------------------------------------------------
print("\nLooping over a set (order may vary!):")
unique_numbers = {1, 2, 3}
for num in unique_numbers:
    print(num, end=" ")
print()

# -------------------------------------------------
# Range -> a memory-efficient sequence of numbers
# -------------------------------------------------
print("\nLooping over range(5):")
for num in range(5):
    print(num, end=" ")
print()
