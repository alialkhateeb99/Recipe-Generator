import flask
import tweepy
import os
import random
from tweepy import Cursor
import requests
from os.path import join, dirname
from dotenv import load_dotenv
import json

dotenv_path = join(dirname(__file__), 'spoonacularkeys.env')
load_dotenv(dotenv_path)

dotenv_path2 = join(dirname(__file__), 'twitterkeys.env')
load_dotenv(dotenv_path2)

twitter_consumer_key = os.environ['KEY']
twitter_consumer_secret = os.environ['KEY_SECRET']
twitter_access_token = os.environ['TOKEN']
twitter_access_token_secret = os.environ['TOKEN_SECRET']

spoonacular_key = os.environ['SPOONACULAR_KEY']



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
    numberOfItems = 3
    randomfoodname = random.choice(food)
    fetch_id_url   = "https://api.spoonacular.com/recipes/complexSearch?query={}&number={}&apiKey={}".format(randomfoodname,numberOfItems,spoonacular_key)
    
    response  = requests.get(fetch_id_url)
    json_body = response.json()
    
    id_to_fetch = json_body["results"][random.randint(0,numberOfItems-1)]["id"]
    
    fetch_food_information_url = "https://api.spoonacular.com/recipes/{}/information?&apiKey={}".format(id_to_fetch,spoonacular_key)
    
    response2  = requests.get(fetch_food_information_url)
    json_body2 = response2.json()
    
    food_title      = json_body2["title"]
    food_servings   = json_body2["servings"]
    food_prep_time  = json_body2["readyInMinutes"]
    food_image_url  = json_body2["image"]
    food_source_url = json_body2["sourceUrl"]

    ingredients = []
    for x in json_body2["extendedIngredients"]:
        ingredients.append(x["originalString"])
    ingredients_length = len(ingredients)
    
    tweets = api.search(q=randomfoodname,lang="en",count=5,tweet_mode='extended')
    tweets_list = []
    
    for tweet in tweets:
        tweets_list.append(tweet)

    tweet2 = random.choice(tweets_list)

    tweetcontent = tweet2.full_text
    tweetdate = tweet2.created_at
    tweetauthor = tweet2.user.screen_name
    
    return flask.render_template("index.html",
    foodname=randomfoodname,
    tweet_content=tweetcontent,
    tweet_date=tweetdate,
    tweet_author=tweetauthor,
    foodTitle=food_title,
    foodServings=food_servings,
    foodPrepTime=food_prep_time,
    foodImageUrl=food_image_url,
    foodSourceUrl=food_source_url,
    foodIngredients=ingredients,
    foodIngredientsLength=ingredients_length
    )
    
app.run(
     debug= True,
      port=int(os.getenv('PORT',8080)),
      host= os.getenv('IP','0.0.0.0')
    )

