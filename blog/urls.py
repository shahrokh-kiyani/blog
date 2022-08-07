from django.urls import path

from .views import *

urlpatterns = [
    path('', ListView.as_view(), name='home'),
    path('deatil/<slug:slug>/', DetailView.as_view(), name='detail'),
]
