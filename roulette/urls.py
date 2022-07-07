from django.urls import path
from roulette.views import Spin, Statistic

urlpatterns = [
    path('spin/', Spin.as_view(), name='spin'),
    path('stat/', Statistic.as_view(), name='stat'),
]