from Admins import *


class Master:
    def __init__(self, Admin: Admins, text) -> None:
        self.text = text
        self.Admin = Admin
        self.pos = Admin.pos
        self.chat_id = Admin.chat_id
        self.keyboards = Admin.keyboards

    @property
    def __data(self):
        return db.Data

    def requests(self):
        lines = self.text.splitlines()
        det = lines[0]
        if det == '/add_admin':
            admin_chat_id = lines[1]
            admin_channel_id = lines[2]
            admin_name = lines[3]
            file = self.file_template(admin_channel_id, admin_name)
            db.add_admin(admin_chat_id, file)
            bot.sendMessage(admin_chat_id, "تمت اضافتك كادمن في البوت")

        elif det == '/add_depart':
            """
            id of admin
            name of admin
            id of channel
            name of subjects
            pos of depart

            1- create the buttons
            2- add admin
            3- add subjects to the admin

            """
            admin_id = lines[1]
            admin_name = lines[2]
            channel_id = lines[3]
            subjects = lines[4:]

            file = self.file_template(channel_id, admin_name)
            db.add_admin(admin_id, file)
            bot.set_commands()
            
            num = 1
            channel_name = self.keyboards.get_channel_name_from_id(channel_id)
            channel_name = self.keyboards.handle_button(channel_name)
            invent_link = bot.createChatInviteLink(channel_id,creates_join_request=True)['invite_link']
            channel_name_link = f"[{channel_name}]({invent_link})"
            msg_id_link = bot.sendMessage(main_group_id, channel_name_link, parse_mode="MarkdownV2")['message_id']
            self.keyboards.create_Q_button("...1...", self.pos, "قناة القسم", [msg_id_link])
            for sub in subjects:
                num += 1
                place = f"...{num}..."
                pos = self.pos
                value = str(self.keyboards.max_key+1)
                self.keyboards.create_Q_button(place, self.pos, sub, value)
                new_pos = self.keyboards.create_new_keyboard(self.pos, sub)
                pin_msg = bot.sendMessage(channel_id, sub)['message_id']
                sub_temp = self.subject_template(pin_msg, new_pos)
                db.add_sub_to_admin(admin_id, sub, sub_temp)

            bot.sendMessage(admin_id, "تمت اضافتك كادمن في البوت")

            self.keyboards.Open_Keyboard(self.chat_id, self.pos, shape=True)

        elif det == '/channel_ids':
            channels = self.__data['channel_ids']
            ids = ""
            for name_channel in channels:
                channel_id = channels[name_channel]
                ids += f"{name_channel} : `{channel_id}`\n\n"
            bot.sendMessage(self.chat_id, ids, parse_mode="Markdown")

        elif det == "/admins_ids":
            chat_ids = db.Data['admins']
            ids = ""
            for chat_id in chat_ids:
                name = self.keyboards.handle_button(chat_ids[chat_id]['admin_name'])
                ids += f"{name} `{chat_id}`\n\n"
            bot.sendMessage(master_id, ids, parse_mode="Markdown")

        elif det == "/add_sub":
            chat_id = lines[1]
            sub_name = lines[2]
            pos = self.Admin.pos
            new_admin = Admins(chat_id)
            channel_id = new_admin.channel_id
            file = new_admin.get_sub_pos_pin(pos)
            if not file:
                pin_msg = bot.sendMessage(channel_id, sub_name)['message_id']
                sub_temp = self.subject_template(pin_msg, pos)
                db.add_sub_to_admin(chat_id, sub_name, sub_temp)
                bot.sendMessage(chat_id, f'تم فتح مادة {sub_name} لك للتعديل فيها')

        else:
            self.keyboards.Open_Keyboard(self.chat_id, self.Admin.pos, ms.messages_closed, shape=True)
        bot.sendMessage(master_id, 'Done')

    def add_admin_request(self):
        self.Admin.set_change_request("add_Admin")
        msg = "admin_chat_id\nchannel_id"
        bot.sendMessage(self.chat_id, msg)

    def gen_postions(self, pos):
        buttons = self.keyboards.Keys[str(pos)]
        postions = []
        postions.append(pos)
        for button in buttons:
            value = buttons[button]
            if type(value) is str and value != "#" and value != "###" and button != "رجوع":
                postions += self.gen_postions(value)
        return postions

    def subject_template(self, pin_msg_id, sub_pos):
        postions = self.gen_postions(sub_pos)
        sub = {
            "pin_msg_id": pin_msg_id,
            "sub_pos": sub_pos,
            "postions": postions
        }
        return sub

    def file_template(self, channel_id, admin_name):
        return {
            "admin_name": admin_name,
            "change_request": "",
            "event": "",
            "add_mat_parameters": (),
            "channel_id": channel_id,
            "channel_url": f"c/{int(str(channel_id)[2:])}",
            "subjects": {}
        }
