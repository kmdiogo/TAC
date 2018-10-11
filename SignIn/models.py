from django.db import models

# Create your models here.
SCHOOL_IDENTIFIER_ALIAS = "Y Number"

class Student(models.Model):
    SEX_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female')
    )
    schoolIdentifier = models.CharField(max_length=50, primary_key=True, verbose_name=SCHOOL_IDENTIFIER_ALIAS)
    firstName = models.CharField(max_length=50, verbose_name="First Name")
    lastName = models.CharField(max_length=50, verbose_name="Last Name")
    sex = models.CharField(max_length=1, choices=SEX_CHOICES, verbose_name="Sex")
    email = models.EmailField(verbose_name="E-mail")
    created = models.DateField(auto_now_add=True)