from django.urls import path

from .views import *

urlpatterns = [
    path('', ListView.as_view(), name='listview'),
    path('<slug>:<slug>/', DetailView.as_view(), name='detailview'),
]
