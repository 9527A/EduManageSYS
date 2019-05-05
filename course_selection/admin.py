from django.contrib import admin

# Register your models here.

from course_selection.models import User, Course, Subject, Student

admin.site.register(User)
admin.site.register(Course)
admin.site.register(Subject)
admin.site.register(Student)