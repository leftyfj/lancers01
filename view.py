import eel
import apps.search as search
import apps.upload as upload
import common.authentication as authentication
import pandas as pd
import common.util as util
import common.desktop as desktop

#フォルダ名
app_name = "web"
end_point = "index.html"
size = size=(900, 600)


@eel.expose
def text_function(str):
  print(str)

# @eel.expose
# def test(str):
#   tw_search_twitter_by_keyword.import_test(str)

@eel.expose
def search_tweet(keyword):
  search.search_tweet_by_keyword(keyword)
  
@eel.expose
def search_users(keyword):
  search.search_profile_by_keyword(keyword)


@eel.expose
def get_lists_all(screen_name):
  df = search.get_lists_all(screen_name)
  util.save_csvfile('list_all_', screen_name, df, 'lists')
  
@eel.expose
def upload_users(list_id):
  upload.add_users_to_list(list_id)
  
@eel.expose
def make_new_list(list_name, list_desc):
  upload.set_new_list(list_name, list_desc)

  
def main():
  desktop.start(app_name,end_point,size)
  
  
if __name__ == "__main__":
    main()