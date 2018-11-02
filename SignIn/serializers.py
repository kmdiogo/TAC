from rest_framework import serializers
from .models import *
from Dashboard.models import *
from SignIn.CONSTANTS import *
from django.core.validators import RegexValidator


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
        fields = ['rating', 'comments', 'student']


class ShiftSerializer(serializers.ModelSerializer):
    first_name = serializers.ReadOnlyField(source='user.first_name')
    last_name = serializers.ReadOnlyField(source='user.last_name')
    username = serializers.ReadOnlyField(source="user.username")

    class Meta:
        model = Shift
        fields = ['user', 'username', 'first_name', 'last_name']


class GetUserSerializer(serializers.Serializer):
    username_validator = RegexValidator(EMPLOYEE_ID_REGEX, "The username does not match the correct format")
    username = serializers.CharField(validators=[username_validator])



