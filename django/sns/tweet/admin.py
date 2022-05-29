from django.contrib import admin
from .models import TweetModel # 현재위치와 동일하게 있는 models.py 에서 TweetModel(클래스)을 불러옴

# Register your models here.
admin.site.register(TweetModel) # 불 러 온 TweetModel(클래스)를 관리자 계정에 넣음