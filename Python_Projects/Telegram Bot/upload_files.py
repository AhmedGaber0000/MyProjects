
from distutils.filelist import findall
import requests

token_sohag = "da34d646ade97bd95194cd75074793b2c08acd51"
user_name_sohag = "djttcote"
user_asu = "djttcote2"
token_asu = "3f341cf4d5104e5ab0b4a8646116a78b516203e1"


def upload_file(file_name, content, user, token, folder="/bot"):
    headers = {'Authorization': f'Token {token}'}
    url = "https://www.pythonanywhere.com/api/v0/user/{user_name}/files/path/home/{user_name}{}/{}".format
    url = url(folder, file_name, user_name=user)
    a = requests.post(url, headers=headers, files={"content": content})
    return a


def reload(user, token):
    headers = {'Authorization': f'Token {token}'}
    url = "https://www.pythonanywhere.com/api/v0/user/{username}/webapps/{domain_name}/reload/".format
    a = requests.post(url(domain_name=f"{user}.pythonanywhere.com", username=user), headers=headers)
    print(a)
    return a


def update_python_files():
    file_names = [
        'bot/keyboards.py',
        'bot/bot_file.py',
        'bot/Update.py',
        'bot/user.py',
        'bot/Admins.py',
        'bot/Messages_text.py',
        'bot/const_file.py',
        'bot/Database.py',
        'bot/delete_data.py',
        'bot/edit_keyboard.py',
        'bot/master.py',
        'bot/pri_msg.py',
        'bot/bot_lib.py',
    ]
    for file_name in file_names:
        with open(file_name, 'r') as a:
            content = a.read()
            sohag = upload_file(file_name, content, user_name_sohag, token_sohag, folder="")
            asu = upload_file(file_name, content, user_asu, token_asu, folder="")
            print(sohag, asu)


def update_sohag_data():
    with open('data_sohag.py', 'r') as a:
        a = upload_file('data.py', a.read(), user_name_sohag, token_sohag)
        print(a)


def update_asu_data():
    with open('data_ASU.py', 'r') as a:
        a = upload_file('data.py', a.read(), user_asu, token_asu)
        print(a)


update_asu_data()
update_sohag_data()
update_python_files()
reload(user_name_sohag, token_sohag)
reload(user_asu, token_asu)
