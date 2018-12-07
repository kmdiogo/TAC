from rest_framework import serializers
from Dashboard.models import *
from SignIn.CONSTANTS import *
from django.core.validators import RegexValidator
from django.contrib.auth.hashers import make_password


class TimeOffPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeOff
        fields = ('comment', 'status')


class CourseOfferSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(source='user.first_name', read_only=True)
    last_name = serializers.CharField(source='user.last_name', read_only=True)

    class Meta:
        model = CourseOffer
        fields = ['course', 'first_name', 'last_name']


# SUPER HACKY WAY TO GET USER AND EMPLOYEE MODELS CREATED IN ONE POST! !!!WARNING REWRITE THIS PLZ!!
class UserEmployee:
    username = ""
    password = ""
    first_name = ""
    last_name = ""
    email = ""
    sex = ""
    dob = ""

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

class EmployeeSerializer(serializers.Serializer):
    username = serializers.ModelField(model_field=User._meta.get_field('username'))
    password = serializers.ModelField(model_field=User._meta.get_field('password'))
    first_name = serializers.ModelField(model_field=User._meta.get_field('first_name'))
    last_name = serializers.ModelField(model_field=User._meta.get_field('last_name'))
    email = serializers.ModelField(model_field=User._meta.get_field('email'))

    sex = serializers.ModelField(model_field=Employee._meta.get_field('sex'))
    dob = serializers.ModelField(model_field=Employee._meta.get_field('dob'))

    def create(self, validated_data):
        d = validated_data
        user = User.objects.create(username=d['username'],
                                       password=make_password(d['password']),
                                       first_name=d['first_name'],
                                       last_name=d['last_name'],
                                       email=d['email'],
                                       is_staff=True,
                                       is_active=True)

        employee = Employee.objects.create(user=user, sex=d['sex'], dob=d['dob'])
        return UserEmployee(username=user.username,
                            password=user.password,
                            first_name=user.first_name,
                            last_name=user.last_name,
                            email=user.email,
                            sex=employee.sex,
                            dob=employee.dob)


