from rest_framework import serializers
from .models import *


class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = ('schoolId', 'firstName', 'lastName')


class CreateStudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = ['schoolId', 'firstName', 'lastName', 'sex', 'dob', 'academicYear', 'major', 'email']


class OpenSessionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Session
        fields = ['course', 'reason', 'student']


class CloseSessionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Session
        fields = ['rating', 'comments']


class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = ['id', 'firstName', 'lastName']


class OpenShiftSerializer(serializers.ModelSerializer):
    firstName = serializers.PrimaryKeyRelatedField(source='employee.firstName', read_only=True)
    lastName = serializers.PrimaryKeyRelatedField(source='employee.lastName', read_only=True)

    class Meta:
        model = Shift
        fields = ['employee', 'firstName', 'lastName']

