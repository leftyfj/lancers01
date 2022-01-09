import tweepy
import json
import pandas as pd
import os
import datetime
from apikeys import *
import common.authentication as authentication
import time

def set_new_list(list_name, list_desc):
  api = authentication.auth_twitter_api()
  # list_name = input('リスト名 ==>')
  # list_desc = input('リスト内容の説明 ==>')
  list_mode = 'public'
  
  list_detail = api.create_list(name=list_name, mode=list_mode, description = list_desc)
  
  return list_detail

def add_users_to_list(list_id):
  api = authentication.auth_twitter_api()
  filename = 'addlist.csv'
  SEARCH_FILE_PATH = f'./addlist/' + filename
  df = pd.read_csv(SEARCH_FILE_PATH,header=None,usecols=[0])
  screen_name_list = df[0].tolist()
  print(screen_name_list)
 
  for screen_name in screen_name_list:
    try:
      api.add_list_member(list_id = list_id, screen_name = screen_name)
      time.sleep(2)
    except Exception as e:
      print(e)
      print('リストできないユーザーが見つかりました。スキップします。')
    finally:
      print('リスト化終了')
      
def main():
  api = authentication.auth_twitter_api()
  # add_users_to_list(api)
  
if __name__ == "__main__":
    main()