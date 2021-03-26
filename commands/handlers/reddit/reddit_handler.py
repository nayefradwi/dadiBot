import praw
import random
import os
# env variables
client_id = os.getenv('client_id')
client_secret = os.getenv('client_secret')
username = os.getenv('username')
password = os.getenv('password')
user_agent = os.getenv('user_agent')


class RedditHandler():
    def __init__(self):
        self.reddit = praw.Reddit(client_id=client_id,
                                  client_secret=client_secret,
                                  user_agent=user_agent)

    def get_random_from_subreddit(self, sub):
        submissions = sub.hot()
        post_to_pick = random.randint(1, 50)
        for i in range(0, post_to_pick):
            submission = next(x for x in submissions if not x.stickied)
        return submission.url

    def getFromSub(self, subname):
        sub = self.reddit.subreddit(subname)
        return self.get_random_from_subreddit(sub)

    async def get_seal(self):
        try:
            url = self.getFromSub("seals")
            return url
        except Exception as e:
            print(e)
            return "im sorry i failed to amuse you"

    async def get_meme(self):
        try:
            url = self.getFromSub("memes")
            return url
        except Exception as e:
            print(e)
            return "im sorry i failed to amuse you"
