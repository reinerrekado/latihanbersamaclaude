"""
DEMO 4: Nested, Callback, and Recursive Functions
=============================================================
Goal: see three special ways functions can relate to each other -
defined inside another function, passed as an argument, and calling
themselves.
"""

# -------------------------------------------------
# 1. Nested function - a helper function defined INSIDE another
# -------------------------------------------------
def calculate_total(prices):
    tax_rate = 0.11

    def add_tax(price):  # only exists while calculate_total() runs
        return price * (1 + tax_rate)

    total = 0
    for price in prices:
        total += add_tax(price)
    return total

print("calculate_total:", round(calculate_total([100, 200]), 2))  # 333.0

try:
    add_tax(100)  # NameError - add_tax doesn't exist out here
except NameError as e:
    print("Error:", e)

print("-" * 40)

# -------------------------------------------------
# 2. Callback function - a function passed as an argument
# -------------------------------------------------
def tambah(a, b):
    return a + b

def kurang(a, b):
    return a - b if a >= b else b - a

def kalkulator(operasi, a, b):  # "operasi" receives a FUNCTION
    return operasi(a, b)        # ...and calls it here

print("kalkulator(tambah, 1, 3):", kalkulator(tambah, 1, 3))   # 4
print("kalkulator(kurang, 1, 2):", kalkulator(kurang, 1, 2))   # 1
print("kalkulator(kurang, 5, 2):", kalkulator(kurang, 5, 2))   # 3

print("-" * 40)

# -------------------------------------------------
# 3. Recursive function - a function that calls itself
# -------------------------------------------------
def countdown(num):
    print(num)
    if num > 1:
        countdown(num - 1)  # calls itself with a smaller number
    # num == 1 is the stopping condition - no more calls after that

countdown(3)  # 3, 2, 1
