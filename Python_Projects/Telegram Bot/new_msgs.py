from bot_lib import bot
from data import *


# a = bot.sendPoll(main_group_id,"نشوف مين اكتر\nولد ام بنت؟",['ولد','بنت'])

# channel_id = 0
# a = bot.promoteChatMember(channel_id,master_id)
# a = bot.sendMessage(main_group_id,"flamingo5")['message_id']
# a = bot.sendMessage(main_group_id,'Hello')

1-12000+19937 - (1-13895+13900) - (1-15506+15605) - (1-15806+15906) - (1+17106-17106) - (1+17407-17407) - (1-17707+17708) - (1-17710+17911)


def get_old_msg_id(old_msg_id):
    x = old_msg_id
    if old_msg_id in range(12000, 12621):  # 1 checked
        return 1943+(-12000+x), x+1 
        
        #12621

    elif old_msg_id in range(12621, 13895):  # 2 checked
        return 1943+(-12000+x) +1 , x+1

    elif old_msg_id in range(13895, 15500):  # 2 checked
        return 1943+(-12000+x) , x+6

    elif old_msg_id in range(15500, 15700):  # 3 checked
        return 1943+(-12000+x), x+6+100

    elif old_msg_id in range(15700, 16899):  # 4 checked
        return 1943+(-12000+x), x+6+100+101

    elif old_msg_id in range(16899, 17199):  # 5 checked
        return 1943+(-12000+x), x+6+100+101+1

    elif old_msg_id == 17199:  # 6 checked
        return 1943+(-12000+x), 19938

    elif old_msg_id in range(17200, 17499):  # 7 checked
        return 1943+(-12000+x), x+6+100+101+1

    elif old_msg_id == 17499:  # 8 checked
        return 1943+(-12000+x), x+6+100+101+1+2

    elif old_msg_id in range(17500, 18000):  # 9 checked
        return 1943+(-12000+x), x+6+100+101+1+2+202

    elif old_msg_id in range(18000, 18566):  # 10 checked
        return 1943+(-12000+x)+100, x+6+100+101+1+2+202

    elif old_msg_id in range(18566, 18645):  # 11
        return 1943+(-12000+x)+100 + 1, x+6+100+101+1+2+202

    elif old_msg_id in range(18645, 19526):  # 12
        return 1943+(-12000+x)+100 + 2, x+6+100+101+1+2+202

    elif old_msg_id == 19526:  # 12
        return 0, x+6+100+101+1+2+202

    elif old_msg_id in range(19527, 19627):  # 13
        return 7943+x-19527, x+6+100+101+1+2+202


# x = 15499
# print()  # 13895:15499
# x = 15699
# print()  # 15500:15699
# x = 16898
# print()  # 15700:16898
# x = 17198
# print()  # 16899:17198
# x = 17199
# print()  # 17199
# x = 17498
# print()  # 17200:17498
# x = 17500
# print()  # 17499
# x = 17999
# print()  # 17500:17999
(18559+18571)/2
url = "https://t.me/c/1520098399/{}".format

xx = [
    12000,
    13895,
    15500,
    15700,
    16899,
    17199,
    17200,
    17499,
    17500,
    18000,
    18566,
    18645,
    19525,
    19527,
    19627,
    19626,
    19557]

# xx = [12621]
# c = 0
# for x in xx:
#     c += 1
#     b, a = get_old_msg_id(x)
#     bot.sendMessage(master_id, f"num ({c})\n{url(a)}\n{url(b)}")

# 12621-1


dic = {}
for new_msg_id in range(12000, 19627):
    old_msg_id2, exact_new_msg = get_old_msg_id(new_msg_id)
    dic[str(old_msg_id2)] = exact_new_msg

Files_actions().write_json('bot/new_msg_ids.json', dic)
# def get_new_msg_id(old_msg_id):
