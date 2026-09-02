"""
DEMO 9 (BONUS / OPTIONAL): else in a Loop
=============================================================
INSTRUCTOR NOTE: this is genuinely unintuitive and rarely used in
real code. If you're short on time, feel free to SKIP this file
entirely - it's not essential to understanding loops. Mention it
only exists briefly, or cover it only if students ask.

THE KEY IDEA (this is NOT the same as if-else!):
The `else` block after a loop runs ONLY when the loop finishes
NORMALLY (the while/for condition became False on its own) - and
is SKIPPED if the loop was stopped early by `break`.

  while condition:      for item in items:
      ...                   ...
      break  (maybe)        break  (maybe)
  else:                 else:
      # runs only if       # runs only if
      # break NEVER ran    # break NEVER ran
"""

# -------------------------------------------------
# Password attempt example (slide 35)
# -------------------------------------------------
attempt = 0

while attempt < 3:
    password = input("Password: ")

    if password == "python":
        print("Authenticated!")
        break                     # loop stops early -> else block is SKIPPED
    else:
        print("Wrong password!")
        attempt += 1
else:
    # this only runs if the while loop ended because `attempt < 3`
    # became False - meaning the user NEVER guessed correctly
    print("Maximum attempts reached! Account locked!")

print("Program finished.")

# -------------------------------------------------
# Simple mental model for students:
# "else on a loop" basically means "if we never broke out early"
# It has nothing to do with the if/else inside the loop body -
# those are two completely separate `else` keywords doing different jobs.
# -------------------------------------------------
