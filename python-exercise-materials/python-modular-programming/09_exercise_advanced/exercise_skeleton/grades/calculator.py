"""grades/calculator.py - responsible for the CALCULATIONS. Nothing else.
(Already complete - carried over from Exercises 1 & 2.)
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
