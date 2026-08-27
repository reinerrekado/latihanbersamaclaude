"""
LIVE DEMO: Infinite Loop
=============================================================
INSTRUCTOR NOTES (read before class):

WARNING: running this file will loop FOREVER. That's the point.

HOW TO RUN THIS DEMO LIVE:
1. Run this file:  python 09_infinite_loop_LIVE_DEMO.py
2. Let it print for a few seconds so students SEE it never stops
   and never reaches "Done buying chocolate!" at the bottom.
3. Press CTRL + C in the terminal to interrupt it.
   -> Python raises a KeyboardInterrupt and the program stops.
4. Ask: "why did this never stop?" then scroll down to the BUG comment.
5. Fix it live by uncommenting the `money = money - 1` line, save, and
   run again to show it terminating normally this time.
"""

import time

money = 10

while money > 0:
    print("Buying $1 Chocolate... (money is still", money, ")")
    time.sleep(0.3)   # slows the loop down so students can actually watch it run

    # BUG: we never decrease `money`, so `money > 0` is ALWAYS True.
    # This is the #1 cause of infinite loops for beginners: the
    # variable used in the while condition never changes inside the loop.
    #
    # THE FIX (uncomment this line):
    money = money - 1

print("Done buying chocolate!")   # this line will NEVER be reached as-is
