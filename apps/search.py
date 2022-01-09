import tweepy
import json
import pandas as pd
import os
import datetime
import traceback
import time

from apikeys import *
import common.authentication as authentication
import common.util as util


#キーワードをつぶやいた人を検索する
#1000人を検索、重複を省き残りをcsvファイルの保存する
def search_tweet_by_keyword(keyword):
  api = authentication.auth_twitter_api()
  
  try:
    tweets = tweepy.Cursor(api.search,q=keyword,lang='ja').items(1000)
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
  cols=['screen_name','id','name']
  df =pd.DataFrame(temp_list, columns=cols)

  #重複してツイートしている人を削除
  df = df.drop_duplicates(subset=['id'])
  util.save_csvfile('users_', keyword, df, 'search')
  
  
def search_profile_by_keyword(keyword):
  api = authentication.auth_twitter_api()
  
  temp_list = []
  try:
    users = tweepy.Cursor(api.search_users, q=keyword).items(1000)
    for user in users:
      user = user._json
      print(user['id'])
      temp_list.append([user['screen_name'],user['id'],user['name']])
      
  except:   
    print('エラー')
    print(traceback.format_exc())
  finally:
    print("-処理終了-")

  cols=['screen_name','id','name']
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
    print(list_detail['id'], list_detail['name'], list_detail['description'])
    temp_list.append([list_detail['id'], list_detail['name'], list_detail['description']])
    
  cols = ['id','name','description']
  df = pd.DataFrame(temp_list, columns=cols)
  
  return df  
  
  
  
def search_follower():
  pass

# def save_csvfile(prefix, keyword, df, foldername):
#   now = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
#   filename = prefix + keyword+'_' + now + '.csv'
#   #path = f'./search/' + filename
#   path = f'./{foldername}/' + filename
#   os.makedirs(os.path.dirname(path), exist_ok=True)
#   df.to_csv(path, encoding='utf_8_sig', index=False)