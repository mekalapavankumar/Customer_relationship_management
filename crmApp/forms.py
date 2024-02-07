from django import forms
from .models import *

class NewStudentForm(forms.ModelForm):
    class Meta:
        model = NewStudent
        fields = "__all__"
        
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"