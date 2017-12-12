from django.db import models
from django.utils import timezone


class Scheduling(models.Model):
    patient = models.CharField(max_length=20)
    procedure = models.CharField(max_length=30)
    date = models.DateField()
    start_time = models.CharField(max_length=20)
    end_time = models.CharField(max_length=20)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.procedure
