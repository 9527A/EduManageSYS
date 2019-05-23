from django.shortcuts import render
from django.http import HttpResponse
from . import models

# Create your views here.
def index(request):
    return render(request, 'course_selection/index.html')

def login(request):
    if request.method == 'POST':
        stuid=request.POST.get('stuid')
        pwd=request.POST.get('password')
        if models.User.check_pwd(stuid, pwd):
            return render(request, 'course_selection/index.html')
    return render(request, 'course_selection/login.html')

def select(request):
    return render(request, 'course_selection/select.html', {'title':'选课'})

def view(request):
    return render(request, 'course_selection/view.html', {'title':'查看课程'})

def delete(request):
    return render(request, 'course_selection/delete.html', {'title':'退选课程'})