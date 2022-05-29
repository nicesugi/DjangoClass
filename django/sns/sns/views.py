from django.http import HttpResponse # HttpResponse 는 클래스. 
from django.shortcuts import render # render 는 html을 보여주는 역할


def base_response(request):
    return HttpResponse("안녕하세요! 장고의 시작입니다!")

def first_view(request):
    return render(request, 'my_test.html')

# first_view는 my_test.html을 보여주는 함수로, 함수를 만든 후에는 url 연동 필수 ! 같은 위치의 폴더에서 urls.py에서 진행합니다.