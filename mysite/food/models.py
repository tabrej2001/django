from pyexpat import model
from django.db import models

# Create your models here.

class Item(models.Model):
    
    def __str__(self):
        return self.item_name
    
    item_name=models.CharField(max_length=200)
    item_desc=models.CharField(max_length=200)
    item_price=models.IntegerField()
    item_image=models.CharField(max_length=500,default="https://c8.alamy.com/comp/B3C2XG/taking-a-slice-of-pizza-B3C2XG.jpg")