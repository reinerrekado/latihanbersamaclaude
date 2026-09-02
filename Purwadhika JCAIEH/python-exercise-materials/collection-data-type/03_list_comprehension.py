"""
DEMO 3: List Comprehension
=============================================================
Goal: a shorter way to build a new list from an existing one -
compare the "long way" (a for loop) with the shorthand.
"""

fruits = ["apple", "banana", "cherry", "date", "elderberry"]

# -------------------------------------------------
# 1. The long way: build a new list with a for loop
# -------------------------------------------------
fruit_with_a = []
for fruit in fruits:
    if "a" in fruit:
        fruit_with_a.append(fruit.upper())

print("without list comprehension:", fruit_with_a)
# Output: ['APPLE', 'BANANA', 'DATE']

print("-" * 40)

# -------------------------------------------------
# 2. The short way: list comprehension
# -------------------------------------------------
# newlist = [expression for item in iterable if condition]
fruit_with_a_v2 = [fruit.upper() for fruit in fruits if "a" in fruit]
print("with list comprehension:   ", fruit_with_a_v2)
# Same result, one line instead of four

print("-" * 40)

# -------------------------------------------------
# 3. Breaking down the syntax
# -------------------------------------------------
#   [ fruit.upper()  for fruit in fruits   if 'a' in fruit ]
#     ^ 3. expression   ^ 1. loop over        ^ 2. filter
#        (what to keep     fruits, storing       (only keep
#         for each item)    each in `fruit`        fruits with 'a')

# More examples:
squares = [n * n for n in range(1, 6)]
print("squares:", squares)  # [1, 4, 9, 16, 25]

short_fruits = [fruit for fruit in fruits if len(fruit) <= 5]
print("short_fruits:", short_fruits)  # ['apple', 'date']
