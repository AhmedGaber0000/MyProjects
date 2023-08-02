import json
with open('database.json', 'r') as a:
    string = a.read()

file = json.loads(string)

# has_enter = file['has_enter']
users = file['users']
# log = file['log']

approved_users = []
for chat_id in users:
    user = users[chat_id]
    if user['is_approved'] :
        approved_users.append(chat_id)

# # traffic = {
# #     "a":1
# # }
# # chat_ids = {}
# # for log_it in log:
# #     time = log_it[0]
# #     chat_id = log_it[1]
# #     pos = log_it[2][0]
# #     button_name = log_it[2][1]
# #     name = button_name+" "+pos
# #     if name in traffic:
# #         if chat_id not in chat_ids[name]:
# #             chat_ids[name].append(chat_id)
# #             traffic[name] += 1
# #     else:
# #         chat_ids[name] = [chat_id]
# #         traffic[name] = 1

# # # traffic
# # # a = sorted(traffic,key=)
# # # f = []
# # # for i in a:
# # #     f.append(traffic[i])
# # def fun(item):
# #     return int(item[1])

# # sorted = sorted(traffic.items(),key=fun, reverse=True)


with open('test.json', 'w') as a:
    a.write(json.dumps(approved_users, indent=4, ensure_ascii=False))


