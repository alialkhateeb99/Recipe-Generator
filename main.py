import flask
import tweepy
import os
import random
from tweepy import Cursor


twitter_consumer_key = os.environ['KEY']
twitter_consumer_secret = os.environ['KEY_SECRET']

twitter_access_token = os.environ['TOKEN']
twitter_access_token_secret = os.environ['TOKEN_SECRET']


auth = tweepy.OAuthHandler(twitter_consumer_key,twitter_consumer_secret)
auth.set_access_token(twitter_access_token,twitter_access_token_secret)

api = tweepy.API(auth)


app = flask.Flask(__name__)

food = ["ice cream","pizza","sushi","ramen","tacos","cheeseburger","mac and cheese","fried chicken","hamburger"]


tweetcontent = ""
tweetauthor  = ""
tweetdate    = ""
    

@app.route('/')
def index():
    tweets = api.search(q=random.choice(food),lang="en",count=100)
    tweets_list = []
    
    for tweet in tweets:
        tweets_list.append(tweet)

    tweet2 = random.choice(tweets_list)
    tweetcontent = tweet2.text
    tweetdate = tweet2.created_at
    tweetauthor = tweet2.user.screen_name
    return flask.render_template("index.html",tweet_content=tweetcontent,tweet_date=tweetdate,tweet_author=tweetauthor)
    
app.run(
     debug= True,
      port=int(os.getenv('PORT',8080)),
      host= os.getenv('IP','0.0.0.0')
    )

