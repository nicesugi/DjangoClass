# user의 urls.py에 연결 할 user앱의 views.py 작성하기
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import UserModel
from django.contrib.auth import get_user_model #사용자가 있는지 검사하는 함수



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

        me = UserModel.objects.get(username=username)  # 사용자 불러오기
        if me.password == password:  # 저장된 사용자의 패스워드와 입력받은 패스워드 비교
            request.session['user'] = me.username  # 세션에 사용자 이름 저장
            return HttpResponse(me.username) # 로그인 하는 username 브라우저에 표시함
        else: 
            return redirect('/sign-in')
    elif request.method == 'GET':
        return render(request, 'user/signin.html')

