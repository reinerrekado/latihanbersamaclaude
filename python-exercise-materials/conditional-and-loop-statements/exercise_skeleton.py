"""
EXERCISE SKELETON - Conditional and Loop Statements
=============================================================
Fill in the TODO sections for each exercise. Each function has:
- A docstring explaining what it should do
- Example inputs/outputs (from the slides)
- `pass` or a TODO comment where your code goes

At the bottom, uncomment ONE exercise call at a time to test it
(running all 4 at once means answering a lot of input() prompts back
to back, so it's easier to test them one by one).
"""


# =================================================================
# EXERCISE 1: Even, Odd, or Zero
# =================================================================
# Write a code to check if the input number is "even", "odd", or "zero"
#   Example: number = 10 -> "even"
#   Example: number = 1  -> "odd"
#   Example: number = 0  -> "zero"
#
# HINT: a number is even if it divides evenly by 2 -> number % 2 == 0
#       don't forget zero is neither even nor odd for this exercise -
#       check for zero FIRST before checking even/odd.
def check_number_type():
    number = int(input("Enter a number: "))

    # TODO: write your if / elif / else here
    # if ...:
    #     print("zero")
    # elif ...:
    #     print("even")
    # else:
    #     print("odd")
    pass


# =================================================================
# EXERCISE 2: Average Until Zero
# =================================================================
# Write a program to repeatedly ask the user for an integer until 0
# is entered. Then, print the average of all entered integers,
# excluding 0.
#   Example: 1, 2, 3, 0    -> average = 2
#   Example: 1, 2, 0       -> average = 1.5
#
# HINT: use a `while True:` loop, break when the input is 0.
#       keep a running total and a count of how many numbers were entered.
def average_until_zero():
    total = 0
    count = 0

    # TODO: loop asking for input until the user enters 0
    # while True:
    #     number = int(input("Enter an integer (0 to stop): "))
    #     if ...:
    #         break
    #     total += number
    #     count += 1

    # TODO: calculate and print the average
    # careful: what happens if count is still 0 (user entered 0 immediately)?
    pass


# =================================================================
# EXERCISE 3: Largest of Three
# =================================================================
# Write a code to ask the user to enter 3 integers and print the
# largest number.
#   Example: 9, 2, 3 -> largest = 9
#
# HINT: you can compare with if/elif/else
def largest_of_three():
    num1 = int(input("Enter first integer: "))
    num2 = int(input("Enter second integer: "))
    num3 = int(input("Enter third integer: "))

    # TODO: find and print the largest of num1, num2, num3
    pass


# =================================================================
# EXERCISE 4: Sum of Primes in Range
# =================================================================
# Write a code that asks the user to enter the lower and upper bounds
# of a range of positive integers. Then, calculate and print the sum
# of all prime numbers within that range. If the lower bound is
# greater than the upper bound, print "range not valid" instead.
#   Example: lower = 10, upper = 0  -> "range not valid"
#   Example: lower = 0,  upper = 10 -> 17   (2 + 3 + 5 + 7 = 17)
#   Example: lower = -1             -> "range not valid"
#
# HINT: a prime number is a number greater than 1 that is only
#       divisible by 1 and itself. You'll need a loop INSIDE a loop:
#       - outer loop: walk through every number in the range
#       - inner loop: check if that number has any divisor other than
#         1 and itself (if it does, it's NOT prime)
def sum_of_primes_in_range():
    lower = int(input("Enter lower bound: "))
    upper = int(input("Enter upper bound: "))

    # TODO 1: handle the invalid range case first (lower > upper),
    #         print "range not valid" and stop the function

    # TODO 2: loop through every number from lower to upper (inclusive)
    #         for each number, figure out whether it's prime
    #         (hint: numbers <= 1 are never prime)

    # TODO 3: keep a running total of the prime numbers you find,
    #         then print it
    pass


# =================================================================
# Uncomment ONE line at a time to test each exercise
# =================================================================
if __name__ == "__main__":
    check_number_type()
    # average_until_zero()
    # largest_of_three()
    # sum_of_primes_in_range()
