from django.shortcuts import render, redirect
from django.http import HttpResponse
from bs4 import BeautifulSoup
import requests
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from mainApp.models import twitterLinks
# Create your views here.

def index(request):
    return render(
        request,
        './index.html'
    )
def data(request):
    username = None
    if request.user.is_authenticated:
        username = request.user
        userid = request.user.id
    all_tweets = twitterLinks.objects.filter(user = userid)
    date = []
    name = []
    link = []
    retweet = []
    like = []
    tweet = []
    try:
        for number in range(len(all_tweets)):
            date.append(all_tweets[number].post_date)
            name.append(all_tweets[number].influencer)
            link.append(all_tweets[number].tweeturl)
            retweet.append(all_tweets[number].retweets)
            like.append(all_tweets[number].likes)
            tweet.append(all_tweets[number].quote)
    except:
        print("nothing found")
    zipped = zip(date, name, link, retweet, like, tweet)
    return render(
        request,
        './data.html',
        context={'info':zipped}
    )

def search(request):
    username = None
    if request.user.is_authenticated:
        username = request.user
        userid = request.user.id
        try:
            to_remove = twitterLinks.objects.filter(user = userid)
            to_remove.delete()
        except:
            print("No tweets deleted")
    if 'q' in request.GET:
        parse = request.GET['q']
        sort = parse.split("https")
        num = len(sort)
        links = ""
        names = ""
        like = 0
        retweet = 0
        tweets = ""
        date = ""
        for link in range(1, num):
            url = "https"
            try:
                url += sort[link]
                # req = urlreq.urlopen(url)
                url = url[:len(url) - 2]
                link = url
                req = requests.get(url, verify=False)
                soup = BeautifulSoup(req.content)
                name = soup.find_all("span", {"class": "username"})
                name = name[4].text.strip()
                name = name[1:]

                tweet = soup.find_all("p", {"class": "TweetTextSize--jumbo"})
                tweet = tweet[0].text.strip()

                try:
                    retweets = soup.find_all("a", {"class": "request-retweeted-popup"})
                    retweets = retweets[0].text.strip()
                    retweets = retweets.split(" ")
                    retweets = retweets[0]
                    retweet = int(retweets.replace(",", ""))
                except:
                    retweet = 0

                try:
                    likes = soup.find_all("a", {"class": "request-favorited-popup"})
                    likes = likes[0].text.strip()
                    likes = likes.split(" ")
                    likes = likes[0]
                    like = int(likes.replace(",", ""))
                except:
                    like = 0

                timestamp = soup.find_all("span", {"class": "metadata"})
                timestamp = timestamp[0].text.strip()
                timestamp = timestamp.split("- ")
                timestamp = timestamp[1]
                try:
                    timestamp = timestamp.split("from")
                    timestamp = timestamp[0].strip()
                except:
                    timestamp = timestamp
            except:
                names = ""
                like = 0
                retweet = 0
                tweet = ""
                timestamp = ""
            tweetInfo = twitterLinks(post_date=timestamp,influencer=name,tweeturl=link,retweets=retweet,likes=like,quote=tweet, user=username )
            tweetInfo.save()
    else:
        message = 'You submitted an empty form.'
        return HttpResponse(message)
    return render(
        request,
        './index.html',
        context={'submitted':True}
    )

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})
