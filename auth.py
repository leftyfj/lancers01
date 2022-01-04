from config import *
import tweepy

# 認証手続き
def auth_twitter_api(consumer_key,consumer_secret,access_token,access_token_secret):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth,wait_on_rate_limit=True)
    
    return api


if __name__ == "__main__":
  auth_twitter_api(consumer_key,consumer_secret,access_token,access_token_secret)