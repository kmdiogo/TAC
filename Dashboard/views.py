from django.shortcuts import render, redirect
from Dashboard.models import Schedule
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import logout
from django.contrib.admin.views.decorators import staff_member_required

# Create your views here.



@staff_member_required
def index(request):
    #schedules = Schedule.objects.filter(user__username="Y00123456").order_by('dayOfWeek')
    #context = {'schedules': schedules}

    schedules = Schedule.objects.filter(user=request.user).order_by('dayOfWeek')
    context = {'schedules': schedules, 'name': '{f} {l}'.format(f=request.user.first_name, l=request.user.last_name)}
    return render(request, 'Dashboard/index.html', context)


def employee_logout(request):
    logout(request)
    return redirect('index')
