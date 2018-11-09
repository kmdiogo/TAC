from django.forms import ModelForm
from Dashboard.models import *


class AvailabilityForm(ModelForm):
    class Meta:
        model = Availability
        exclude = ['user']


class TimeOffForm(ModelForm):
    class Meta:
        model = TimeOff
        fields = ['date', 'reason']
