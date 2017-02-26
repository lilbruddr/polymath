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

def assignment(request):
    context = {
        'course': "MA 103",
        'assignment': "Homework 3.4",
        'number_of_problems': range(1,7),
        'problem_number': 23,
        'problem_text': "Evaluate the following integral. \[\int e^{3x}\ dx\]",
    }
    return render(request, 'polymath/assignment.html', context)

def submit_answer(request):
    if request.method == 'POST':
        if 'answer' in request.POST:
            answer = request.POST['answer']
            # doSomething with pieFact here...
            return HttpResponse('correct') # if everything is OK
    # nothing went well
    return HttpRepsonse('FAIL!!!!!')