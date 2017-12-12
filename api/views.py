from django.shortcuts import render, HttpResponse, get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from api.serializer import SchedulingSerializer
from core.models import Scheduling


def home(request):
    return HttpResponse('API')


class SchedulingListView(APIView):
    serializer_class = SchedulingSerializer

    def get(self, request):
        serializer = self.serializer_class(Scheduling.objects.all(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class SchedulingView(APIView):
    serializer_class = SchedulingSerializer

    def get(self, request, pk):
        object = get_object_or_404(Scheduling, pk=pk)
        serializer = self.serializer_class(object, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_409_CONFLICT)

    def delete(self, request, pk):
        object = get_object_or_404(Scheduling, pk=pk)
        object.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)