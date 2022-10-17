from django.contrib import admin
from .models import condition, sleepLog

admin.site.register(sleepLog)
admin.site.register(condition)