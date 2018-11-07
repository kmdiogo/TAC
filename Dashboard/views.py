from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from Dashboard.models import Schedule
from Dashboard.forms import *
from django.views.decorators.http import require_http_methods, require_GET
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import logout
from django.contrib.admin.views.decorators import staff_member_required

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
        return HttpResponse(render_to_string('Dashboard/HomeSection/_HomeSection.html', context))


@staff_member_required
@require_http_methods(['GET', 'POST'])
def availability_view(request):
    if request.method == 'GET' and request.is_ajax():
        context = {'availabilities': [], 'firstName': request.user.first_name, 'lastName': request.user.last_name}
        availabilities = Availability.objects.filter(user=request.user).order_by('dayOfWeek')
        for avail in availabilities:
            context['availabilities'].append(AvailabilityForm(instance=avail))
        html = render_to_string('Dashboard/AvailabilitySection/_AvailabilitySection.html', context)
        return HttpResponse(html)


def employee_logout(request):
    logout(request)
    return redirect('index')
