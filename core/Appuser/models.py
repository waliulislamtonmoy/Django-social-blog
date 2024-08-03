from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    image=models.ImageField( upload_to='profile/',blank=True,null=True)
    phone=models.CharField( max_length=15,blank=True,null=True)
    address=models.TextField(blank=True,null=True)
    description=models.TextField(blank=True,null=True)
    
    
    