# user의 urls.py에 연결 할 user앱의 views.py 작성하기
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import UserModel
from django.contrib.auth import get_user_model #사용자가 있는지 검사하는 함수
from django.contrib import auth # 사용자 auth 기능
from django.contrib.auth.decorators import login_required

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
        username = request.POST.get('username', '') # 입력되는 'username'의 정보는 username의 변수로 저장 (없다면 none 처리)
        password = request.POST.get('password', '')
        password2 = request.POST.get('password2', '')
        bio = request.POST.get('bio', '') 

        if password != password2: # 입력되는 password와 재확인하는 password2 값이 다르다면,
            return render(request, 'user/signup.html', {'error':'비밀번호를 확인해주세요'})
        else: 
            if username == '' or password == '':
                return render(request, 'user/signup.html', {'error':'사용자의 이름과 비밀번호는 필수입니다'})
            exist_user = get_user_model().objects.filter(username=username) # 데이터베이스에 유저네임을 가진 사용자가 있는지 확인
            if exist_user: 
                return render(request, 'user/signup.html', {'error':'사용자가 존재합니다'})
            else: 
                UserModel.objects.create_user(username=username, password=password, bio=bio)
            return redirect('/sign-in')



def sign_in_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        me = auth.authenticate(request, username=username, password=password)  # authenticate 함수 이용하여 암호화된 비밀번호와 입력한 비밀번호가 일치하고 유저네임도 맞는지 확인가능
        if me is not None:  # 사용자가 있는지 구분만 함 / 왜? 위에서 이미 사용자 정보를 체크해주고 로그인 정보를 들고오기 때문
            auth.login(request, me) # auth.login : 장고 제공되는 로그인 함수 / 로그인 함수에 사용자(me) 정보를 넣어줌
            return redirect('/') # '/' : tweet.urls > views.home > home 함수 > 성공시 트윗페이지
        else: 
            return render(request, 'user/signin.html', {'error':'username 혹은 password를 확인해주세요'})
    elif request.method == 'GET':
        user = request.user.is_authenticated
        # 사용자가 로그인(인증)상태로 sign-up페이지에 접속한다면 트윗페이지로 돌려주고, 인증상태가 아니라면 sign-up페이지 이동
        if user:
            print('로그인상태입니다.로그아웃해주세요.')
            return redirect('/') # tweet.views에 home 함수 기능 때문에 이곳에서는 '/'로 redirect시켜줌
        else:
            return render(request, 'user/signin.html')




@login_required
def logout(request):
    auth.logout(request)
    return redirect('/')

# 장고 logout함수를 이용하여 '/'로 이동시켜줌 
# '/'로 이동하는 이유는 tweet.views에 home 함수에서 자동으로 조건에 맞는 페이지로 이동하기 때문
# home 함수는 tweet or sign-in 로 redirect해줌
# 로그아웃은 로그인만 되어있는 상태에서 가능하기 때문에 임포트해주고 함수에 @ 작성해 적용시켜준다



@login_required
def user_view(request):
    if request.method == 'GET':
        user_list = UserModel.objects.all().exclude(username=request.user.username)
        return render(request, 'user/user_list.html', {'user_list': user_list})
        # username=request.user.(로그인한사용자의)username(username) > '나'를 exclude한 모든 객체 리스트
        # 위의 user_list를 user/user_list.html에서 같이 보여줌
@login_required
def user_follow(request, id):
    me = request.user
    click_user = UserModel.objects.get(id=id) # 눌림당한 유저
    if me in click_user.followee.all(): # 클릭유저 팔로우하는 모든 사람 중에 내가 있으면
        click_user.followee.remove(request.user) # 나를 빼주기
    else:   #클릭유저를 팔로우하는 사람 중에 내가 없다면
        click_user.followee.add(request.user) #나를 더해줌
    return redirect('/user')