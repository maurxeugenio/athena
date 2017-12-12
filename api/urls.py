from django.urls import path
from .views import SchedulingView, SchedulingListView
urlpatterns = [
    path('agendamentos/',  SchedulingListView.as_view()),
    path('agendamento/<int:pk>/', SchedulingView.as_view()),
]