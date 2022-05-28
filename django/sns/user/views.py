# user의 urls.py에 연결 할 user앱의 views.py 작성하기
from django.shortcuts import render, redirect
from .models import UserModel


def sign_up_view(request):
    if request.method == 'GET':
        return render(request, 'user/signup.html')
    elif request.method == 'POST':
        username = request.POST.get('username', None) # 입력되는 'username'의 정보는 username의 변수로 저장 (없다면 none 처리)
        password = request.POST.get('password', None)
        password2 = request.POST.get('password2', None)
        bio = request.POST.get('bio', None) 

        if password != password2: # 입력되는 password와 재확인하는 password2 값이 다르다면,
            return render(request, 'user/signup.html')
        else:
            new_user = UserModel() # new_user 변수명으로 UserModel(클래스)를 가져옴 > 테이블 이름은 my_user로, 데이터베이스 정보는 클래스 Meta 에 적어줌.
            new_user.username = username 
            new_user.password = password 
            new_user.bio = bio # 지금까지의 코드에서 UserModel은 admin에'만' 저장이 되어서
            new_user.save() # 데이터베이스에도 저장을 해 줌.
        return redirect('/sign-in')

def sign_in_view(request):
    return render(request, 'user/signin.html')