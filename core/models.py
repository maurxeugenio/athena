from django.db import models
from django.utils import timezone


class Scheduling(models.Model):
    data = models.DateField()
    start_time = models.CharField(max_length=20)
    end_time = models.CharField(max_length=20)
    patient = models.CharField(max_length=20)
    procedure = models.CharField(max_length=30)
    created_at = models.DateTimeField(default=timezone.now)