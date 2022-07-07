from django.urls import path
from roulette.views import Spin

urlpatterns = [
    path('spin/', Spin.as_view(), name='spin'),
]