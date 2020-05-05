from django.urls import path

from .views import *

app_name = 'rates'

urlpatterns = [
    path('rates', RatesListView.as_view()),
    path('all/rate', RateListView.as_view()),
    path('create/rate', RateCreateView.as_view()),
    path('create/rates', RatesCreateView.as_view()),
]
