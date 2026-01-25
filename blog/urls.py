from django.urls import path
from . views import *

urlpatterns = [
    path('',blog,name='blog'),
    path('detail/<slug:slug>/',detail_blog,name='detail_blog'),
    path('blog_cart/',blog_cart,name='blog_cart'),
    path('add_blog/',add_blog,name='add_blog'),
    path('edit_blog/<slug:slug>/',edit_blog,name='edit_blog'),
    path('delete_blog/<slug:slug>/',delete_blog,name='delete_blog')
]
