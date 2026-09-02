"""
DEMO 5: Packages in Python
=============================================================
Goal: see what happens when one module isn't enough - related
modules get grouped into a PACKAGE (a folder + __init__.py):

    05_packages_demo/
        main.py   (this file)
        utils/            <- a PACKAGE (has __init__.py)
            __init__.py
            data.py
            text.py
            visualization.py

Run this file:
    python main.py
"""

# -------------------------------------------------
# 1. "Deep" import - reach directly into a specific module
# -------------------------------------------------
from utils.text import clean_text as clean_text_deep

print(clean_text_deep("  HELLO WORLD  "))   # hello world

print("-" * 40)

# -------------------------------------------------
# 2. "Shallow" import - thanks to utils/__init__.py re-exporting
#    names, we can import straight from the package itself
# -------------------------------------------------
from utils import clean_text, load_data, plot

print(clean_text("  Purwadhika  "))   # purwadhika
data = load_data()
plot(data)

print("-" * 40)

print("Without __init__.py exposing names, we'd always need the")
print('longer form: from utils.data import load_data, etc.')
