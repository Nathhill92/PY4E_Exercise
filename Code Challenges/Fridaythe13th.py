# Given the month and year as numbers, return whether that month contains a Friday 13th.
# Note - January will be given as 1, February as 2, etc ...
# Examples
# has_friday_13(3, 2020) ➞ True
# has_friday_13(10, 2017) ➞ True
# has_friday_13(1, 1985) ➞ False

import datetime

def has_friday_13(day, year):
    x = datetime.date(year, day, 13)
    return x.strftime("%A") == "Friday"

print(has_friday_13(3, 2020))
print(has_friday_13(10, 2017))
print(has_friday_13(1, 1985))
print(has_friday_13(5, 2025))
print(has_friday_13(3, 2033))
