from django.shortcuts import render

# user의 urls.py에 연결 할 user앱의 views.py 작성하기
def sign_up_view(request):
    return render(request, 'user/signup.html')


def sign_in_view(request):
    return render(request, 'user/signin.html')