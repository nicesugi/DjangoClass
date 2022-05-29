from django.shortcuts import render, redirect

# Create your views here.
def home(request):
    user = request.user.is_authenticated # 장고함수 > 사용자가 인증을 받았는지 (로그인이 되어있는지)
    if user:
        return redirect('/tweet') # user.views.sign_in_view 함수 성공 > tweet.urls.name=home > tweet.views 지금 이 코드와 최종적 연결됨
    else:
        return redirect('sign-in')

def tweet(request):
    if request.method =='GET':
        return render(request, 'tweet/home.html')