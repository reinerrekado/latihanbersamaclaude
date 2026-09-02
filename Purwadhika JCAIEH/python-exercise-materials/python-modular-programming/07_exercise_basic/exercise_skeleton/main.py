"""
Orchestrator for Exercise 1 - imports grades_utils and uses it.
You shouldn't need to change this file; the exercise is in
grades_utils.py.

Run:
    python main.py
"""
import grades_utils

if __name__ == "__main__":
    scores = [80, 90, 75]

    average = grades_utils.calc_average(scores)
    grade = grades_utils.get_grade(average)

    print(f"Scores: {scores}")
    print(f"Average: {average}")
    print(f"Grade: {grade}")

    # Expected output:
    # Scores: [80, 90, 75]
    # Average: 81.67
    # Grade: B
