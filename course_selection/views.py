from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User, Subject, Course, Student

# Create your views here.
def index(request):
    id = request.session.get('id', '')
    if id:
        return render(request, 'course_selection/index.html', {'id':id})
    else:
        return redirect('login')

def login(request):
    if request.method == 'POST':
        stuid=request.POST.get('stuid')
        pwd=request.POST.get('password')
        user = User.objects.filter(id__exact=stuid, password__exact=pwd)
        if user:
            request.session['id'] = stuid
            return redirect('index')
    return render(request, 'course_selection/login.html')

def logout(request):
    try:
        del request.session['id']
    except KeyError:
        pass
    return redirect('login')

def select(request):
    id = request.session.get('id', '')
    sub = Subject.objects.filter(student__stuid=id)[0]
    courses = Course.objects.filter(subject=sub)
    
    return render(request, 'course_selection/select.html', {'title':'选课','courses':courses})

def view(request):
    return render(request, 'course_selection/view.html', {'title':'查看课程'})

def delete(request):
    return render(request, 'course_selection/delete.html', {'title':'退选课程'})