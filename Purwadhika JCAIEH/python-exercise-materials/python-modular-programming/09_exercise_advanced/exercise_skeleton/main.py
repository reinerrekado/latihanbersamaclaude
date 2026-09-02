"""
Orchestrator for Exercise 3 - relies on grades/__init__.py
exposing get_grade and print_report at the PACKAGE level. You
shouldn't need to change this file; the exercise is inside the
grades/ package (report.py and __init__.py).

NOTE: the two imports below will raise an ImportError until you
fill in the TODOs in grades/__init__.py - that's expected, keep
going until it passes.

Run:
    python main.py
"""
from grades import get_grade, print_report   # <- only works once __init__.py exposes these!
from grades.calculator import calc_average
from grades.loader import get_scores

if __name__ == "__main__":
    scores = get_scores()
    average = calc_average(scores)
    grade = get_grade(average)
    print(f"Average: {average}, Grade: {grade}")

    print_report()

    # Expected output:
    # Average: 81.67, Grade: B
    # Scores: [80, 90, 75]
    # Average: 81.67
    # Grade: B
