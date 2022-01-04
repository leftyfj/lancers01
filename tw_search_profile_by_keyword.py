#ツイプロAPI　プロフイールから指定したキーワードを検索し、ユーザーの情報を得る

import requests
import os
import json
import pprint
import pandas as pd

TWPRO_URL = 'https://twpro.jp/1/search'
keyword = input('キーワード=')

url_search = TWPRO_URL + '?q=' + keyword + '&num=300'
res = requests.get(url_search)
res =res.json()

df = pd.DataFrame(res['users'])
cols = ['name', 'screen_name','created_at',  'id','description', 'followers_count', 'friends_count',]
df = df[cols]
filename = keyword+'.csv'

SEARCH_FILE_PATH = f'./search/' + filename
os.makedirs(os.path.dirname(SEARCH_FILE_PATH), exist_ok=True)
df.to_csv(SEARCH_FILE_PATH, encoding='utf_8_sig', index=False)