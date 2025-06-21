from django.shortcuts import render
from .models import Tweet
from .forms import TweetForm
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
# Create your views here.

def index(request):
    """
    Render the index page.
    """
    return render(request, 'index.html')


def tweet_list(request):
    """
    Display a list of tweets.
    """
    tweets = Tweet.objects.all().order_by('-created_at')
   
    return render(request, 'tweet_list.html', {'tweets': tweets})


def tweet_create(request):
    """
    Handle the creation of a new tweet.
    """
    if request.method == 'POST':
        form = TweetForm(request.POST, request.FILES)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return HttpResponseRedirect('tweet_list')
    else:
        form = TweetForm()
    
    return render(request, 'tweet_form.html', {'form': form})



def tweet_edit(request,tweet_id):
    """
    Handle the editing of an existing tweet.
    """
    tweet = get_object_or_404(Tweet, id=tweet_id, user=request.user)
    
    if request.method == 'POST':
        form = TweetForm(request.POST, request.FILES, instance=tweet)
        if form.is_valid():
            form.save(commit=False)
            tweet.user = request.user   
            tweet.save()
            return HttpResponseRedirect('tweet_list')
    else:
        form = TweetForm(instance=tweet)
    
    return render(request, 'tweet_form.html', {'form': form})


def tweet_delete(request,tweet_id):
    tweet = get_object_or_404(Tweet, id=tweet_id, user=request.user)

    if request.method == 'POST':
        tweet.delete()
        return HttpResponseRedirect('tweet_list')
    return render(request, 'tweet_confirm_delete.html', {'tweet': tweet})
