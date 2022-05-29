#user/models.py
from configparser import MAX_INTERPOLATION_DEPTH
from django.db import models
from django.contrib.auth.models import AbstractUser 


class UserModel(AbstractUser): 
    class Meta:
        db_table = "my_user" 
        
    bio = models.CharField(max_length=256, default='')

   