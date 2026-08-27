"""
DEMO 6: Modular Programming Tips
=============================================================
Goal: a few short, runnable illustrations of the tips from the
slides - not a full project, just quick before/after snippets.
"""

# -------------------------------------------------
# 1. Follow the Single Responsibility Principle
# -------------------------------------------------
# Each file/function should handle ONE task. Data loading,
# preprocessing, and model logic belong in separate modules - see
# 03_organizing_project/ for the full example (data.py,
# preprocessing.py, model.py, evaluation.py).
print("Tip 1: one file = one responsibility (see 03_organizing_project/)")

print("-" * 40)

# -------------------------------------------------
# 2. Organize with a clear folder structure
# -------------------------------------------------
# Group related modules into packages so the project flow is easy
# to navigate - see 05_packages_demo/utils/.
print("Tip 2: group related modules into packages (see 05_packages_demo/)")

print("-" * 40)

# -------------------------------------------------
# 3. Use if __name__ == "__main__"
# -------------------------------------------------
# Keep main execution code inside main.py. Use the guard in utility
# modules only for isolated tests - see 04_name_equals_main/.
print("Tip 3: guard runnable code with __name__ == '__main__'")

print("-" * 40)

# -------------------------------------------------
# 4. Avoid circular imports
# -------------------------------------------------
# NEVER let file_A.py import file_B.py while file_B.py also
# imports file_A.py - Python can't resolve the order and raises
# an ImportError. For example, this pair of files would break:
#
#   # file_a.py
#   import file_b
#   def greet_from_a():
#       print("hello from A")
#
#   # file_b.py
#   import file_a          # <- file_a is still being loaded!
#   def greet_from_b():
#       print("hello from B")
#
# Fix: keep a clear one-directional dependency flow (e.g. both
# file_a.py and file_b.py can depend on a shared utils.py, but
# should not depend on EACH OTHER).
print("Tip 4: avoid circular imports (A imports B, B imports A)")

print("-" * 40)

# -------------------------------------------------
# 5. Pass parameters (avoid hardcoding)
# -------------------------------------------------
# BAD: the function only ever works for one hardcoded dataset name
def load_hardcoded():
    return "sales_2024.csv"

# GOOD: the caller decides, so the function is reusable
def load(dataset_name):
    return dataset_name

print("Bad :", load_hardcoded())
print("Good:", load("sales_2025.csv"))
print("Good:", load("churn_dataset.csv"))

print("-" * 40)

# -------------------------------------------------
# 6. Add __init__.py for packages
# -------------------------------------------------
# An (even empty) __init__.py tells Python "this folder is a
# package" and lets you expose a clean public API - see
# 05_packages_demo/utils/__init__.py.
print("Tip 6: add __init__.py to declare a folder as a package")
