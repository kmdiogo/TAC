from django.db import models
from SignIn.CONSTANTS import *
from django.core.validators import RegexValidator
# Create your models here.


class Student(models.Model):
    schoolIdValidator = RegexValidator(SCHOOL_ID_REGEX, 'School Id does not match the school format')

    schoolId = models.CharField(max_length=50, primary_key=True, verbose_name=SCHOOL_ID_ALIAS, validators=[schoolIdValidator])
    firstName = models.CharField(max_length=50, verbose_name="First Name", null=True)
    lastName = models.CharField(max_length=50, verbose_name="Last Name", null=True)
    sex = models.CharField(max_length=1, choices=SEX_CHOICES, verbose_name="Sex", null=True)
    dob = models.DateField(verbose_name="Date of Birth", null=True)
    academicYear = models.CharField(max_length=2, choices=CLASS_CHOICES, verbose_name="Academic Year", null=True)
    major = models.CharField(max_length=50, choices=MAJOR_CHOICES, verbose_name="Major", null=True)
    email = models.EmailField(verbose_name="E-mail", null=True)
    created = models.DateField(auto_now_add=True)

