
async function getKeyword_search_users() {
  let keyword_search_users = document.getElementById('keyword_search_users').value;

  await eel.search_tweet(keyword_search_users);
}

async function getKeyword_search_users_profile() {
  let keyword_search_users_profile = document.getElementById('keyword_search_users_profile').value;

  await eel.search_users(keyword_search_users_profile);
}

async function get_lists_all(){
  let screen_name = document.getElementById('screen_name').value;
  await eel.get_lists_all(screen_name)
}

async function upload_users(){
  let list_id = document.getElementById('list_id').value;
  await eel.upload_users(list_id)
}