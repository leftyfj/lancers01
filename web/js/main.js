
async function getKeyword_search_users() {
  let keyword_search_users = document.getElementById('keyword_search_users').value;
  if(keyword_search_users) {
    document.getElementById("searching_users").style.display = "inline-block";
  }

  let finish_flag = await eel.search_tweet(keyword_search_users)();
  
  if(finish_flag == 'True') {
     document.getElementById("searcingh_users").style.display = "none";
  }
 
}

async function getKeyword_search_users_profile() {
  let keyword_search_users_profile = document.getElementById('keyword_search_users_profile').value;

  if(keyword_search_users_profile) {
    document.getElementById("searching_users_profile").style.display = "inline-block";
  }

  let finish_flag = await eel.search_users(keyword_search_users_profile)();

  if(finish_flag == 'True') {
     document.getElementById("searching_users_profile").style.display = "none";
  }

}

async function get_lists_all(){
  let screen_name = document.getElementById('screen_name').value;

  if(screen_name) {
    document.getElementById("getting_lists").style.display = "inline-block";
  }

  let finish_flag = await eel.get_lists_all(screen_name)();

  if(finish_flag == 'True') {
     document.getElementById("getting_lists").style.display = "none";
  }
}

async function upload_users(){
  let list_id = document.getElementById('list_id').value;

  if(list_id) {
    document.getElementById("uploading_users").style.display = "inline-block";
  }

  let finish_flag = await eel.upload_users(list_id)()

  if(finish_flag == 'True') {
     document.getElementById("uploading_users").style.display = "none";
  }

}

async function make_new_list(){
  let new_list_name= document.getElementById('new_list_name').value;
  let new_list_desc= document.getElementById('new_list_desc').value;
  await eel.make_new_list(new_list_name,new_list_desc)
 
}