from bot_lib import Bot_action
from data import *

sohag_token = "6330074336:AAGMMabZRDwm7wg1SEEs4JZUeRNep0Juz94"
asu_token = "6387194055:AAHiHtmkG7VQLePOKQ7FCvOb4D6xQiP2npg"
test_token = '5766065005:AAGol_9ingrt1Lw3HWgxd8cII6vkpkQAHpk'
sohag_bot = Bot_action(sohag_token)
asu_bot = Bot_action(asu_token)
test_bot = Bot_action(test_token)


# a  = test_bot.sendPoll(main_group_id,'ولد ام بنت\nنشوف مين اكتر',['ولد','بنت'])
# print(a['message_id'], a['poll']['poll_id'])
# print(a)


with open('test.json', 'r') as a:
    chat_ids = json.loads(a.read())

for chat_id in chat_ids:
    text = f'عفوا الرجاء الاشتراك بهذه القناة وذلك ليتم التواصل معنا بسهولة وحل المشكلات التي تواجهكم وابداء ارائكم عن البوت\nعلما بانه يمكنك الخروج منها متي شئت ولكن يجب الدخول لها ولو لمرة واحده وذلك لضمان جودة الخدمة\n\n{link_saraha_channel}\nبعد الاشتراك بالقناة يمكنك تصفح البوت بدون اي مشاكل\nشكرا لكم'
    try:
        sohag_bot.sendMessage(chat_id,text)
    except:
        print(chat_id)


