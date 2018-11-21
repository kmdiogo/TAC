from django.db import models
from SignIn.CONSTANTS import *
from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator
import datetime
# Create your models here.


class Person(models.Model):
    firstName = models.CharField(max_length=50, verbose_name="First Name")
    lastName = models.CharField(max_length=50, verbose_name="Last Name")
    sex = models.CharField(max_length=1, choices=SEX_CHOICES, verbose_name="Sex")
    dob = models.DateField(verbose_name="Date of Birth")
    email = models.EmailField(verbose_name="E-mail")
    created = models.DateField(auto_now_add=True)

    class Meta:
        abstract = True


class Log(models.Model):
    startTime = models.DateTimeField(auto_now_add=True)
    endTime = models.DateTimeField(null=True, blank=True)

    class Meta:
        abstract = True


# -----------------------STUDENT---------------------
class Student(Person):
    schoolIdValidator = RegexValidator(SCHOOL_ID_REGEX, 'School ID does not match the specified format')
    schoolId = models.CharField(max_length=50, primary_key=True, verbose_name=SCHOOL_ID_ALIAS, validators=[schoolIdValidator])
    academicYear = models.CharField(max_length=2, choices=CLASS_CHOICES, verbose_name="Academic Year")
    major = models.CharField(max_length=50, choices=MAJOR_CHOICES, verbose_name="Major")

    def __str__(self):
        return '{id} - {last}, {first}'.format(id=self.schoolId, last=self.lastName, first=self.firstName)


class Session(Log):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.CharField(max_length=50, verbose_name="Course Seeking Help For", choices=COURSE_CHOICES)
    reason = models.CharField(max_length=50, verbose_name="Reason for Visit")
    rating = models.PositiveSmallIntegerField(null=True, blank=True, validators=[MinValueValidator(1), MaxValueValidator(4)])
    comments = models.TextField(null=True, blank=True, max_length=1000)

    def __str__(self):
        if not self.endTime:
            return '{date} - Open {course} session for {student}'.format(course=self.course, student=self.student,
                                                                         date=self.startTime.date())
        else:
            return '{date} - Closed {course} session for {student}'.format(course=self.course, student=self.student,
                                                                           date=self.startTime.date())


# --------------------------EMPLOYEE----------------------------





