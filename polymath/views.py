from django.shortcuts import render
from django.http import HttpResponse
#from django.template import loader
from polymath.extra_functions import calendar
from polymath.extra_functions import grade_svg_gen
import datetime

def index(request):
    return HttpResponse("Hello, world.  You're at the polls index.")

class Student():
    def __init__(self):
        self.first_name = "Josiah"
        self.last_name = "Hartley"    

def dashboard(request):
    #highlighted_day = datetime.date(2017,6,13)
    highlighted_day = datetime.date.today()
    user = Student()
    month = calendar(highlighted_day)
    grades = grade_svg_gen(46.333, 150)
    context = {
        'user': user,
        'month': month,
        'header_month': highlighted_day.strftime('%B %Y'),
        'bold_day': highlighted_day.day,
        'grade_plot': grades,
    }
    return render(request, 'polymath/dashboard.html', context)