from rest_framework import serializers
from Dashboard.models import *
from SignIn.CONSTANTS import *
from django.core.validators import RegexValidator


class TimeOffSerializer(serializers.ModelSerializer):

    class Meta:
        model = TimeOff
        fields = ('date', 'reason')