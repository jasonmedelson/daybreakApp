from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class twitterLinks(models.Model):
    post_date = models.CharField(max_length=20)
    influencer = models.CharField(max_length=50)
    tweeturl = models.CharField(max_length=200)
    retweets = models.IntegerField()
    likes = models.IntegerField()
    quote = models.TextField()
    user = models.ForeignKey(User,on_delete=models.CASCADE,)

