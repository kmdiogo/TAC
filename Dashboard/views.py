from django.http import HttpResponse
from SignIn.CONSTANTS import *
from Dashboard.serializer import *
from rest_framework import status
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from Dashboard.models import Schedule
from rest_framework.views import APIView
from rest_framework.exceptions import MethodNotAllowed
from rest_framework.response import Response
from rest_framework.decorators import api_view
from Dashboard.forms import *
from django.views.decorators.http import require_http_methods, require_GET, require_POST
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import logout
from django.utils import timezone
from django.contrib.admin.views.decorators import staff_member_required
from datetime import datetime, timedelta
# Create your views here.


@staff_member_required
def index(request):
    #schedules = Schedule.objects.filter(user__username="Y00123456").order_by('dayOfWeek')
    #context = {'schedules': schedules}

    context = {'firstName': request.user.first_name, 'lastName': request.user.last_name}
    return render(request, 'Dashboard/index.html', context)


@staff_member_required
@require_GET
def home_view(request):
    if request.is_ajax():
        schedules = Schedule.objects.filter(user=request.user).order_by('dayOfWeek')
        context = {'schedules': schedules, 'firstName': request.user.first_name, 'lastName': request.user.last_name}
        return HttpResponse(render_to_string('Dashboard/HomeSection/_HomeSection.html', context, request))


@staff_member_required
@require_http_methods(['GET', 'POST'])
def availability_view(request):
    if request.method == 'GET' and request.is_ajax():
        context = {'availabilities': [], 'firstName': request.user.first_name, 'lastName': request.user.last_name}
        availabilities = Availability.objects.filter(user=request.user).order_by('dayOfWeek')
        for avail in availabilities:
            context['availabilities'].append(AvailabilityForm(instance=avail, prefix=DOW_DICT[avail.dayOfWeek]))
        html = render_to_string('Dashboard/AvailabilitySection/_AvailabilitySection.html', context, request)
        return HttpResponse(html)


@staff_member_required
@api_view(['GET', 'POST'])
def timeoff_view(request):
    if request.method == 'GET':
        form = TimeOffForm()
        today = timezone.now()
        timeoffs = TimeOff.objects.filter(user=request.user, date__gte=today).order_by('date')
        context = {'timeoffs': timeoffs, 'firstName': request.user.first_name, 'lastName': request.user.last_name, 'form': form}
        return HttpResponse(render_to_string("Dashboard/TimeOffSection/_TimeOffSection.html", context, request))
    else:
        form = TimeOffForm(request.POST)
        if form.is_valid():
            newTimeOff = form.save(commit=False)
            newTimeOff.user = request.user
            newTimeOff.save()
            return Response(form.data, status=status.HTTP_201_CREATED)
        return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)


@staff_member_required
@require_GET
def shifts_view(request):
    if request.method == 'GET' and request.is_ajax():
        currentDate = timezone.now()
        starOfWeek = currentDate - timedelta(days=currentDate.weekday())
        endWeek = starOfWeek + timedelta(days=6)
        shifts = Shift.objects.filter(startTime__range=(starOfWeek, endWeek), endTime__isnull=False).distinct()
        context = {'shifts': shifts, 'firstName': request.user.first_name, 'lastName': request.user.last_name}
        return HttpResponse(render_to_string("Dashboard/ShiftsSection/_ShiftsSection.html", context, request))


def employee_logout(request):
    logout(request)
    return redirect('index')


