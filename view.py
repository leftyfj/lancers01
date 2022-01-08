import eel
import search
import upload
import authentication
import pandas as pd
import common



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
  common.save_csvfile('list_all_', screen_name, df, 'lists')
  
@eel.expose
def upload_users(list_id):
  upload.add_users_to_list(list_id)
  
def main():
  eel.init('web')
  eel.start("index.html", size=(900, 600))

  
  
if __name__ == "__main__":
    main()