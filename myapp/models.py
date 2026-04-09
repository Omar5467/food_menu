from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.


class item(models.Model):
    def __str__(self):
        return self.item_name + ' - ' + str(self.item_price) + ' - ' + self.created_at.strftime('%Y-%m-%d %H:%M:%S')
    
    def get_absolute_url(self):
        return reverse('myapp:index')
    user_name = models.ForeignKey(User,on_delete=models.CASCADE,default=2)
    item_name = models.CharField(max_length=20)
    item_price = models.DecimalField(max_digits=6, decimal_places=2)
    item_desc = models.TextField(max_length=50)
    item_image = models.URLField(max_length=500,default='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRPSa35DdV7zBu1GZnX78dUWbnG3dxMo9GfbQ&s')
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Category(models.Model):
    def __str__(self):
        return self.name
    
    name = models.CharField(max_length=100)
    added_on = models.DateField(auto_now = True)