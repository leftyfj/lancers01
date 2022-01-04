#キーワードをツィートした人を1,000人分検索
#重複した人を省いてDataFrameに格納

import tweepy
import json
import pandas as pd
import os
import datetime
from config import *
import auth

#50ページ×20件 = 1,000件のツイートを検索。　52以上でエラーする。念の為50ページに設定
def search_users_by_keyword(api, keyword):
    users = tweepy.Cursor(api.search_users, q=keyword).pages(5)
    #検索データを格納する仮のリスト
    temp_list = []
    #検索データを仮のリストへ格納
    for users2 in users:
        for user in users2:
            #print(user._json)
            temp_list.append(user._json)
    #DataFrameへ変換
    df =pd.DataFrame(temp_list)
    #DataFrameを必要な項目だけに圧縮
    cols=['name', 'screen_name','id','created_at','description']
    df = df[cols]
    print(f'{keyword}をツイートした人は延べ{len(df)}人いました。')
    #重複してツイートしている人を削除
    df = df.drop_duplicates(subset=['id'])
    df=df.replace('\r\n','')
    print(f'重複を省き{len(df)}人のデータを取得しました。')

    return df

def make_csvfile(df, keyword):
    now = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    filename = 'user_' + keyword+'_' + now + '.csv'
    SEARCH_FILE_PATH = f'./search/' + filename
    os.makedirs(os.path.dirname(SEARCH_FILE_PATH), exist_ok=True)
    df.to_csv(SEARCH_FILE_PATH, encoding='utf_8_sig', index=False)

def main():
    keyword = input('検索キーワード = ')
    api = auth.auth_twitter_api(consumer_key,consumer_secret,access_token,access_token_secret)
    df = search_users_by_keyword(api, keyword)
    make_csvfile(df, keyword)
    
if __name__ == "__main__":
    main()