from email.mime import image
from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from django.forms import CharField
# Create your models here.


class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    image  = models.ImageField(default='profilepic.jpg',upload_to='profile_pictures')
    location=models.CharField(max_length=100)

    def __str__(self):
       return self.user.username

