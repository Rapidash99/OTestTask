from django.urls import path

from .views import *

app_name = 'rates'

urlpatterns = [
    path('', MetricsListView.as_view()),
]
