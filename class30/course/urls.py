from django.urls import path
from . import views

urlpatterns = [
    path('learndj/', views.learn_djanngo, name='coursename'),
    # path('learndjone/', views.learn_djanngo, name='coursename'),
]