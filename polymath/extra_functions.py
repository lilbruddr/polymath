
import datetime
from calendar import monthrange

def calendar(given_day=datetime.date.today()):
    """Generate a calendar for the month containing the given date.

    Returns a matrix with 0s for missing days.
    """
    this_month = given_day.month
    this_year = given_day.year
    this_day = given_day.day

    if this_month == 1 or this_month == 2:
        this_month += 12
        this_year -= 1

    century = this_year // 100
    last_two_digits = this_year % 100

    sum = 1 + int(2.6*this_month - 5.39) + century // 4 + last_two_digits // 4 + last_two_digits - 2*century
    
    first_day_of_month = sum % 7
    
    this_month = given_day.month
    this_year = given_day.year

    num_days = max(monthrange(this_year,this_month))
    num_weeks = ((num_days + first_day_of_month) // 7) + 1

    month = [[]]
    day_i = 0
    for empty in range(first_day_of_month):
        month[0].append(0)
    for day_of_first_week in range(first_day_of_month,7):
        day_i = day_of_first_week - first_day_of_month + 1
        month[0].append(day_i)
    for week in range(1,num_weeks):
        month.append([])
        for day in range(7):
            if day_i < num_days:
                day_i += 1
                month[week].append(day_i)
            else:
                month[week].append(0)

    return month