
import datetime
from calendar import monthrange
from math import pi, sin, cos

def grade_svg_gen(overall_grade, dimensions=150):
    """Generate an SVG grade donut chart, given a Student's grades.

    Returns a string with the svg.
    """
    center_dim = dimensions // 2
    radius = center_dim - 5
    font_size_in_px = (radius - 20) // 2

    if overall_grade > 50: # sets which direction the sweep should occur
        dir_flag = 1
    else:
        dir_flag = 0

    ending_angle = (1 - overall_grade/100)*2*pi
    if overall_grade >= 100:
        ending_angle = 2*pi+0.01
    if overall_grade < 0:
        ending_angle = 0

    ending_position_x = center_dim + radius*cos(ending_angle)
    ending_position_y = center_dim - radius*sin(ending_angle)

    svg = """<span style="font-family: 'Open Sans'; font-size:""" + str(font_size_in_px) + """px"><svg width='""" + str(dimensions) + """' height='""" + str(dimensions) + """'>
                <circle cx='""" + str(center_dim) + """' cy='""" + str(center_dim) + """' r='""" + str(radius) + """' stroke="#fff" stroke-width="4" fill="#BDBDBD" />
                <path d="M """ + str(center_dim + radius) + " " + str(center_dim) + """
                        A """ + str(radius) + " " + str(radius) + """ 0 """ + str(dir_flag) + " 1 " + str(ending_position_x) + " " + str(ending_position_y) + """
                        L """ + str(center_dim) + " " + str(center_dim) + """
                        L """ + str(center_dim + radius) + " " + str(center_dim) + """ " stroke="#fff" fill="#1B5E20" stroke-width="4"/>
                <circle cx='""" + str(center_dim) + """' cy='""" + str(center_dim) + """' r='""" + str(radius - 20) + """' stroke="#fff" stroke-width="4" fill="white" />
                <text x='""" + str(center_dim) + """' y='""" + str(center_dim) + """' font-family="Open Sans;" text-anchor="middle" dominant-baseline="middle">""" + str('{:.1f}'.format(overall_grade)) + """%</text>
            </svg></span>"""

    return svg


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