from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class NewStudent(models.Model):
    gender_choices = [
        ('M','Male'),
        ('F','Female'),
        ('O','Prefer Not to say'),
    ]
    course_details = [
        ('PYTHON','Python'),
        ('PYTHON FULL STACK','Python Full Stack'),
        ('JAVA','Java'),
        ('JAVA FULL STACK','Java Full Stack'),
        ('MACHINE LEARNING','Machine Learning'),
        ('AWS DEVOPS','AWS Devops'),
        ('TESTING TOOLS','Testing Tools'),
        ('POWER BI','Power BI'),
        ('TABLEAU','Tableau'),
        ('SQL SERVER','SQL Server'),
        ('SELENIUM WITH JAVA','Selenium with Java'),
        ('SELENIUM WITH PYTHON','Selenium with Python'),
        ('AZURE DATA FACTORY','Azure Data Factory'),
        ('MERN DEVELOPMENT','MERN Development'),
        ('ANGULAR JS','Angular Js'),
        ('API TESTING','API Testing'),
    ]
    Name = models.CharField(max_length=25,null=True)
    email = models.EmailField()
    Mobile = models.CharField(max_length=15,null=True)
    gender = models.CharField(max_length=1,choices=gender_choices,null=True)
    course = models.CharField(max_length=20,choices=course_details,null=True, default='Machine Learning')


#demo Demopage
class Student_Demo(models.Model):
    Name = models.CharField(max_length=25,null=True)
    email = models.EmailField()
    Mobile = models.CharField(max_length=15,null=True)
    gender=models.CharField(max_length=20,null=True)
    course = models.CharField(max_length=20,null=True)

    def __str__(self):
        return self.Name


class Remove_student(models.Model):
    Name = models.CharField(max_length=25, null=True)
    email = models.EmailField()
    Mobile = models.CharField(max_length=15, null=True)
    gender = models.CharField(max_length=20, null=True)
    course = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.Name


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    joining_date = models.DateField()
    image = models.ImageField(upload_to='images/', null=True)
    course = models.CharField(max_length=20,null=True)

    def __str__(self):
        return f"{self.user.username}"
