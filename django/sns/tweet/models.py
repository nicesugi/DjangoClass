# tweet/models.py
from django.db import models
from user.models import UserModel


# Create your models here.
class TweetModel(models.Model): # admin에서 클래스가 호출 당한 뒤, admin에 넣어짐 > admin에 넣을 클래스 = 데이터베이스에 넣을 클래스
    class Meta:
        db_table = "tweet" # 테이블 이름은 tweet로, 데이터베이스 정보는 클래스 Meta 에 적어줌.

    author = models.ForeignKey(UserModel, on_delete=models.CASCADE) # ForeignKey(to , on_delete , **options)
    content = models.CharField(max_length=256) # CharField : 클래스 상세내용은 init.py에서 확인
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True) # DateTimeField : 클래스 상세내용은 init.py에서 확인



class TweetComment(models.Model):
    class Meta:
        db_table = "comment"
    tweet = models.ForeignKey(TweetModel, on_delete=models.CASCADE)
    author = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    comment = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)