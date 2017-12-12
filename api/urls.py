from django.urls import path
from .views import SchedulingView, SchedulingListView, SchedulingCreate
urlpatterns = [
    path('agendamento/criar/', SchedulingCreate.as_view(), name='create'),
    path('agendamento/<int:pk>/', SchedulingView.as_view(), name='details'),
    path('agendamentos/',  SchedulingListView.as_view(), name='list'),
]
