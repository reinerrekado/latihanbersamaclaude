"""
DEMO 2: Module in Python
=============================================================
Goal: create our first module (calculator.py) and import it two
different ways.

Run this file (not calculator.py) to see the demo:
    python main.py
"""

# -------------------------------------------------
# 1. import <module_name> - access everything through the module
# -------------------------------------------------
import calculator

result = calculator.add(2, 3)
print("calculator.add(2, 3) =", result)          # 5
print("calculator.subtract(5, 2) =", calculator.subtract(5, 2))   # 3

print("-" * 40)

# -------------------------------------------------
# 2. from <module_name> import <name> - import specific names
# -------------------------------------------------
# This feels more clean and concise - no need to prefix with
# "calculator." every time.
from calculator import add

result = add(2, 3)
print("add(2, 3) =", result)   # 5

print("-" * 40)

# -------------------------------------------------
# 3. Module vs Package vs Project (see slide 11)
# -------------------------------------------------
# - Module  -> a single .py file (calculator.py is a module)
# - Package -> a folder of related modules (see 05_packages_demo/)
# - Project -> the complete application (this whole repo folder)
print("calculator is a MODULE - a single .py file with reusable code.")
