from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    first_name=models.CharField(blank=True,max_length=50)
    last_name=models.CharField(blank=True,max_length=40)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='account/user',blank=True)
    bio=models.TextField(blank=True)


    def __str__(self):
        return self.user.username
    

