from data import *


class Bot_action(telepot.Bot):
    def __init__(self, token):
        super().__init__(token)

    def invint_link(self, chat_id, is_approved, channel_id):
        if is_approved:
            self.approveChatJoinRequest(channel_id, chat_id)
        else:
            self.declineChatJoinRequest(channel_id, chat_id)

    def not_approve_msg(self, user, msg):
        chat_id = user.chat_id
        if msg.is_text:
            self.sendMessage(chat_id, 'تم ارسال الرسالة الي الادمن')
            text = f"Name {user.get_neck_name_handeled}\nChat id `{chat_id}`\n\n{msg.text_handeled}"
            self.sendMessage(chat_id_group_id, text, parse_mode='Markdown',reply_markup={"inline_keyboard":[[{"text":"approve","callback_data":str(chat_id)}]]})
        else:
            self.sendMessage(chat_id, 'عفوا غير مسموح بارسال اي رسالة غير نصيه')

    def Send_Questions(self, chat_id, msg_ids):
        try:
            for msg_id in msg_ids:
                self.copyMessage(chat_id, main_group_id, msg_id, protect_content=True)
        except:
            self.sendMessage(chat_id, ms.no_material)

    def Send_Data(self, chat_id, msg_id):
        try:
            r_msg_id = self.copyMessage(chat_id, main_group_id, msg_id, protect_content=True)['message_id']
            db.add_delete_msg_id(chat_id, r_msg_id)
            return r_msg_id
        except:
            self.sendMessage(chat_id, ms.no_material)

    def send_to_main_group(self, msg_id, chat_id_from):
        return self.copyMessage(main_group_id, chat_id_from, msg_id)['message_id']

    def open_menu(self, chat_id, keyboard, text, reply_to_msg_id=None):
        reply_markup = {
            "keyboard": keyboard,
            "is_persistent": True,
            "resize_keyboard": True
        }
        self.sendMessage(chat_id, text, reply_to_message_id=reply_to_msg_id, reply_markup=reply_markup)

    def set_commands(self):
        admins_chat_ids = list(db.Data['admins'])
        commands = []
        for command in admin_commands:
            discription = admin_commands[command]
            commands.append({"command": command, 'description': discription})

        def scope(a): return {
            "type": "chat",
            "chat_id": a}

        for chat_id in admins_chat_ids:
            try:
                self.setMyCommands(commands, scope(chat_id))
            except:
                pass

        for command in master_commands:
            discription = master_commands[command]
            commands.append({"command": command, 'description': discription})
        self.setMyCommands(commands, scope(master_id))

    def setwebhook(self):
        self.setWebhook(url, max_connections=1)


bot = Bot_action(token)
