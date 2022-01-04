import tweepy
import json
import pandas as pd

consumer_key = 'OmNT5TYykQxIW3C7i2J9GTeYW'
consumer_secret = 'ZFBnEU3vXPjMHVBCM9z3gnq6S4LXjjrs1iglqQ4kqv7mzWKrFQ'
access_token = '43001713-KC7jJ4dWUXxEQdk9qV85nechj6y4CqiZqYUxE9PAz'
access_token_secret = 'yPhqB80AYgMOAAyyPypKriwaAT4z0kypghkchwnsjGseD'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth ,wait_on_rate_limit = True)

followers = tweepy.Cursor(api.followers, screen_name='gwall59').items()

df = pd.DataFrame(columns = ["name", "screen_name", "id"])

for follower in followers:
          df = df.append(
            {"name": follower.name,
            "screen_name": follower.screen_name,
            "id": follower.id},
            ignore_index=True,
            )
print(df.head())