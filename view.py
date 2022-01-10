import eel
import apps.search as search
import apps.upload as upload
import common.authentication as authentication
# import pandas as pd
import common.util as util
import common.desktop as desktop

#フォルダ名
app_name = "web"
end_point = "index.html"
size = size=(1280, 800)


@eel.expose
def text_function(str):
  print(str)


@eel.expose
def search_tweet(keyword):
  res = search.search_tweet_by_keyword(keyword)
  print(res[1])
  df = res[0]
  finish_flag = res[1]
  util.save_csvfile('users_', keyword, df, 'search')
  
  return finish_flag
  
@eel.expose
def search_users(keyword):
  res = search.search_profile_by_keyword(keyword)
  df = res[0]
  finish_flag = res[1]
  util.save_csvfile('users_profile_', keyword, df, 'search')
  
  return finish_flag

@eel.expose
def get_lists_all(screen_name):
  res = search.get_lists_all(screen_name)
  df = res[0]
  finish_flag = res[1]
  util.save_csvfile('list_all_', screen_name, df, 'lists')
  
  return finish_flag
  
@eel.expose
def upload_users(list_id):
  finish_flag  = upload.add_users_to_list(list_id)
  
  return finish_flag
  
@eel.expose
def make_new_list(list_name, list_desc):
  upload.set_new_list(list_name, list_desc)

  
def main():
  desktop.start(app_name,end_point,size)
  
  
if __name__ == "__main__":
    main()