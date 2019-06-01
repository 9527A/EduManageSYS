from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
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
    stu = Student.objects.get(stuid=id)
    if request.method == 'POST':
        couid = request.POST.get('couid')
        cou = Course.objects.get(couid=couid)
        if cou.nownum < cou.maxnum:
            stu.course.add(couid)
            cou.nownum = cou.nownum + 1
            cou.save()
        else:
            messages.error(request,"人数已满")
        return redirect('select')
    sub = Subject.objects.filter(student__stuid=id).first()
    courses = Course.objects.filter(subject=sub).filter(flag__in=[11,21,31,32]).order_by('flag')
    courses_on = Course.objects.filter(student__stuid=id).filter(flag__in=[11,21,31,32]).order_by('flag')
    flags_on = []
    for item in courses_on:
        if item.flag == 11:
            flags_on.append(11)
        elif item.flag == 21:
            flags_on.append(21)
        elif item.flag == 31:
            flags_on.append(31)

    return render(request, 'course_selection/select.html', {'title':'选课','courses':courses, 'courses_on':courses_on, 'flags_on':flags_on})

def view(request):
    id = request.session.get('id', '')
    courses = Course.objects.filter(student__stuid=id).order_by('flag')
    return render(request, 'course_selection/view.html', {'title':'查看课程', 'courses':courses})

def delete(request):
    id = request.session.get('id', '')
    stu = Student.objects.get(stuid=id)
    if request.method == 'POST':
        couid = request.POST.get('couid')
        cou = Course.objects.get(couid=couid)
        stu.course.remove(couid)
        cou.nownum = cou.nownum - 1
        cou.save()
        return redirect('delete')
    courses = Course.objects.filter(student__stuid=id).filter(flag__in=[11,21,31,32]).order_by('flag')
    return render(request, 'course_selection/delete.html', {'title':'退选课程', 'courses':courses})