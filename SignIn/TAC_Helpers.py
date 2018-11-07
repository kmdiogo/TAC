from django.contrib.auth.models import User
from Dashboard.models import Shift
from SignIn.models import *
from django.http import Http404


def get_user_or_404(username):
    try:
        return User.objects.get(username__iexact=username)
    except User.DoesNotExist:
        raise Http404("User with username {username} does not exist".format(username=username))


def get_open_shift_or_404(user):
    try:
        return Shift.objects.get(user=user, endTime__isnull=True)
    except Shift.DoesNotExist:
        raise Http404("An open shift does not exist for this user")


def get_student_or_404(schoolId):
    try:
        return Student.objects.get(schoolId__iexact=schoolId)
    except Student.DoesNotExist:
        raise Http404("Student with ID {id} does not exist".format(id=schoolId))

