from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse



def index(request):
    return HttpResponse('Home Page')

def learn_django(request):
    return HttpResponse('<h1>"Hello Django"</h1>')

def learn_python(request):
    return HttpResponse('<h1>Hello Python</h1>')