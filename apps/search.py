import tweepy
import json
import pandas as pd
import os
import datetime
import traceback
import time

from common.apikeys import *
import common.authentication as authentication
import common.util as util
import common.config as config


#キーワードをつぶやいた人を検索する
#1000人を検索、重複を省き残りをcsvファイルの保存する
def search_tweet_by_keyword(keyword):
  api = authentication.auth_twitter_api()
  
  try:
    tweets = tweepy.Cursor(api.search,q=keyword,lang='ja').items(config.MAX_ITEMS)
    #検索データを格納する仮のリスト
    temp_list = []
    #検索データを仮のリストへ格納
    for tweet in tweets:
      temp_list.append([tweet.user.screen_name,tweet.user.id,tweet.user.name])
  except:
    print('エラー発生。52ページ超え')
  finally:
      print("-処理終了-")
      
  #DataFrameへ変換
  cols=config.cols
  df =pd.DataFrame(temp_list, columns=cols)

  #重複してツイートしている人を削除
  df = df.drop_duplicates(subset=['id'])
  
  return df, 'True'
  # util.save_csvfile('users_', keyword, df, 'search')
  
  
def search_profile_by_keyword(keyword):
  api = authentication.auth_twitter_api()
  
  temp_list = []
  try:
    users = tweepy.Cursor(api.search_users, q=keyword).items(config.MAX_ITEMS)
    for user in users:
      user = user._json
      print(user['id'])
      temp_list.append([user['screen_name'],user['id'],user['name']])
      
  except:   
    print('エラー')
    print(traceback.format_exc())
  finally:
    print("-処理終了-")

  cols=config.cols
  df =pd.DataFrame(temp_list, columns=cols)
  df = df.drop_duplicates(subset=['id'])
  
  util.save_csvfile('users_profile_', keyword, df, 'search')
  
def get_list_id(list_detail):
  list_id = list_detail._json['id']
  return list_id

def get_lists_all(screen_name):
  api = authentication.auth_twitter_api()
  temp_list = []
  for twilist in (api.lists_all(screen_name = screen_name)):
    #print(twilist._json)
    list_detail = twilist._json
    temp_list.append([list_detail['screen_name'],list_detail['id'],list_detail['name'],list_detail['description']])
    
  cols = config.cols_desc
  df = pd.DataFrame(temp_list, columns=cols)
  
  return df  
  

def search_follower(screen_name):
  api = authentication.auth_twitter_api()
  
  #items数をオーバーしたときの処理をする
  followers = tweepy.Cursor(api.followers, screen_name = screen_name).items()
  df = pd.DataFrame(columns =config.cols)
  return df
