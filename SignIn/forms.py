from django import forms
from django.forms import ModelForm
from SignIn.models import Student

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ['schoolIdentifier', 'firstName', 'lastName', 'sex', 'email']