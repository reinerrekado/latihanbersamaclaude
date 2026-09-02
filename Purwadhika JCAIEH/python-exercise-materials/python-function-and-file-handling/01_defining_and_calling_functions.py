"""
DEMO 1: Defining and Calling Functions
=============================================================
Goal: see why we bundle repeated logic into a function, then learn
def, calling, parameters/arguments, and default values.
"""

# -------------------------------------------------
# 1. A function is a block of code that performs a specific task
# -------------------------------------------------
def greet():
    print("Hello world!")

# Defining it doesn't run it - we still have to CALL it
greet()
print("This is outside the function.")

print("-" * 40)

# -------------------------------------------------
# 2. Parameter vs argument
# -------------------------------------------------
# "name" below is a PARAMETER - a placeholder defined in the function
def greet_person(name):
    print("Hello", name + "!")

# "Alice" and "Bob" below are ARGUMENTS - the actual values passed in
greet_person("Alice")
greet_person("Bob")

print("-" * 40)

# -------------------------------------------------
# 3. Default parameter values
# -------------------------------------------------
# If no argument is passed, Python uses the default value instead
def greet_with_time(name="Bob", time=None):
    if time:
        print(f"Selamat {time}, {name}!")
    else:
        print(f"Halo, {name}!")

greet_with_time()                   # Halo, Bob!
greet_with_time("Andi")             # Halo, Andi!
greet_with_time(time="pagi")        # Selamat pagi, Bob!
greet_with_time("Andi", "pagi")     # Selamat pagi, Andi!
