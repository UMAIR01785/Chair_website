from django.shortcuts import render,redirect
from .forms import OderForm
from .models import Order,OrderItem
from cart.models import Cartitem,Cart
from cart.views import _cart_id
from decimal import Decimal
# Create your views here.
def order(request):
    total=Decimal('0.00')
    quantity=0
    cartitem=[]
    try:
        cart=Cart.objects.get(cart_id=_cart_id(request))
        cartitem=Cartitem.objects.filter(cart=cart, is_active=True)
        for item in cartitem:
            total += Decimal(item.product.price) * item.quantity
            quantity += item.quantity
    except Cart.DoesNotExist:
        return redirect('cart')
    
    if request.method == "POST":
       form= OderForm(request.POST)
       if form.is_valid():
          obj_order=Order.objects.create(
             user=request.user if request.user.is_authenticated else None,
             first_name=form.cleaned_data.get('first_name'),
             last_name=form.cleaned_data.get('last_name'),
             email=form.cleaned_data.get('email'),
             phone_number=form.cleaned_data.get('phone_number'),
             address1=form.cleaned_data.get('address1'),
             address2=form.cleaned_data.get('address2'),
             country=form.cleaned_data.get('country'),
             city=form.cleaned_data.get('city'),
             state=form.cleaned_data.get('state'),
             order_note=form.cleaned_data.get('order_note'),
             total=total
          )

          for item in cartitem:
             orderitem=OrderItem.objects.create(
                order=obj_order,
                product=item.product,
                quantity=item.quantity,
                price=item.product.price
             )
             item.delete()
          
          return redirect('order_success')
    else:
       form=OderForm()
    
    context={
       'form':form,
       'total':total,
       'cartitem':cartitem
    }
        
    
            
    return render(request,'order/order.html',context)


def order_success(request):
   return render(request,'order/success.html')