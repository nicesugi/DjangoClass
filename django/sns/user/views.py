# user의 urls.py에 연결 할 user앱의 views.py 작성하기
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import UserModel
from django.contrib.auth import get_user_model #사용자가 있는지 검사하는 함수
from django.contrib import auth # 사용자 auth 기능

def sign_up_view(request):
    if request.method == 'GET':
        user = request.user.is_authenticated
        # 사용자가 로그인(인증)상태로 sign-up페이지에 접속한다면 트윗페이지로 돌려주고, 인증상태가 아니라면 sign-up페이지 이동
        if user:
            print('로그인상태입니다.로그아웃해주세요.')
            return redirect('/') # tweet.views에 home 함수 기능 때문에 이곳에서는 '/'로 redirect시켜줌
        else:
            return render(request, 'user/signup.html')

    elif request.method == 'POST':
        username = request.POST.get('username', None) # 입력되는 'username'의 정보는 username의 변수로 저장 (없다면 none 처리)
        password = request.POST.get('password', None)
        password2 = request.POST.get('password2', None)
        bio = request.POST.get('bio', None) 

        if password != password2: # 입력되는 password와 재확인하는 password2 값이 다르다면,
            return render(request, 'user/signup.html')
        else: 
            exist_user = get_user_model().objects.filter(username=username) # 데이터베이스에 유저네임을 가진 사용자가 있는지 확인
            if exist_user: 
                print('해당 아이디가 이미 존재합니다')
                return render(request, 'user/signup.html')
            else: 
                UserModel.objects.create_user(username=username, password=password, bio=bio)
                print('신규 가입 성공')
            return redirect('/sign-in')



def sign_in_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)

        me = auth.authenticate(request, username=username, password=password)  # authenticate 함수 이용하여 암호화된 비밀번호와 입력한 비밀번호가 일치하고 유저네임도 맞는지 확인가능
        if me is not None:  # 사용자가 있는지 구분만 함 / 왜? 위에서 이미 사용자 정보를 체크해주고 로그인 정보를 들고오기 때문
            auth.login(request, me) # auth.login : 장고 제공되는 로그인 함수 / 로그인 함수에 사용자(me) 정보를 넣어줌
            print('로그인 성공')
            return redirect('/') # '/' : tweet.urls > views.home > home 함수 > 성공시 트윗페이지
        else: 
            print('로그인 실패')
            return redirect('/sign-in')
    elif request.method == 'GET':
        return render(request, 'user/signin.html')


def sign_in_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)

        me = auth.authenticate(request, username=username, password=password)  
        if me is not None:  
            auth.login(request, me)
            print('로그인 성공')
            return redirect('/') 
        else: 
            print('로그인 실패')
            return redirect('/sign-in')
    elif request.method == 'GET':
        user = request.user.is_authenticated
        # 사용자가 로그인(인증)상태로 sign-up페이지에 접속한다면 트윗페이지로 돌려주고, 인증상태가 아니라면 sign-up페이지 이동
        if user:
            print('로그인상태입니다.로그아웃해주세요.')
            return redirect('/') # tweet.views에 home 함수 기능 때문에 이곳에서는 '/'로 redirect시켜줌
        else:
            return render(request, 'user/signin.html')
