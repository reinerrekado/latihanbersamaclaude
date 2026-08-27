"""
LIVE DEMO: IndentationError
=============================================================
INSTRUCTOR NOTES (read before class):

Python decides which lines belong to a block (if, for, while, etc.)
purely by INDENTATION (spaces at the start of a line) - not by
brackets {} like other languages. Get the indentation wrong and
Python refuses to even run the file.

HOW TO RUN THIS DEMO LIVE:
1. Run this file as-is:  python 03_indentation_error_LIVE_DEMO.py
   -> Python will crash immediately with an IndentationError.
      It won't even print "Start of program!" because Python checks
      indentation BEFORE running any code (during parsing).
2. Point at the error message with students:
   "IndentationError: expected an indented block after 'if' statement on line ..."
3. Fix it live: indent the line under `if` with 4 spaces, save, run again.
4. Optional: show the SECOND common mistake below (inconsistent indentation)
   by commenting out Mistake #1 and uncommenting Mistake #2.
"""

print("Start of program!")

user_age = 20

# ============================================================
# MISTAKE #1 (active): missing indentation
# This is the most common beginner mistake - forgetting to indent
# the line(s) that belong inside the if block.
# ============================================================
# if user_age >= 17:
#    print("You are eligible to sign up!")   # <-- BUG: not indented!

# print("Have a nice day!")


# ============================================================
# THE FIX for Mistake #1 (uncomment to show the corrected version):
# ============================================================
# if user_age >= 17:
#     print("You are eligible to sign up!")   # <-- now indented with 4 spaces
# print("Have a nice day!")


# ============================================================
# MISTAKE #2 (optional, comment out Mistake #1 above to try this instead):
# Inconsistent indentation - mixing different indent widths for lines
# that are supposed to be in the SAME block.
# ============================================================
if user_age >= 17:
   print("You are eligible to sign up!")
   print("Check your email!")   # <-- BUG: indented MORE than the line above
#
# Error you'll see: "IndentationError: unexpected indent"
#
# THE FIX: every line in the same block must use the EXACT same
# number of spaces. Most editors (VS Code included) auto-insert
# 4 spaces per Tab press - stick to that consistently.
