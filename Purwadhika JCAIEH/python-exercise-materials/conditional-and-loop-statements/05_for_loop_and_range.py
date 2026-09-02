"""
DEMO 4: for Loop and the range() Function
=============================================================
"""

# -------------------------------------------------
# 1. range(stop) -> sequence starting at 0, stops BEFORE `stop`
# -------------------------------------------------
print("range(10):")
for number in range(10):
    print(number, end=" ")
print()   # just a newline
# Output: 0 1 2 3 4 5 6 7 8 9

print("-" * 40)

# -------------------------------------------------
# 2. range(start, stop) -> sequence starting at `start`
# -------------------------------------------------
print("range(1, 10):")
for number in range(1, 10):
    print(number, end=" ")
print()
# Output: 1 2 3 4 5 6 7 8 9

print("-" * 40)

# -------------------------------------------------
# 3. range(start, stop, step) -> custom increment
# -------------------------------------------------
print("range(1, 10, 2):")
for number in range(1, 10, 2):
    print(number, end=" ")
print()
# Output: 1 3 5 7 9

print("=" * 40)


# -------------------------------------------------
# QUESTION FROM SLIDE 26:
# "After the loop finishes, does the `number` variable still
#  store a value? If so, what is it?"
#
# ANSWER: YES. Python's for loop does NOT create a separate scope.
# The loop variable keeps whatever value it had on its LAST
# iteration. It is NOT deleted or reset after the loop ends.
# -------------------------------------------------
for number in range(10):
    pass   # do nothing, we only care about the final value of `number`

print("After the loop, number =", number)   # prints 9, NOT 10!
# Why 9, not 10? Because range(10) stops BEFORE 10 -> last value used is 9.

print("=" * 40)

# -------------------------------------------------
# Common beginner trap: reusing a loop variable name after the loop
# -------------------------------------------------
for i in range(3):
    print("looping, i =", i)

print("outside the loop, i is still accessible:", i)   # i == 2 here
# This is different from many other languages (like Java/C++) where
# the loop variable only exists INSIDE the loop's {} block.
