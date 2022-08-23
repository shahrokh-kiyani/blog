from django.urls import path

from .views import *

urlpatterns = [
    path('', ListView.as_view(), name='home'), # NO path used for home to use site easy
    path('detail/<slug:slug>/', post_detail_view, name='detail'), # Detail path have slug because used slug in models
    path('category/', CategoryListView.as_view(), name='category'), # Category path have slug because used slug in models
    path('category/<slug:slug>/', category_detail_view, name='category_detail'), # Category deatail is view for see what posts have same category
    path('search/', search_view, name='search'),
]
