from django import forms
from django.forms import ModelForm
from SignIn.models import Student, Session


class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ['schoolId', 'firstName', 'lastName', 'sex', 'email', 'dob', 'major', 'academicYear']


class OpenSessionForm(ModelForm):
    class Meta:
        model = Session
        fields = '__all__'


class CloseSessionForm(ModelForm):

    class Meta:
        model = Session
        fields = ['comments', 'rating']