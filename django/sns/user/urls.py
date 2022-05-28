from django.urls import path
from . import views
# sns.urls에서 작성된 [path('', include('user.urls'))] 코드로 이 곳에서 작성되는 모든 url은 sns.urls와 연결됨
urlpatterns = [ # 작성한 views.py 를 urls.py에 연결 해 주기
    path('sign-up/', views.sign_up_view, name='sign-up'),
    path('sign-in/', views.sign_in_view, name='sign-in'),
]