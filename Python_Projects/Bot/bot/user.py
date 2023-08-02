from keyboards import *


class User:
    def __init__(self, chat_id) -> None:
        self.chat_id = str(chat_id)
        self.keyboards = Keyboards()
    
    
    @property
    def __data(self):
        return db.Data['users'][self.chat_id]

    @property
    def is_in_channel(self):
        if 'is_in_channel' in self.__data:
            is_in_channel = self.__data['is_in_channel']
        else:
            db.user_join_saraha(self.chat_id,False)
            return False
        if is_in_channel:
            return True
        status = bot.getChatMember(saraha_channel_id,self.chat_id)['status']
        if status == 'creator' or status == 'administrator' or status == 'member' or status == 'restricted':
            db.user_join_saraha(self.chat_id,True)
            return True
        return False

    

    def user_has_ans_poll(self):
        db.user_has_ans_poll(self.chat_id)
        if not rm_approve_fun:
            bot.sendMessage(self.chat_id, "الرجاء ارسال اسمك ثلاثي والفرقة والقسم\nوسيقوم الادمن باتاحة البوت اليك بعد التحقق من الاسم")

        else:
            self.approve_user(self.chat_id)

    def approve_user(self,msg_id):
        db.approve_user(self.chat_id)
        text = "اهلا وسهلا بك لقد تم قبولك بنجاح نتمني لك تجربة ممتعة"
        self.keyboards.Open_Keyboard(self.chat_id, '0', text, shape= True)
        bot.editMessageReplyMarkup(chat_id_group_id,msg_id)

    def set_pos(self, new_pos):
        db.set_pos(self.chat_id, new_pos) 

    def create_new_user(self):
        text = bot.getChat(self.chat_id)
        first_name = text['first_name']
        last_name = text['last_name'] if 'last_name' in text else ""
        data = {
            "postion": "0",
            "is_ans_poll": False,
            "is_approved": False,
            "first_name": first_name,
            'last_name': last_name,
        }
        db.new_user(self.chat_id, data)
        msg = json.dumps(text, indent=4, ensure_ascii=False)
        bot.sendMessage(chat_id_group_id, msg)
        if not rm_alarm_msg:
            bot.copyMessage(self.chat_id, main_group_id, privacy_msg_id, protect_content=True)
        bot.forwardMessage(self.chat_id, main_group_id, main_poll_id, protect_content=True)

    @property
    def pos(self):
        return self.__data['postion']

    @property
    def get_neck_name(self):
        first_name = self.__data['first_name']
        last_name = self.__data['last_name']
        return f"{first_name} {last_name}"

    @property
    def get_neck_name_handeled(self):
        return self.keyboards.handle_button(self.get_neck_name)

    @property
    def is_approved(self):
        if rm_approve_fun:
            return True
        return self.__data['is_approved']


    @property
    def is_ans_poll(self):
        x = self.__data['is_ans_poll']
        return x
