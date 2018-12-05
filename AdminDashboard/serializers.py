from rest_framework import serializers
from Dashboard.models import *
from SignIn.CONSTANTS import *
from django.core.validators import RegexValidator


class TimeOffPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeOff
        fields = ('comment', 'status')
