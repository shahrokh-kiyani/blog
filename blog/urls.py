from django.urls import path

from .views import *

urlpatterns = [
    path('', ListView.as_view(), name='home'), # NO path used for home to use site easy
    path('detail/<slug:slug>/', DetailView.as_view(), name='detail'), # Detail path have slug because used slug in models
]
