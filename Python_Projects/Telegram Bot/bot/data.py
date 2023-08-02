from const_file import *

token = "5766065005:AAGol_9ingrt1Lw3HWgxd8cII6vkpkQAHpk"
url = "https://2e17-102-43-73-159.ngrok-free.app"
main_poll_id = 20190
main_poll_id_num = "5919987254981296497"
privacy_msg_id = 20094
rm_approve_fun = False
rm_alarm_msg = False
def save_update(id, string):
    with open(f'bot/updates/{1000000000000-id}.json', 'w') as a:
        a.write(string)
