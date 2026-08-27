"""
DEMO 5: Python Tuple - Methods and Functions
=============================================================
Goal: since tuples are read-only, we can only ASK questions
about them (index, count, length) - not modify them.
"""

fibonacci_numbers = (1, 1, 2, 3, 5, 8, 13)

print("fibonacci_numbers:", fibonacci_numbers)

# -------------------------------------------------
# 1. .count(value) -> how many times does a value appear?
# -------------------------------------------------
print("fibonacci_numbers.count(1):", fibonacci_numbers.count(1))  # 2

# -------------------------------------------------
# 2. .index(value) -> what is the index of the FIRST match?
# -------------------------------------------------
print("fibonacci_numbers.index(5):", fibonacci_numbers.index(5))  # 4

# -------------------------------------------------
# 3. len() -> how many items are in the tuple?
# -------------------------------------------------
print("len(fibonacci_numbers):", len(fibonacci_numbers))  # 7

print("-" * 40)

# What happens if the value isn't there?
try:
    fibonacci_numbers.index(100)
except ValueError as e:
    print("Error:", e)  # .index() raises an error if the value is missing
