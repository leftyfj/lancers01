import datetime
import os

def save_csvfile(prefix, keyword, df, foldername):
  now = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
  filename = prefix + keyword+'_' + now + '.csv'
  path = f'./{foldername}/' + filename
  os.makedirs(os.path.dirname(path), exist_ok=True)
  df.to_csv(path, encoding='utf_8_sig', index=False)