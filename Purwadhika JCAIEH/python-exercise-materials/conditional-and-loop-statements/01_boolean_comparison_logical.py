"""
DEMO 1: Review - Boolean, Comparison, and Logical Operators
=============================================================
Goal: refresh students' memory before diving into if/else and loops,
since conditions are built from these operators.
"""

x = 5

# -------------------------------------------------
# 1. Comparison Operators -> always return a Boolean (True/False)
# -------------------------------------------------
print("x =", x)
print("x == 5  :", x == 5)   # equal to
print("x == 8  :", x == 8)
print("x != 8  :", x != 8)   # not equal
print("x > 8   :", x > 8)    # greater than
print("x < 8   :", x < 8)    # less than
print("x >= 5  :", x >= 5)   # greater than or equal to
print("x <= 5  :", x <= 5)   # less than or equal to

# NOTE: in Python, == compares VALUE. "5" (string) is NOT the same as 5 (int)
print('x == "5":', x == "5")  # False, int 5 is not the same as string "5"

print("-" * 40)

# -------------------------------------------------
# 2. Logical Operators -> combine multiple Boolean conditions
# -------------------------------------------------
# and -> True only if BOTH conditions are True
print("x > 3 and x < 10 :", x > 3 and x < 10)   # True and True -> True
print("x > 3 and x < 5  :", x > 3 and x < 5)    # True and False -> False

# or -> True if AT LEAST ONE condition is True
print("x < 3 or x == 5  :", x < 3 or x == 5)    # False or True -> True
print("x < 3 or x == 8  :", x < 3 or x == 8)    # False or False -> False

# not -> reverses a Boolean value
print("not (x > 5)      :", not (x > 5))        # x > 5 is False, so not False -> True

print("-" * 40)

# -------------------------------------------------
# 3. Why this matters: Booleans decide which code runs
# -------------------------------------------------
# This is a preview of the next file (02_conditional_statements.py).
# The condition below is just a Boolean expression, same as the ones above.
is_eligible = x >= 17
print("is_eligible :", is_eligible)

if is_eligible:
    print("This block runs because is_eligible is True")
else:
    print("This block runs because is_eligible is False")
