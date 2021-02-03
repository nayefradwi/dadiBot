import praw
import random
import os

# env variables
client_id = os.getenv('client_id')
client_secret = os.getenv('client_secret')
username = os.getenv('username')
password = os.getenv('password')
user_agent = os.getenv('user_agent')



reddit = praw.Reddit(client_id=client_id,
                     client_secret=client_secret,
                     username=username,
                     password=password,
                     user_agent=user_agent)

async def get_seal():
    memes_submissions = reddit.subreddit('seals').random()
    print(memes_submissions)
    return memes_submissions