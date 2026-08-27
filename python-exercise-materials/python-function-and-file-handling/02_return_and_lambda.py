"""
DEMO 2: return Statement and lambda Functions
=============================================================
Goal: see why print() alone isn't enough when we want to reuse a
function's result, then learn the lambda shorthand for one-line
functions and what a "clean" function looks like.
"""

# -------------------------------------------------
# 1. Without return - the result stays trapped inside the function
# -------------------------------------------------
def multiply_no_return(num1, num2):
    result = num1 * num2
    # nothing sent back!

x = multiply_no_return(5, 10)
print("x:", x)  # None - the value never left the function

print("-" * 40)

# -------------------------------------------------
# 2. With return - the result is sent back to the caller
# -------------------------------------------------
def multiply(num1, num2):
    result = num1 * num2
    return result

x = multiply(5, 10)
print("x:", x)  # 50 - now we can store it, reuse it, print it, etc.

print("-" * 40)

# -------------------------------------------------
# 3. lambda - a function without a name, for single-line logic only
# -------------------------------------------------
def single_line_function(num1, num2, num3):
    return (num1 + num2 + num3) / 3

lambda_function = lambda num1, num2, num3: (num1 + num2 + num3) / 3

print("def version:", single_line_function(1, 2, 3))       # 2.0
print("lambda version:", lambda_function(1, 2, 3))          # 2.0

print("-" * 40)

# -------------------------------------------------
# 4. Writing a clean function: descriptive name, type hints, docstring
# -------------------------------------------------
def get_average(numbers: list) -> float:
    """
    Get the average value from a list of numbers.

    Args:
        numbers (list): A list of numbers.
    Returns:
        float: The average value.
    """
    return sum(numbers) / len(numbers)

print("get_average:", get_average([10, 20, 30]))  # 20.0
