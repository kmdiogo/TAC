from django.db import models
from SignIn.CONSTANTS import *
from django.contrib.auth.models import User
from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator
from SignIn.CONSTANTS import *
from django.db.models.signals import post_save


def custom_user_string_method(self):
    if self.first_name and self.last_name:
        return '{user} - {last}, {first}'.format(user=self.username, last=self.last_name, first=self.first_name)
    return self.username


User.add_to_class("__str__", custom_user_string_method)


class Employee(models.Model):
    employeeIdValidator = RegexValidator(EMPLOYEE_ID_REGEX, 'Employee ID does not match the specified format')
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #employeeId = models.CharField(max_length=50, primary_key=True, verbose_name=EMPLOYEE_ID_ALIAS, validators=[employeeIdValidator])
    sex = models.CharField(max_length=1, choices=SEX_CHOICES, verbose_name="Sex")
    dob = models.DateField(verbose_name="Date of Birth")
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return '{id} - {last}, {first}'.format(id=self.user, last=self.user.last_name, first=self.user.first_name)


class Shift(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    startTime = models.DateTimeField(auto_now_add=True)
    endTime = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        if not self.endTime:
            return 'Open Shift for {employee} - {last}, {first}'.format(employee=self.user.username, last=self.user.last_name, first=self.user.first_name)
        else:
            return 'Closed Shift for {employee} - {last}, {first}'.format(employee=self.user.username, last=self.user.last_name, first=self.user.first_name)


class CourseOffer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.CharField(max_length=50, verbose_name="Course Number")


class AbstractAvailSched(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    dayOfWeek = models.PositiveSmallIntegerField(validators=[MinValueValidator(DOW_ALLOWED_MIN), MaxValueValidator(DOW_ALLOWED_MAX)])
    h0600 = models.BooleanField(default=False)
    h0700 = models.BooleanField(default=False)
    h0800 = models.BooleanField(default=False)
    h0900 = models.BooleanField(default=False)
    h1000 = models.BooleanField(default=False)
    h1100 = models.BooleanField(default=False)
    h1200 = models.BooleanField(default=False)
    h1300 = models.BooleanField(default=False)
    h1400 = models.BooleanField(default=False)
    h1500 = models.BooleanField(default=False)
    h1600 = models.BooleanField(default=False)
    h1700 = models.BooleanField(default=False)
    h1800 = models.BooleanField(default=False)
    h1900 = models.BooleanField(default=False)

    class Meta:
        abstract = True
        unique_together = (('user', 'dayOfWeek'),)


class Availability(AbstractAvailSched):

    def __str__(self):

        return '{dow} Availability for {id} - {last}, {first}'.format(id=self.user.username,
                                                                      last=self.user.last_name,
                                                                      first=self.user.first_name,
                                                                      dow=DOW_DICT[self.dayOfWeek])


class Schedule(AbstractAvailSched):

    def __str__(self):
        return '{dow} Schedule for {id} - {last}, {first}'.format(id=self.user.username,
                                                                  last=self.user.last_name,
                                                                  first=self.user.first_name,
                                                                  dow=DOW_DICT[self.dayOfWeek])


# ----------MODEL SIGNALS FOR USER----------
def create_profile(sender, **kwargs):
    user = kwargs['instance']
    if kwargs['created']:
        # Create empty schedules and availabilities for the created user
        for dow in range(DOW_ALLOWED_MIN, DOW_ALLOWED_MAX+1):
            sched = Schedule(user=user, dayOfWeek=dow)
            avail = Availability(user=user, dayOfWeek=dow)
            sched.save()
            avail.save()

post_save.connect(create_profile, sender=User)