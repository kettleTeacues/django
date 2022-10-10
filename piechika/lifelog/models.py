from unittest.util import _MAX_LENGTH
from django.db import models

class sleepLog(models.Model):
    userId = models.EmailField()
    date = models.DateField()
    staDateTime = models.DateTimeField()
    endDateTime = models.DateTimeField()
    sleepingTime = models.CharField(max_length=5)

    def __str__(self):
        return self.userId + ' ' + self.date.strftime('%Y/%m/%d')