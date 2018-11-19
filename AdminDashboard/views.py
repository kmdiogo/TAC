from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required, user_passes_test
from django.template.loader import render_to_string
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.views.decorators.http import require_http_methods, require_GET, require_POST

@staff_member_required
@user_passes_test(lambda u: u.is_superuser)
def index(request):
    context = {'firstName': request.user.first_name, 'lastName': request.user.last_name, 'start': 'home'}
    return render(request, 'AdminDashboard/index.html', context)


