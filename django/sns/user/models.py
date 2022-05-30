#user/models.py
from configparser import MAX_INTERPOLATION_DEPTH
from django.db import models
from django.contrib.auth.models import AbstractUser 
from django.conf import settings



class UserModel(AbstractUser): 
    class Meta:
        db_table = "my_user" 
        
    bio = models.CharField(max_length=256, default='')
    follow = models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='followee')