from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils.text import slugify
from uuid import uuid4
# Create your models here.
class Blog(models.Model):
    blog_title=models.CharField(unique=True, max_length=50)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    image=models.ImageField(upload_to='media/blog')
    description=models.TextField()
    slug=models.SlugField(blank=True)
    created_at=models.DateTimeField( auto_now_add=True)
    is_feature=models.BooleanField(default=False)


    def __str__(self):
        return self.blog_title
    
    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug=f"{slugify(self.blog_title)}-{uuid4().hex[:2]}"
        super().save(*args,**kwargs)


    def get_url(self):
        return reverse('detail_blog',args=[self.slug])

   