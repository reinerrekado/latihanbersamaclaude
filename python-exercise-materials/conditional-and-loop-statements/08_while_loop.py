"""
DEMO 7: while Loop
=============================================================
Unlike `for`, `while` doesn't loop over a fixed collection - it
keeps looping as long as a CONDITION stays True.
"""

# -------------------------------------------------
# 1. Basic while loop (slide 31)
# -------------------------------------------------
count = 1
while count <= 3:
    print(count)
    count += 1   # same as: count = count + 1

print("Loop finished, final count =", count)   # prints 4 (the value that made the condition False)

print("=" * 40)

# -------------------------------------------------
# 2. Buying chocolate example (slide 32)
# -------------------------------------------------
money = 10

while money > 0:              # <- evaluate the condition
    print("Buying $1 Chocolate...")
    money = money - 1         # <- decrease money so the loop CAN eventually stop

print("Out of money!")

# -------------------------------------------------
# Ask students BEFORE running:
# 1. What is the stopping condition here?          -> money > 0 becomes False
# 2. What happens if we forget `money = money - 1`? -> infinite loop!
#    (see 09_infinite_loop_LIVE_DEMO.py for a live example of this)
# -------------------------------------------------
