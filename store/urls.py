from django.urls import path
from  . views import shop, product_detail
urlpatterns = [
    path('shop/',shop,name='shop'),
    path('shop/<slug:slug>/',product_detail,name='product_detail'),
    
]
