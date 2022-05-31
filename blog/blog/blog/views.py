from django.shortcuts import redirect
from django.views.generic import ListView, TemplateView


def category(request):
    if request.method =='GET':
        return redirect('/')
    # 에러 >> ERR_TOO_MANY_REDIRECTS ........
    
def article(request):
    return redirect('/new')