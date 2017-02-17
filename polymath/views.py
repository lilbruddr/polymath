from django.shortcuts import render
from django.http import HttpResponse
#from django.template import loader

def index(request):
    return HttpResponse("Hello, world.  You're at the polls index.")

def dashboard(request):
    context = {}
    return render(request, 'polymath/dashboard.html', context)