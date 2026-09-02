"""
calculator_no_guard.py - the "BAD" version: top-level code runs
immediately, even when this file is just imported by someone else.
"""

def add(a, b):
    return a + b

# This line is NOT inside any function/guard, so it runs the
# instant this module is imported - not just when run directly.
result = add(1, 2)
print("(inside calculator_no_guard.py) result =", result)   # Output: 3
