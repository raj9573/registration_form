from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django import forms


class RegistrationForm(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    address=models.TextField()
    profile_pic=models.ImageField()

    
