from django.db import models

# Create your models here.
class TeamMange(models.Model):
    name=models.CharField( max_length=50)
    status=models.CharField( max_length=50)
    bio=models.TextField()
    image=models.ImageField(upload_to='media/staff',blank=True)


    def __str__(self):
        return self.name