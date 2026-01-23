from django.shortcuts import render
from store.models import Product
# Create your views here.
def home(request):
    product=Product.objects.filter(is_available=True).order_by('-created_at')[:3]
    context={
        'product':product,
    }
    return render(request,'home.html',context)


def services(request):
    product=Product.objects.filter(is_available=True).order_by('-created_at')[:3]
    context={
        'product':product,
    }
    return render(request,'shop/services.html',context)