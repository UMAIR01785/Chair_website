from django.urls import path
from . views import *

urlpatterns = [
    path('',blog,name='blog'),
    path('<slug:slug>/',detail_blog,name='detail_blog'),
]
