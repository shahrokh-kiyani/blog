from django.urls import path

from .views import *

urlpatterns = [
    path('', ListView.as_view(), name='home'),
]
