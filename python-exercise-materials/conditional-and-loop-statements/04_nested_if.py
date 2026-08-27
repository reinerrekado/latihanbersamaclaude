"""
DEMO 3: Nested if
=============================================================
Use a nested if when the SECOND condition should only be checked
after the FIRST condition is already True (slide 16-17: NIK example).
"""


def validate_nik(nik):
    """Simple stand-in for the slide's validate_NIK() - a real NIK
    is 16 digits. We just check length + digits so the demo runs."""
    result = len(nik) == 16 and nik.isdigit() # True or False

    return result


user_age = int(input("Enter your age: "))

if user_age >= 17:
    nik = input("Enter your NIK (16 digits): ")
    is_nik_valid = validate_nik(nik)
    print(is_nik_valid) # True or False

    # This inner "if" is ONLY reached if user_age >= 17 was True.
    # That's what makes it "nested" - an if statement living inside
    # another if statement's block (notice the DOUBLE indentation).
    if is_nik_valid:
        print("Check your email for the application form!")
    else:
        print("NIK is not valid!")

elif user_age == 16:
    print("You need your parents' permission to sign up!")
else:
    print("You are not eligible to sign up!")

print("Have a nice day!")

# -------------------------------------------------
# Key takeaway for students:
# - Every extra level of nesting = one more level of indentation (4 more spaces)
# - The inner if/else only matters when the outer condition already passed
# - Too much nesting gets hard to read - 2-3 levels is usually the practical limit
# -------------------------------------------------
