from .models import TweetModel # 글쓰기 모델 -> 가장 윗부분에 적어주세요!
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
        user = request.user.is_authenticated 
        # 사용자의 로그인(인증)상태를 user라고 함
        if user: # 사용자가 로그인(인증)상태라면
            all_tweet = TweetModel.objects.all().order_by('-created_at')  # TweetModel에 저장한 모든 모델을 저장함 (생성된 시간을 '-'을 붙여 최신순,역순으로 정렬)
            return render(request, 'tweet/home.html',{'tweet':all_tweet}) # 최신순 정렬인 all_tweet을 tweet/home.html 넘겨준다 > 딕셔너리 형태로 ! 키값은 트윗
        else: # 사용자가 로그인(인증)상태가 아니라면
            print('로그인이 안된 상태')
            return redirect('/sign-in')
    elif request.method == 'POST':  
        user = request.user  # 현재 로그인 한 사용자를 불러오기
        my_tweet = TweetModel()  # my_tweet이름으로 TweetModel 가져오기
        my_tweet.author = user  # 모델에 사용자 저장
        my_tweet.content = request.POST.get('my-content', '')  # 모델에 글 저장
        my_tweet.save() 
        return redirect('/tweet')
    
    
   