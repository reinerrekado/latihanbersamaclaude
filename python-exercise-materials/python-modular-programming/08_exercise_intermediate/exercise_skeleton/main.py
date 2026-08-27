"""
Orchestrator for Exercise 2 - importing grades_utils here should
NOT trigger the self-test print you add inside its
if __name__ == "__main__" guard. You shouldn't need to change
this file; the exercise is in grades_utils.py.

Run:
    python main.py
Then compare with:
    python grades_utils.py
"""
import grades_utils

if __name__ == "__main__":
    scores = [80, 90, 75]
    average = grades_utils.calc_average(scores)
    grade = grades_utils.get_grade(average)

    print(f"Average: {average}, Grade: {grade}")

    # Expected output when run as: python main.py
    #   Average: 81.67, Grade: B
    #   (no "[self-test]" line - importing grades_utils stayed silent)
    #
    # Expected output when run as: python grades_utils.py
    #   [self-test] average=81.67, grade=B
