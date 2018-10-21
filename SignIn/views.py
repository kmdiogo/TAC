from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .forms import *
from .models import *
from rest_framework import viewsets, generics
from rest_framework.views import APIView
from rest_framework.exceptions import MethodNotAllowed
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.http import require_POST, require_http_methods, require_GET
from django.http import JsonResponse, HttpResponse
from .serializers import *
from datetime import datetime
from django_filters.rest_framework import DjangoFilterBackend


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
            session.endTime = datetime.now()
            serializer = CloseSessionSerializer(session, data=request.data)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CreateOpenSessionView(APIView):
    def post(self, request, format=None):
        serializer = OpenSessionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@require_http_methods(['GET'])
def index(request):
    studentForm = StudentForm()
    openSessionForm = OpenSessionForm()
    closeSessionForm = CloseSessionForm()

    context = {'studentForm': studentForm, 'openSessionForm': openSessionForm, 'closeSessionForm': closeSessionForm}
    return render(request, 'SignIn/Index.html', context)






