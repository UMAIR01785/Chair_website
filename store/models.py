from django.db import models
from django.utils.text import slugify
from uuid import uuid4
from django.urls import reverse
# Create your models here.
class Product(models.Model):
    product_name=models.CharField( max_length=50)
    price=models.CharField( max_length=50)
    image=models.ImageField(upload_to='media')
    is_available=models.BooleanField(default=True)
    stock=models.IntegerField()
    slug=models.SlugField(blank=True)
    is_feature=models.BooleanField(default=False)
    created_at=models.DateTimeField( auto_now_add=True,blank=True,null=True)


    def __str__(self):
        return self.product_name
        
    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug=f"{slugify(self.product_name)}-{uuid4().hex[:4]}"
        super().save(*args,**kwargs)


    def get_url(self):
        return reverse('product_detail',args=[self.slug])