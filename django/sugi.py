def tweet(request):
    if request.method =='GET':
        user = request.user.is_authenticated 
        if user: 
            all_tweet = TweetModel.objects.all().order_by('-created_at')  
            return render(request, 'tweet/home.html',{'tweet':all_tweet}) 
        else: 
            print('로그인이 안된 상태')
            return redirect('/sign-in')
    elif request.method == 'POST':  
        user = request.user 
        content = request.POST.get('my-content','')
        if content == '':
            all_tweet = TweetModel.objects.all().order_by('-created_at') 
            return render(request, 'tweet/home.html', {'error':'내용을 입력해주세요', 'tweet':all_tweet})
        else:
            my_tweet = TweetModel.objects.create(author=request.user, content=content)
            my_tweet.save()
            return redirect('/tweet')