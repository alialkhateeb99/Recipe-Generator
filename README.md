# Recipes and Tweets app

## Pre-Requisites 

- Python 3.6+
- Git
- Pip/Pip3
- Tweepy
- python-dotenv
- Twitter Developer Account

## Cloning repository 

- Add a new folder under your userhome directory 
- Run the below command 
    - ``` git clone https://github.com/NJIT-CS490/project1-aaa332 ```

## Apply for a Twitter Developer Account

- For more information:  https://developer.twitter.com/en/apply-for-access
- Here you will get your API keys and tokens after approval.

## Installation

 Run the following commands:
 
 - Tweepy:
 
    ([sudo] pip[3] install tweepy)
    
- Flask:

    ([sudo] pip[3] install flask)
    
- python-dotenv

    ([sudo] pip[3] install python-dotenv)
    
## Twitter API keys and tokens

- Make a root level file called twitterkeys.env and populate it as follows:

    KEY=''
    
    KEY_SECRET=''
    
    TOKEN=''
    
    TOKEN_SECRET=''
    
- Then appropriately fill in the correct keys.


## Build and Run

- Run  ``` python main.py ``` in your enviroment.
- If on Cloud9, preview templates/index.html. This should successfully render the HTML.

## Deploying to Heroku

 Sign up for heroku at heroku.com
 
- Install heroku in the CLI by running ``` npm install -g heroku ```
- Make two files ``` requirements.txt ``` and ``` Procfile ``` named exactly as shown.
- In the ``` requirements.txt ``` add ``` tweepy ``` ``` flask ``` ``` python-dotenv ``` each on a seperate new line.
- In the ``` Procfile ``` add ``` web: python main.py ```
 
Run the following commands:
- ``` nvm i v8 ```
- ``` heroku login -i ```
-  ``` heroku create ```
-  ``` git push heroku master ```

Navigate to https://dashboard.heroku.com/apps and add your keys to the config vars.


## Technical Issues

### v1

- Had a problem where the same tweets was being fetched every time  the program was ran.
 This was because the code for fetching tweets was statically placed above the index function
which is supposed to run everytime the website is refreshed. By placing it inside the index function
i am guranteed to get different a new batch of tweets everytime.

 - Had a problem where the python compiler will give me an error indicating that the 'KEY'
 token was invalid. The solution to this is to source the twitterkeys.env with the below 
below command every time you start your enviroment. 

``` source twitterkeys.env ```


### v2
- Had an issue where the API wouldn't load some images and it 
would throw an error message in jinja. Fixed this issue by checking
if it received an image url in the json object and appropriately handle
it in the html side using flask.
- ( The issue with having to source env files was fixed in the v2 of the application.
It now uses the python-dotenv module to automatically source the files.) 

 

## Known Issues

- The application still requires you to source the env files before running the python
file for the first time everytime you start your enviroment.
- Application still uses hard coded food names instead of being dynamic, or being inputted
 by the user.
- Application is still being hosted locally, and has not been deployed anywhere.


- 

    
### v2 new features

- Application is now hosted on heroku and is visible to any user.
- Uses spoonacular API to fetch details about the food recipes.
- Application has been redesigned with new styling designs.


