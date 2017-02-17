from django.shortcuts import render
from django.http import HttpResponse
#from django.template import loader
import polymath.calendar_gen as cal

def index(request):
    return HttpResponse("Hello, world.  You're at the polls index.")

class Student():
    def __init__(self):
        self.first_name = "Josiah"
        self.last_name = "Hartley"    

def dashboard(request):
    user = Student()
    month = cal.calendar()
    context = {
        'user': user,
        'month': month
    }
    return render(request, 'polymath/dashboard.html', context)