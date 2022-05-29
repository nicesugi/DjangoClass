# tweet/urls.py
from django.urls import path
from . import views
# sns.urls에서 작성된 [path('', include('tweet.urls'))] 코드로 이 곳에서 작성되는 모든 url은 sns.urls와 연결됨
urlpatterns = [ # 작성한 views.py 를 urls.py에 연결 해 주기
    path('', views.home, name='home'), # 127.0.0.1:8000 과 views.py 폴더의 home 함수 연결
    path('tweet/', views.tweet, name='tweet') # 127.0.0.1:8000/tweet 과 views.py 폴더의 tweet 함수 연결
]
