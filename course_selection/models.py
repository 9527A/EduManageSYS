from django.db import models

# Create your models here.
class User(models.Model):
    id = models.CharField(max_length=12, primary_key=True)
    password = models.CharField(max_length=128,null=True,blank=True)
    flag = models.IntegerField(null=True,blank=True)


class Subject(models.Model):
    subid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)


class Course(models.Model):
    couid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=32)
    flag = models.IntegerField()
    maxnum = models.IntegerField(null=True,blank=True)
    nownum = models.IntegerField(default=0,null=True,blank=True)
    subject = models.ManyToManyField(Subject,null=True,blank=True)
    '''
    	0：必修
		10：专业课必修
		11：专业课限选
		21：体育课限选
		31：公共课限选
        32：慕课任选
    '''


class Student(models.Model):
    stuid = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=10)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE,null=True,blank=True)
    course = models.ManyToManyField(Course,null=True,blank=True)




# class StuCourse(models.Model):
#     stuid = models.ForeignKey(Student, on_delete=models.CASCADE)
#     couid = models.ForeignKey(Course, on_delete=models.CASCADE)

# class SubCourse(models.Model):
#     subid = models.ForeignKey(Subject, on_delete=models.CASCADE)
#     couid = models.ForeignKey(Course, on_delete=models.CASCADE)

