from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required, user_passes_test
from django.template.loader import render_to_string
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.views.decorators.http import require_http_methods, require_GET, require_POST
from datetime import datetime, timedelta
from django.utils import timezone
from SignIn.models import *

@staff_member_required
@user_passes_test(lambda u: u.is_superuser)
@api_view(['GET'])
def index(request):
    context = {'firstName': request.user.first_name, 'lastName': request.user.last_name}
    return render(request, 'AdminDashboard/index.html', context)


@staff_member_required
@user_passes_test(lambda u: u.is_superuser)
@api_view(['POST', 'GET'])
def home_view(request):
    context = {'firstName': request.user.first_name, 'lastName': request.user.last_name}
    return HttpResponse(render_to_string('AdminDashboard/HomeSection/HomeSection.html', context, request))


@staff_member_required
@user_passes_test(lambda u: u.is_superuser)
@api_view(['GET'])
def analytics_view(request):
    context = {'firstName': request.user.first_name, 'lastName': request.user.last_name}
    return HttpResponse(render_to_string('AdminDashboard/AnalyticsSection/AnalyticsSection.html', context, request))


@staff_member_required
@user_passes_test(lambda u: u.is_superuser)
@api_view(['GET'])
def weekly_traffic(request):
    currentDate = timezone.now()
    startOfWeek = currentDate - timedelta(days=currentDate.weekday())
    startOfWeek = startOfWeek.replace(hour=0, minute=0, second=0, microsecond=0)
    endOfWeek = startOfWeek + timedelta(days=6)
    context = {}
    for i in range(7):
        context[DOW_DICT[i]] = Session.objects.filter(startTime__range=(startOfWeek, endOfWeek),
                                                      endTime__isnull=False, startTime__week_day=i+1).count()
    return JsonResponse(context)


