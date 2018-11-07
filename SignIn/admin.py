from django.contrib import admin
from .models import *


class LogAdmin(admin.ModelAdmin):
    readonly_fields = ('startTime',)

# Register your models here.
admin.site.register(Student)
admin.site.register(Session, LogAdmin)

