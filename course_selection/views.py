from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, 'course_selection/index.html')

def login(request):
    return render(request, 'course_selection/login.html')

def select(request):
    return render(request, 'course_selection/select.html')

def view(request):
    return render(request, 'course_selection/view.html')

def delete(request):
    return render(request, 'course_selection/delete.html')