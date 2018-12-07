from django.forms import ModelForm
from django import forms
from Dashboard.models import *
from django.contrib.auth.models import User


class UserForm(ModelForm):

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']
