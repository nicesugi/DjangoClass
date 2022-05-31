from django.conf import settings
from django.db import models



class Category(models.Model):
    class Meta:
        db_table = "category"
    name = models.CharField(max_length=256)
    desc = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class Article(models.Model):
    class Meta:
        db_table = "article"
    title = models.CharField(max_length=256)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    content = models.CharField(max_length=256) 
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True) 
    

