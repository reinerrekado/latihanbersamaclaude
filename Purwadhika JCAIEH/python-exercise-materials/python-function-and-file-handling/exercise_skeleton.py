"""
EXERCISE SKELETON - Python Function and File Handling
=============================================================
Fill in the TODO sections for each exercise. Each function has:
- A docstring explaining what it should do
- Example inputs/outputs
- A hint
- TODO comments marking where your code goes

At the bottom, uncomment ONE exercise call at a time to test it.
"""

import math


# =================================================================
# EXERCISE 1: Circle Area
# =================================================================
# Write a get_circle_area function with two parameters, radius and
# diameter, both defaulting to None. Return the area of the circle
# using whichever one was given. If BOTH are given, prioritize
# radius.
#   Example: get_circle_area(radius=7)   -> 153.938
#   Example: get_circle_area(diameter=7) -> 38.485
#
# HINT: area = math.pi * radius ** 2. A diameter is 2 * radius, so
#       radius = diameter / 2. round() the final answer to 3 decimals.
def get_circle_area(radius=None, diameter=None):
    # TODO: if radius was given, use it directly
    # TODO: else if diameter was given, convert it to a radius first
    # TODO: return the area, rounded to 3 decimal places
    pass


# =================================================================
# EXERCISE 2: Temperature Converter
# =================================================================
# Write a convert_temperature function that takes a temperature and
# a unit ("C" or "F"). If the unit is "C", convert Celsius to
# Fahrenheit. If the unit is "F", convert Fahrenheit to Celsius.
#   Example: convert_temperature(20, "C") -> 68
#   Example: convert_temperature(68, "F") -> 20
#
# HINT: F = C * 9/5 + 32        C = (F - 32) * 5/9
def convert_temperature(temperature, unit):
    # TODO: if unit == "C", convert Celsius -> Fahrenheit and return it
    # TODO: if unit == "F", convert Fahrenheit -> Celsius and return it
    pass


# =================================================================
# EXERCISE 3: Analyze a Number
# =================================================================
# Write an analyze_number function that takes an integer and returns
# a message describing it. The function should check:
#   1. whether it's positive, negative, or zero
#   2. whether it's even or odd
#   3. (only if positive) whether it's a prime number
#   4. combine the results into one message
#   Example: analyze_number(7)  -> "Prime and odd"
#   Example: analyze_number(-2) -> "Negative and even"
#   Example: analyze_number(9)  -> "Positive and odd"
#   Example: analyze_number(0)  -> "Zero"
#
# HINT: a number is prime if it's > 1 and has no divisor between
#       2 and (number - 1). A nested loop or a helper function both
#       work here.
def analyze_number(num):
    # TODO 1: handle the num == 0 case first -> return "Zero"
    # TODO 2: figure out even/odd with num % 2
    # TODO 3: if num > 0, check for primality and prefer "Prime" over
    #         "Positive" in the message
    # TODO 4: if num < 0, the message should start with "Negative"
    pass


# =================================================================
# EXERCISE 4: Save an Invoice to a File
# =================================================================
# Ask the user how many fruits they bought. For each fruit, ask for
# the name, price, and quantity, then WRITE each item to a file
# named "invoice.txt" in this format (one blank line between items):
#
#   nama buah = mangga
#   qty = 2
#   total = 10000
#
#   nama buah = apel
#   qty = 3
#   total = 9000
#
# Finish by printing: Invoice saved to "invoice.txt"
#
# HINT: open the file once with "w" mode, then loop and call
#       file.write(...) for each item. Remember "\n" for new lines.
def save_invoice():
    # TODO: ask how many items with input(), convert to int
    # TODO: open invoice.txt in write mode
    # TODO: loop that many times, asking name/price/qty each time
    # TODO: write "nama buah = ...", "qty = ...", "total = ..." (price * qty)
    # TODO: close the file (or use `with` instead) and print confirmation
    pass


# =================================================================
# EXERCISE 5: Read the Invoice and Apply a Discount
# =================================================================
# Write a function get_total(list_of_price, discount) that returns
# the total price after applying a percentage discount. Then read
# the "total = ..." lines from invoice.txt (created in Exercise 4)
# to build list_of_price, and call get_total() with a 10% discount.
#   Example: get_total([10000, 9000], 10) -> 17100.0
#
# HINT: open invoice.txt with "r" mode. Loop over file.readlines(),
#       and for every line that starts with "total", split on "="
#       and int() the second part. discount is a PERCENT (10 means 10%).
def get_total(list_of_price, discount):
    # TODO: sum list_of_price, then subtract the discount percentage
    pass


def read_prices_and_get_total():
    # TODO: open invoice.txt, collect every "total" value into a list
    # TODO: call get_total(list_of_price, 10) and print the result
    pass


# =================================================================
# Uncomment ONE line at a time to test each exercise
# =================================================================
if __name__ == "__main__":
    print(get_circle_area(radius=7))
    # print(get_circle_area(diameter=7))
    # print(convert_temperature(20, "C"))
    # print(convert_temperature(68, "F"))
    # print(analyze_number(7))
    # save_invoice()
    # read_prices_and_get_total()
