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


@app.route('/')
def index():
    return flask.render_template("index.html")
    
app.run(
     debug= True,
      port=int(os.getenv('PORT',8080)),
      host= os.getenv('IP','0.0.0.0')
    )
