from django.urls import path
from . views import *

urlpatterns = [
    path('',order,name='order'),
    path('ordersuccess/',order_success,name='order_success')
]
