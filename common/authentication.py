# from typing import Annotated, ClassVar
from common.apikeys import *
import tweepy

global CK
global CS
global AT
global ATS

CK = consumer_key
CS = consumer_secret
AT = access_token
ATS = access_token_secret

# 認証手続き
def auth_twitter_api():
    auth = tweepy.OAuthHandler(CK, CS)
    auth.set_access_token(AT, ATS)
    api = tweepy.API(auth,wait_on_rate_limit=True)
    
    return api


# if __name__ == "__main__":
#   auth_twitter_api(consumer_key,consumer_secret,access_token,access_token_secret)