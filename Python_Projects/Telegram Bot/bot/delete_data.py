from bot_lib import *


msgs = db.Data['delete']
for msg in msgs:
    chat_id , msg_id = msg
    print(chat_id, msg_id)
    try:
        bot.deleteMessage((chat_id,msg_id))
    except:
        pass

db.empty_delete_msgs()