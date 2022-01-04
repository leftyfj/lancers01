from myAuth import api
screen_name="gwall59" #リスト作成者の@~~の~~
listname="api_test" #リストの名前
# api.destroy_list(owner_screen_name=screen_name,slug=listname)  #slug...リスト名が日本語のときは注意*1
api.create_list(name="作りたいリストの名前",mode="public",description="説明") #modeは、"public"か"private"で公開、非公開を選べる