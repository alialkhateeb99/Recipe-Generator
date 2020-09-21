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
- If on Cloud9, preview templates/index.html. This should successfully render the HTML!

## Technical Issues

- Had a problem where the same tweets was being fetched every time  the program was ran.
 This was because the code for fetching tweets was statically placed above the index function
which is supposed to run everytime the website is refreshed. By placing it inside the index function
i am guranteed to get different a new batch of tweets everytime.

 - Had a problem where the python compiler will give me an error indicating that the 'KEY'
 token was invalid. The solution to this is to source the twitterkeys.env with the below 
below command every time you start your enviroment.
 
     ``` source twitterkeys.env ```

## Known Issues
- The application still requires you to source the env files before running the python
file for the first time everytime you start your enviroment.
- Application still uses hard coded food names instead of being dynamic, or being inputted
 by the user.
- Application is still being hosted locally, and has not been deployed anywhere.

    




