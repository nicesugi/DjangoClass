from django.contrib import admin
from .models import UserModel # 현재위치와 동일하게 있는 models.py 에서 UserModel(클래스)을 불러옴

# Register your models here.
admin.site.register(UserModel) # 불 러 온 UserModel(클래스)를 관리자 계정에 넣음