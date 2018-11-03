from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .forms import *
from .models import *
from rest_framework import viewsets, generics, status
from rest_framework.views import APIView
from rest_framework.exceptions import MethodNotAllowed
from rest_framework.response import Response
from django.views.decorators.http import require_POST, require_GET
from .serializers import *
from django.utils import timezone
from django.contrib.auth.models import User
from Dashboard.models import *
from rest_framework.decorators import api_view
from .TAC_Helpers import *


# class EmployeeView(viewsets.ModelViewSet):
#     queryset = Employee.objects.all()
#     http_method_names = ['get']
#     serializer_class = EmployeeSerializer
#
#     def list(self, request, *args, **kwargs):
#         raise MethodNotAllowed("GET")


class StudentView(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    http_method_names = ['get', 'post']

    def get_serializer_class(self):
        if self.action == 'create':
            return CreateStudentSerializer
        return StudentSerializer

    def list(self, request, *args, **kwargs):
        raise MethodNotAllowed("GET")


class OpenSessionsView(APIView):

    def get_object(self, pk):
        try:
            return Session.objects.get(student__schoolId__iexact=pk, endTime__isnull=True)
        except Session.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        student = self.get_object(pk)
        serializer = OpenSessionSerializer(student)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        session = self.get_object(pk)
        serializer = CloseSessionSerializer(session, data=request.data)
        if serializer.is_valid():
            session.endTime = timezone.now()
            serializer = CloseSessionSerializer(session, data=request.data)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CreateOpenSessionView(APIView):
    def post(self, request, format=None):
        serializer = OpenSessionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@require_GET
def index(request):
    studentForm = StudentForm()
    openSessionForm = OpenSessionForm()
    closeSessionForm = CloseSessionForm()

    context = {'studentForm': studentForm, 'openSessionForm': openSessionForm, 'closeSessionForm': closeSessionForm}
    return render(request, 'SignIn/Index.html', context)


@api_view(['POST'])
def clock_in_shift(request, pk):
    user = get_user_or_404(pk)
    if Shift.objects.filter(user=user, endTime__isnull=True).exists():
        return Response({'error': 'An open session already exists for this user'}, status=status.HTTP_400_BAD_REQUEST)

    newShift = Shift(user=user)
    newShift.save()
    return Response({"username": user.username, 'firstName': user.first_name, 'clockInTime': newShift.startTime}, status=status.HTTP_201_CREATED)


@api_view(['PUT'])
def clock_out_shift(request, pk):
    user = get_user_or_404(pk)
    if not Shift.objects.filter(user=user, endTime__isnull=True).exists():
        return Response({'error': 'An open shift does not exist for this user'}, status=status.HTTP_400_BAD_REQUEST)

    closeShift = get_open_shift_or_404(user)
    closeShift.endTime = timezone.now()
    closeShift.save()
    return Response({'username': user.username, 'firstName': user.first_name, 'clockOutTime': closeShift.endTime}, status=status.HTTP_200_OK)



















