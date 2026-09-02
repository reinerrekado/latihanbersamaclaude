"""
DEMO 2: Conditional Statements - if / if-else / if-elif-else
=============================================================
Follows the same sign-up age example used in the slides (page 11-14).
"""

# -------------------------------------------------
# 1. Plain "if" -> code only runs when the condition is True
#    If it's False, Python just skips the block and moves on.
# -------------------------------------------------
user_age = int(input("Enter your age: "))

if user_age >= 17:
    print("You can send the application form!")
    print("Check your email for the application form!")

print("Have a nice day!")   # this line ALWAYS runs, it's outside the if block
print("=" * 40)


# -------------------------------------------------
# 2. "if-else" -> covers the True case AND the False case
# -------------------------------------------------
user_age = int(input("Enter your age: "))

if user_age >= 17:
    print("You can send the application form!")
else:
    print("You are not eligible to sign up!")

print("Have a nice day!")
print("=" * 40)


# -------------------------------------------------
# 3. "if-elif-else" -> for more than 2 possible outcomes
#    Python checks each condition TOP TO BOTTOM and stops
#    at the FIRST one that is True. The rest are skipped.
# -------------------------------------------------
user_age = int(input("Enter your age: "))

if user_age >= 17:
    print("You can send the application form!")
elif (user_age == 15) or (user_age == 16):
    print("You need your parents' permission to sign up!")
else:
    print("You are not eligible to sign up!")

print("Have a nice day!")
print("=" * 40)


# -------------------------------------------------
# Quick check for students: what does this print if user_age = 20?
# -------------------------------------------------
# if user_age >= 10:
#     print("A")
# elif user_age >= 15:
#     print("B")     # <-- students often expect this to print, but it won't!
# else:
#     print("C")
#
# Answer: "A" -> because the FIRST True condition wins, elif/else after it
# are never checked, even if they would also be True.
