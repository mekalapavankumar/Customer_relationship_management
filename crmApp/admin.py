from django.contrib import admin
from .models import *


# Register your models here.

@admin.register(NewStudent)
class NewStudentAdmin(admin.ModelAdmin):
    list_display = ('Name','email','Mobile','gender','course')
    list_filter=('course',)

@admin.register(Student_Demo)
class Student_DemoAdmin(admin.ModelAdmin):
    list_display = ('Name','email','Mobile','gender','course')
    
@admin.register(Remove_student)
class Remove_demoAdmin(admin.ModelAdmin):
    list_display = ('Name','email','Mobile','gender','course')
    
@admin.register(Student)
class Student_Admin(admin.ModelAdmin):
    list_display = ('user', 'joining_date', 'image', 'course')
