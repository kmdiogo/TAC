from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required, user_passes_test
from django.template.loader import render_to_string
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.views.decorators.http import require_http_methods, require_GET, require_POST
from datetime import datetime, timedelta
import calendar
from django.utils import timezone
from SignIn.models import *
from django.db.models import Count

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
    context = {'data': {}}
    for i in range(7):
        context['data'][DOW_DICT[i]] = Session.objects.filter(startTime__range=(startOfWeek, endOfWeek),
                                                      endTime__isnull=False, startTime__week_day=i+1).count()
    context['weekOf'] = startOfWeek.strftime('%m/%d/%Y')
    return JsonResponse(context)


@staff_member_required
@user_passes_test(lambda u: u.is_superuser)
@api_view(['GET'])
def monthly_traffic(request):
    currentDate = timezone.now()
    daysInMonth = calendar.monthrange(currentDate.year, currentDate.month)[1]
    context = {'data': {}}
    for i in range(1, daysInMonth+1):
        dateLabel = datetime.date(currentDate.year, currentDate.month, i).strftime('%m/%d/%Y')
        context['data'][dateLabel] = Session.objects.filter(startTime__month=currentDate.month, startTime__day=i,
                                                    endTime__isnull=False).count()
    context['month'] = currentDate.strftime('%B')
    return JsonResponse(context)


@staff_member_required
@user_passes_test(lambda u: u.is_superuser)
@api_view(['GET'])
def monthly_course_traffic(request):
    currentDate = timezone.now()
    daysInMonth = calendar.monthrange(currentDate.year, currentDate.month)[1]
    context = {'labels': [], 'values': [], 'colors': []}
    query = Session.objects.all().values('course').annotate(count=Count('course')).order_by('-count')[:5]
    for o in query:
        context['labels'].append(o['course'])
        context['values'].append(o['count'])
        context['colors'].append(COURSE_COLORS[o['course']])

    return JsonResponse(context)




