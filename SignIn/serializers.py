from rest_framework import serializers
from .models import Student, Session


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


