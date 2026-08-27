"""
EXERCISE 2 (INTERMEDIATE) SKELETON - Control Execution with __name__
=============================================================
calc_average() and get_grade() below are already done for you
(carried over from Exercise 1) - this exercise is about
__name__ == "__main__", not the calculations.

Your job: add a self-test block at the BOTTOM of this file that
only runs when this file is executed DIRECTLY, not when main.py
imports it.

Fill in the TODO below, then compare:
    python grades_utils.py   -> the self-test print SHOULD show
    python main.py           -> the self-test print should NOT show
"""

def calc_average(scores):
    return round(sum(scores) / len(scores), 2)


def get_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "E"


# TODO: add a guard below so the following self-test only runs
# when this file is executed directly:
#
#   if __name__ == "__main__":
#       average = calc_average([80, 90, 75])
#       grade = get_grade(average)
#       print(f"[self-test] average={average}, grade={grade}")
