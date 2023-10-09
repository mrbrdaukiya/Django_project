from django.shortcuts import render
from datetime import datetime

# Create your views here.

def learn_django(request):
    # cname = 'Django'
    # duration = '4 Months'
    # seats = 10
    # django_details = {'nm': cname, 'du': duration, 'st': seats}
    # django_details = {'nm':'django is awesome'}
    # d = datetime.now()



    # return render(request,'course/courseone.html', context= django_details)
    # return render(request,'course/courseone.html', context= django_details)
    # return render(request,'course/courseone.html', {'dt' :d} )
    # return render(request,'course/courseone.html', {'p1' :56.24321, 'p2' :56.000, 'p3' :56.68321} )
    # return render(request,'course/courseone.html', {'nm': True} )
    return render(request,'course/courseone.html', {'nm': 'Django', 'st':5} )


def learn_python(request):
    # student = {'names': ['Rahul', 'Sonam', 'Raj', 'Anu']}
    # stu = {'stu1': {'name':'Rahul', 'roll':101},
    #        'stu2': {'name':'Sonam', 'roll':102},
    #         'stu3': {'name':'Raj', 'roll':103},
    #          'stu4': {'name':'Annu', 'roll':104}, }
    # students = {'student': stu}

    # data = {'name': 'Rahul', 'roll': 101}
    data = {'stu1': {'name':'Rahul', 'roll':101},
           'stu2': {'name':'Sonam', 'roll':102},
            'stu3': {'name':'Raj', 'roll':103},
             'stu4': {'name':'Annu', 'roll':104}, }
    

    
    # return render(request,'course/coursetwo.html', students)
    return render(request,'course/coursetwo.html', {'data': data})
