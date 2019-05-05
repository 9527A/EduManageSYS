from django.db import models

# Create your models here.
class User(models.Model):
    id = models.CharField(max_length=12, primary_key=True)
    password = models.CharField(max_length=32)
    flag = models.IntegerField()

class Subject(models.Model):
    subid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)

class Course(models.Model):
    couid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=32)
    flag = models.IntegerField()
    subject = models.ManyToManyField(Subject)

class Student(models.Model):
    stuid = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=10)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    course = models.ManyToManyField(Course,null=True,blank=True)



# class StuCourse(models.Model):
#     stuid = models.ForeignKey(Student, on_delete=models.CASCADE)
#     couid = models.ForeignKey(Course, on_delete=models.CASCADE)

# class SubCourse(models.Model):
#     subid = models.ForeignKey(Subject, on_delete=models.CASCADE)
#     couid = models.ForeignKey(Course, on_delete=models.CASCADE)

