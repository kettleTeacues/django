from django.db import models
from .consts import MAX_RATE
from django.utils import timezone

import datetime

RATE_CHOICES = [(x, str(x)) for x in range(0, MAX_RATE + 1)]

class sleepLog(models.Model):
    userId = models.EmailField()
    date = models.DateField()
    staDateTime = models.DateTimeField()
    endDateTime = models.DateTimeField()
    sleepingTime = models.CharField(max_length=5)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.userId + ' ' + self.date.strftime('%Y/%m/%d')

class condition(models.Model):
    dateTime = models.DateTimeField(default=timezone.now)
    rate = models.IntegerField(choices = RATE_CHOICES)
    text = models.CharField(max_length = 140)
    picture = models.ImageField(null = True, blank=True)
    sleepLogId = models.ForeignKey(sleepLog, on_delete = models.CASCADE)

    def __str__(self):
        dispDateTime = self.dateTime + datetime.timedelta(hours=9)
        return dispDateTime.strftime('%Y/%m/%d %H:%M:%S')