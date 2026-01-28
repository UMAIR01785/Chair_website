from django.db import models
from django.contrib.auth.models import User
from store.models import Product
# Create your models here.
class Order(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.EmailField()
    phone_number=models.CharField(max_length=15)
    country=models.CharField(max_length=20)
    state=models.CharField(max_length=20)
    city=models.CharField(max_length=30)
    address1=models.TextField(max_length=50)
    address2=models.TextField(max_length=50,blank=True)
    order_note=models.TextField(blank=True)
    total=models.DecimalField(max_digits=10,decimal_places=2)
    is_paid=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"Order #{self.id} - {self.first_name} {self.last_name}"
    

class OrderItem(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    price=models.DecimalField(max_digits=10,decimal_places=2)



    
    





    