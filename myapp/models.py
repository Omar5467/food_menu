from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.


class item(models.Model):
    def __str__(self):
        return self.item_name
    
    def get_absolute_url(self):
        return reverse('myapp:index')
    user_name = models.ForeignKey(User,on_delete=models.CASCADE,default=2)
    item_name = models.CharField(max_length=20)
    item_price = models.FloatField(max_length=10)
    item_desc = models.TextField(max_length=50)
    item_image = models.CharField(max_length=500,default='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRPSa35DdV7zBu1GZnX78dUWbnG3dxMo9GfbQ&s')
