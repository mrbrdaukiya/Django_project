from django.shortcuts import render

# Create your views here.

def learn_djanngo(request):
    return render(request, 'course/courseinfo.html')