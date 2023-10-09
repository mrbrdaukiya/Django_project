from django.shortcuts import render

# Create your views here.

def learn_django(request):
    return render(request,'courseone.html')
    # return HttpResponse('<h1>Hello Django</h1>')


def learn_python(request):
    return render(request,'coursetwo.html')
    # return HttpResponse('<h1>Hello Python</h1>')
