"""
calculator.py - the "GOOD" version: uses the
if __name__ == "__main__" guard.

__name__ is a special variable Python sets automatically:
  - it equals "__main__"        when this file is run directly
  - it equals "calculator"      when this file is imported
So the block below only runs when we execute this file directly,
NOT when another file imports it.
"""

def add(a, b):
    return a + b

# print('__name__ variable inside calculator.py', __name__)
if __name__ == "__main__":
    result = add(1, 2)
    print("(inside calculator.py) result =", result)   # Output: 3
