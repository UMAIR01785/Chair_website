from django.shortcuts import render,get_object_or_404
from . models import Product
# Create your views here.


def shop(request):
    products=Product.objects.filter(is_available=True)
    context={
        'products':products
    }
    return render(request,'shop/shop.html',context)


def product_detail(request,slug):
    product=get_object_or_404(Product, slug=slug, is_available=True)

    context={
        "product":product,
    }
    return render(request,'shop/product_detail.html',context)
