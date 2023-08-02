

class User:
    def __init__(self, chat_id, text="") -> None:
        self.chat_id = chat_id
        def r_n(a): return Files_actions().read_num(a, self.chat_id)
        self.pos = r_n(0)
        self.level = r_n(1)
        self.depart = r_n(2)
        self.change_button = int(r_n(3))
        self.last_seen = r_n(4)
        self.is_block = int(r_n(5))
        self.is_admin = int(r_n(6))
        self.is_has_enter = int(r_n(7))
        self.is_ans_poll = int(r_n(8))
        self.is_sub_gen = int(r_n(9))
        self.is_sub_depart = int(r_n(10))
        self.channel_id = r_n(11)
        self.channel_url = r_n(12)
        self.event_place = r_n(13)

        self.text = text
        self.all_keyboards = Keyboards()
        self.Keys = self.all_keyboards.Keys[self.pos]
        self.Keyboards = self.all_keyboards.Keyboards[self.pos]
        self.log = False
        self.log_pack = lambda state, addition="": Log(self.chat_id, state, self.text, f"{self.pos} {addition}")

    @property
    def write(self):
        varbs = vars(self)
        values = []
        for varb in varbs:
            list_b = [
                'text',
                'chat_id',
                'all_keyboards',
                "Keys",
                "Keyboards",
                "log",
                "log_pack",
            ]

            if not varb in list_b:
                values.append(f"{varbs[varb]}\n")

        if self.log:
            self.log.write

        Files_actions().writelines(f'bot/chats/{self.chat_id}', values)

    @property
    def move_btn(self):
        """
        send move_btn
        -change button = num
        -send choise button
        """
        self.sendMessage('اختر الزر الذي تريد تغيير مكانه')
        self.change_button = 13
        self.log = self.log_pack("move_button")

    def name_btn_moving(self, name_btn: str):
        self.event_place = name_btn.replace('\n', "..-..")
        new_keyboard = self.all_keyboards.add_btn_keyboard(self.pos)
        self.open_keyboard(new_keyboard, 'اختر المكان الجديد للزر',shape=False)
        self.change_button = 14
        self.log = self.log_pack('name_btn_moving')

    def move_btn_done(self, place):
        button_name = self.event_place.replace("..-..", '\n')
        value = self.Keys[button_name]
        self.all_keyboards.rename_button(button_name, 'deleted_button', self.pos)
        is_create_btn = self.all_keyboards.create_Q_button(place, self.pos, button_name, value)
        if is_create_btn:
            self.delete_button('deleted_button', 'لقم تم نقل الزر بنجاح', "move_btn_done")
        else:
            self.sendMessage("الرجاء الاختيار من الازرار التي بالاسفل")

    @property
    def stop_send_q(self):
        self.all_keyboards.rm_three_q_mark(self.pos)
        self.sendMessage('لقد تم اضافة جميع الاسئلة بنجاح')
        self.change_button = 0
        self.log = self.log_pack("stop_send_q")

    def sel_send_multi_qustions(self, button):
        self.all_keyboards.sel_add_multi_qustions(button, self.pos)
        self.sendMessage("ارسل جميع الاسئلة التي تريد اضافتها الي الزر وبعد الانتهاء ارسل stop")
        self.change_button = 11
        self.log = self.log_pack("sel_send_multi_questions")

    def add_question(self, msg_id_from):
        msg_id = bot.send_to_main_group(msg_id_from, self.chat_id)
        num_q = self.all_keyboards.add_qustions_msg_id(msg_id, self.pos)
        self.sendMessage(f"تم اضافة {num_q} اسئلة")
        self.log = self.log_pack("add_question", f"msg_id: {msg_id} Num_Q: {num_q}")

    def rename_button_to_Q(self, button):
        self.all_keyboards.rename_button(button, "?", self.pos)
        self.open_keyboard(self.all_keyboards.Keyboards[self.pos], "ارسل اسم الزر")
        self.change_button = 4
        self.log = self.log_pack("rename_button_to_Q")

    def rename_Q_button(self, new_name):
        self.all_keyboards.rename_button("?", new_name, self.pos)
        self.open_keyboard(self.all_keyboards.Keyboards[self.pos], "تم بنجاح")
        self.change_button = 0
        self.log = self.log_pack("rename_Q_button")

    def add_Q_button(self, place):
        x = self.all_keyboards.create_Q_button(place, self.pos)
        if x:
            self.open_keyboard(self.all_keyboards.Keyboards[self.pos], "ارسل اسم الزر")
            self.change_button = 2
            self.log = self.log_pack("add_Q_button")
        else:
            self.sendMessage('عفوا الرجاء الاختيار من الازرار التي بالاسفل')
            self.log = self.log_pack("wrong_add_Q_button")

    def add_menu(self, button):
        new_pos = self.all_keyboards.create_new_keyboard(self.pos, button)
        self.change_button = 0
        self.open_keyboard_pos(new_pos)
        self.log = self.log_pack("add_menu")

    def add_mat_to_btn(self, msg_id):
        gr_msg_id = bot.copyMessage(main_group_id, self.chat_id, msg_id)['message_id']
        self.all_keyboards.add_mat_to_btn(gr_msg_id, self.pos)
        x = self.all_keyboards.get_pinned_from_pos(self.pos, self.level, self.depart)
        if x:
            msg_id_ch = bot.copyMessage(self.channel_id, self.chat_id, msg_id)['message_id']
            pos_sub, pinned_msg_id, sub = x
            self.all_keyboards.add_msg_id_to_channel(gr_msg_id, msg_id_ch)
            
            sub = self.all_keyboards.handle_button(sub)
            self.all_keyboards.arrang_Keys(pos_sub)
            text = self.all_keyboards.make_dic_map(self.channel_url, pos_sub)
            bot.editMessageText(self.channel_id, pinned_msg_id,
                                f"Subject: {sub}\n\n{text}", parse_mode="MarkdownV2", disable_web_page_preview=True)
        self.open_keyboard(self.all_keyboards.Keyboards[self.pos], "لقد تم اضافة المحتوي بنجاح")
        self.change_button = 0
        self.log = self.log_pack("add_mat_to_btn", f"msg_id: {gr_msg_id}")

    def sel_btn_add_mat(self, button):
        self.all_keyboards.sel_btn_add_mat(button, self.pos)
        self.sendMessage("ارسل المحتوي الذي تريد اضافته")
        self.change_button = 7
        self.log = self.log_pack("sel_btn_add_mat")

    def delete_button(self, button, msg="لقد تم حذف الزر بنجاح", log_msg="delete_button"):
        self.all_keyboards.delete_button(button, self.pos)
        self.open_keyboard(self.all_keyboards.Keyboards[self.pos], msg)
        self.change_button = 0
        self.log = self.log_pack(log_msg)

    @property
    def open_last_keyboard(self):
        keyboard = Keyboards().Keyboards[self.pos]
        self.open_keyboard(keyboard)
        self.log = self.log_pack("open_last_keyboard")

    @property
    def cancel(self):
        self.change_button = 0
        self.open_keyboard_pos(self.pos)
        self.log = self.log_pack("cancel")

    def open_keyboard_pos(self, pos, text="اختر من القائمة"):
        self.open_keyboard(self.all_keyboards.Keyboards[pos], text)
        self.log = self.log_pack("open_keyboard_pos", f"New_pos: {pos}")
        self.pos = pos

    @property
    def open_keyboard_start(self):
        self.open_keyboard(self.all_keyboards.Keyboards['0'])
        self.pos = "0"
        self.log = self.log_pack("open_keyboard_start")

    @property
    def add_menu_req(self):
        self.sendMessage('اختر الزر الذي تريد اضافة قائمة اليه')
        self.change_button = 8
        self.log = self.log_pack("add_menu_req")

    @property
    def send_questions_req(self):
        self.sendMessage('اختر الزر الذي تريد اضافة الاسئلة اليه')
        self.change_button = 10
        self.log = self.log_pack("send_questions_req")

    @property
    def rename_req(self):
        self.sendMessage("اختر الزر الذي تريد تغيير اسمه")
        self.change_button = 3
        self.log = self.log_pack("rename_req")

    @property
    def add_mat_req(self):
        self.sendMessage("اختر الزر الذي تريد اضافة المحتوي اليه")
        self.change_button = 6
        self.log = self.log_pack("add_mat_req")

    @property
    def rm_btn_req(self):
        self.sendMessage("اختر الزر الذي تريد حذفه")
        self.change_button = 5
        self.log = self.log_pack("rm_btn_req")

    @property
    def add_btn_req(self):
        keyboard = Keyboards().add_btn_keyboard(self.pos)
        self.open_keyboard(keyboard,shape=False)
        self.change_button = 1
        self.log = self.log_pack("add_btn_req")



    def open_keyboard(self, keyboard, text="اختر من القائمة", reply_to_msg_id=None, shape=True):
        if shape:
            keyboard = self.all_keyboards.convert_to_shaped(keyboard)
        bot.open_menu(self.chat_id, text, keyboard, reply_to_msg_id)
        self.log = self.log_pack('open_keyboard')

    @property
    def make_old(self):
        if not self.is_sub_gen:
            self.sendMessage(gen_channel_text)
        else:
            self.open_keyboard_start
        self.is_ans_poll = 1
        self.log = self.log_pack("ans_poll")

    @property
    def check_sub_depart(self):
        ids = [
            natural_scinece_channel_id,
            chem_2nd_channel_id,
            chem_3nd_channel_id,
            math_2nd_channel_id,
            chem_and_animals_chennel_id
        ]
        for id in ids:
            if self.check_sub(id):
                self.is_sub_depart = 1
                return True
        return False

    @property
    def check_sub_gen(self):
        x = self.check_sub(gen_channel_id)
        if x:
            self.is_sub_gen = 1
        return x

    def check_sub(self, channel_id):
        try:

            chat = bot.getChatMember(channel_id, self.chat_id)['status']

        except:
            return False

        if chat == 'left':
            return False

        else:
            return True

    def send_questions(self, data):
        for msg_id in data:
            bot.copyMessage(self.chat_id, main_group_id, msg_id)
        self.log = self.log_pack("send_qustions")

    def send_data(self, data):
        msg_id = data[0]
        bot.copyMessage(self.chat_id, main_group_id, msg_id)
        self.log = self.log_pack("send_data")

    @property
    def add_to_has_enter(self):
        Files_actions().append("bot/has_enter", f"{self.chat_id}\n")
        self.is_has_enter = 1
        self.log = self.log_pack("add_to_has_enter")

    def sendPollToUser(self, Poll_msg_id):
        self.forwardMessageToUser(Poll_msg_id, main_group_id)
        self.log = self.log_pack("send_main_poll")

    @property
    def identification(self):
        text = f"""
Chat id: {self.chat_id}
Tele_Name: {self.Tele_Name}
        """
        return text

    @property
    def Tele_Name(self):
        chat = bot.getChat(self.chat_id)
        Name = ""
        if 'first_name' in chat:
            Name += f"{chat['first_name']} "
        if 'last_name' in chat:
            Name += chat['last_name']
        return Name

    def sendMessage(self, text, reply_msg_id=None):
        bot.sendMessage(self.chat_id, text, reply_to_message_id=reply_msg_id)
        num_word = len(text.split())
        self.log = self.log_pack("sendMessage", f"Num_word: {num_word} Text: {text}")

    def forwardMessageToUser(self, msg_id, from_chat_id):
        bot.forwardMessage(self.chat_id, from_chat_id, msg_id)
        self.log = self.log_pack("forwardMessage", f"msg_id: {msg_id} From_chat_id: {from_chat_id}")
