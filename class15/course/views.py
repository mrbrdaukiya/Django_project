from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse



def index(request):
    return HttpResponse('Home Page')

def learn_django(request):
    return HttpResponse("Hello Django")

def learn_python(request):
    return HttpResponse('<h1>Hello Python</h1>')

def learn_var(request):
    a = '<h1>Hello Variable</h1>'
    return HttpResponse(a)

def learn_math(request):
    a = 10 + 10
    return HttpResponse(a)

def learn_format(request):
    a = '<h1>Guru Choudhary </h1>'
    return HttpResponse(f'Hello How are you {a}')