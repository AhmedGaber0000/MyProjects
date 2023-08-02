import json


class DataBase:

    def __init__(self) -> None:
        with open('bot/DataBase.json', 'r') as a:
            self.__Data = json.loads(a.read())

    @property
    def Data(self):
        return self.__Data

    def user_has_ans_poll(self, chat_id):
        self.__Data['users'][chat_id]['is_ans_poll'] = True

    def approve_user(self, chat_id):
        self.__Data['users'][chat_id]['is_approved'] = True

    def set_pos(self, chat_id, new_pos):
        self.__Data['users'][chat_id]['postion'] = new_pos

    def new_user(self, chat_id, data):
        self.__Data['users'][chat_id] = data
        self.__Data['has_enter'].append(chat_id)

    def add_update(self, request):
        self.__Data['updates'].append(request)

    def add_channel_id(self, channel_name, channel_id):
        self.__Data['channel_ids'][channel_name] = channel_id

    def add_delete_msg_id(self, chat_id, msg_id):
        self.__Data['delete'].append([chat_id, msg_id])

    def add_pos_to_sub(self, chat_id, sub, pos):
        self.__Data['admins'][chat_id]['subjects'][sub]['postions'].append(pos)

    def empty_mat_parameter(self, chat_id):
        self.__Data['admins'][chat_id]['add_mat_parameters'] = []

    def set_event(self, chat_id, event):
        self.__Data['admins'][chat_id]['event'] = event

    def set_change_request(self, chat_id, change_request):
        self.__Data['admins'][chat_id]['change_request'] = change_request

    def set_add_mat_parameters(self, chat_id, parameters):
        self.__Data['admins'][chat_id]['add_mat_parameters'] = parameters

    def add_sub_to_admin(self, chat_id, sub, file):
        self.__Data['admins'][chat_id]['subjects'][sub] = file

    def add_admin(self,chat_id,file):
        self.__Data['admins'][chat_id] = file
        
    def write_keyboards(self,keyboards,keys):
        self.__Data["keyboards"] = keyboards
        self.__Data["keys"] = keys

    def add_map_msg_id(self,group_msg_id, channel_msg_id):
        self.__Data['map_msg_id'][str(group_msg_id)] = channel_msg_id

    def count_write(self,l):
        self.__Data['count'] = l

    def log(self,time, chat_id, event):
        self.__Data['log'].append([time, chat_id, event])

    def empty_delete_msgs(self):
        self.__Data['delete'] = []

    def user_join_saraha(self, chat_id, status):
        self.__Data['users'][chat_id]['is_in_channel'] = status

    def Write_Data(self):
        with open('bot/DataBase.json', 'w') as a:
            a.write(json.dumps(self.__Data, indent=4, ensure_ascii=False))


db = DataBase()
