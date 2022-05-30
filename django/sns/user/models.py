#user/models.py
from configparser import MAX_INTERPOLATION_DEPTH
from django.db import models
from django.contrib.auth.models import AbstractUser 
from django.conf import settings #from sns import settings 불러와도 되지만 하나하나 가져오기보다 장고에서 가져올 수 있게끔 임포트를 해줌.


class UserModel(AbstractUser): 
    class Meta:
        db_table = "my_user" 
        
    bio = models.CharField(max_length=256, default='')
    follow = models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='followee')
    # manytomany 관계의 데이터 : 임포트된 장고 세팅에서 AUTH_USER_MODE(=class UserModel)를 (참조)불러옵니다. 
    # follow 필드 안에 들어가는 정보들은 사용자 정보라는 뜻으로 