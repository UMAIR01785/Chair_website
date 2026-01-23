from django.db import models
from store.models import Product
from decimal import Decimal
# Create your models here.
class Cart(models.Model):
    cart_id=models.CharField( max_length=50,unique=True)
    created_at=models.DateTimeField( auto_now_add=True)


    def __str__(self):
        return self.cart_id
    

class Cartitem(models.Model):
    cart=models.ForeignKey(Cart, on_delete=models.CASCADE ,null=True,
        blank=True)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)
    is_active=models.BooleanField(default=True)



    def __str__(self):
        return self.product.product_name
    

    def sub_total(self):
        return Decimal(self.product.price) * self.quantity