from core.models import Scheduling
from rest_framework import serializers


class SchedulingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scheduling
        depth = 1
        fields = ['pk', 'patient', 'procedure', 'date', 'start_time', 'end_time']