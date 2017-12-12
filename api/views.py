from django.shortcuts import get_object_or_404
from core.models import Scheduling

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from api.serializer import SchedulingSerializer


class SchedulingListView(APIView):
    serializer_class = SchedulingSerializer

    def get(self, request):
        serializer = self.serializer_class(Scheduling.objects.all(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class SchedulingView(APIView):
    serializer_class = SchedulingSerializer

    def get(self, request, pk):
        scheduling = get_object_or_404(Scheduling, pk=pk)
        serializer = self.serializer_class(scheduling, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        scheduling = get_object_or_404(Scheduling, pk=pk)
        serializer = self.serializer_class(instance=scheduling, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(status=status.HTTP_304_NOT_MODIFIED)

    def delete(self, request, pk):
        scheduling = get_object_or_404(Scheduling, pk=pk)
        scheduling.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SchedulingCreate(APIView):
    serializer_class = SchedulingSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)