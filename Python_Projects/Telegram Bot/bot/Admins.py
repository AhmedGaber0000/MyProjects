from user import *


class Admins:
    def __init__(self, chat_id) -> None:
        self.user = User(chat_id)
        self.chat_id = str(chat_id)
        self.keyboards = self.user.keyboards

    @property
    def __Data(self):
        x = db.Data['admins']
        if self.chat_id in x:
            return x[self.chat_id]
        return {}

    @property
    def pos(self):
        return self.user.pos

    def add_self_pos(self):
        parameters = self.get_sub_pos_pin(self.pos)
        if parameters:
            sub = parameters[0]
            db.add_pos_to_sub(self.chat_id, sub, self.pos)

    @property
    def channel_id(self):
        return self.__Data['channel_id']

    @property
    def channel_url(self):
        return self.__Data['channel_url']

    @property
    def add_mat_parameters(self):
        x = self.__Data['add_mat_parameters']
        db.empty_mat_parameter(self.chat_id)
        return x

    @property
    def get_event(self):
        return self.__Data['event']

    def set_event(self, event):
        db.set_event(self.chat_id, event)

    @property
    def is_change_request(self):
        a = self.is_admin
        b = self.get_change_request
        return a and b

    @property
    def get_change_request(self):
        x = self.__Data
        if 'change_request' in x:
            return x['change_request']
        return False

    def set_change_request(self, req):
        db.set_change_request(self.chat_id, req)

    @property
    def is_admin(self):
        return self.chat_id in self.admins_chat_ids

    def get_sub_pos_pin(self, pos):
        subjects = self.__Data['subjects']
        for sub in subjects:
            if pos in subjects[sub]['postions']:
                return sub, subjects[sub]['sub_pos'], subjects[sub]['pin_msg_id']
        return []

    def set_add_mat_parameters(self, parameters):
        db.set_add_mat_parameters(self.chat_id, parameters)

    @property
    def is_admin_area(self):
        postions = []
        subs = self.__Data['subjects']
        for sub in subs:
            postions += subs[sub]['postions']

        parameters = self.get_sub_pos_pin(self.pos)
        self.set_add_mat_parameters(parameters)

        if self.pos in postions:
            return True

        if str(self.chat_id) == master_id:
            return True
        return False

    @property
    def admins_chat_ids(self):
        return list(db.Data['admins'])
