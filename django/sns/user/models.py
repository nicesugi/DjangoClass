#user/models.py
from django.db import models


# Create your models here.
class UserModel(models.Model): # admin에서 클래스가 호출 당한 뒤, admin에 넣어짐 > admin에 넣을 클래스 = 데이터베이스에 넣을 클래스
    class Meta:
        db_table = "my_user" # 테이블 이름은 my_user로, 데이터베이스 정보는 클래스 Meta 에 적어줌.

    username = models.CharField(max_length=20, null=False) # CharField : 클래스 상세내용은 init.py에서 확인
    password = models.CharField(max_length=256, null=False)
    bio = models.CharField(max_length=256, default='')
    created_at = models.DateTimeField(auto_now_add=True) # DateTimeField : 클래스 상세내용은 init.py에서 확인
    updated_at = models.DateTimeField(auto_now=True)