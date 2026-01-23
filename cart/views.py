from django.shortcuts import render,get_object_or_404,redirect
from . models import Cart,Cartitem
from store.models import Product
# Create your views here.


def _cart_id(request):
    cart_id=request.session.session_key
    if not cart_id:
        cart_id=request.session.create()
    return cart_id




def cart(request):
    total=0
    quantity=0
    cart = None
    cartitem = []
    try:
        cart= Cart.objects.get(cart_id=_cart_id(request))
        cartitem=Cartitem.objects.filter(cart=cart,is_active=True)
        for cartitems in cartitem:
            total += (float(cartitems.product.price) * cartitems.quantity)
            quantity += cartitems.quantity
    except:
        pass
    context={
        'cart':cart,
        'cartitem':cartitem,
        'total':total,
        'quantity':quantity
    }
    return render(request,'cart/cart.html',context)



def add_cart(request,product_id):
    product=get_object_or_404(Product,id=product_id)
    try:
        cart=Cart.objects.filter(cart_id=_cart_id(request))
        cart.save()
    except Cart.DoesNotExist:
        cart=Cart.objects.create(
            cart_id=_cart_id(request)
        )
    try:
        cartitem=Cartitem.objects.filter(product=product,cart=cart)
        cartitem.quantity += 1
        cartitem.save()
    except Cartitem.DoesNotExist:
        cartitem= Cartitem.objects.create(
            product=product,
            cart=cart,
            quantity=1
        )
    return redirect('cart')