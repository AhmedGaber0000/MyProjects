from master import *


class Edit_Keyboard:
    def __init__(self, Admin: Admins, msg_id, text, is_poll, is_forwarded) -> None:
        self.is_poll = is_poll
        self.is_forwarded = is_forwarded
        self.Admin = Admin
        self.msg_id = msg_id
        self.text = text
        self.change_request = Admin.get_change_request
        self.keyboards = Keyboards()

    def press_key_methods(self):
        if self.change_request == "rename_btn_request":
            self.keyboards.rename_button(self.text, "?", self.Admin.pos)
            self.keyboards.Open_Keyboard(self.Admin.chat_id, self.Admin.pos, "ارسل الاسم الجديد")
            self.Admin.set_change_request("rename_btn_new_name")

        elif self.change_request == "remove_btn_request":
            value = self.keyboards.Keys[self.Admin.pos][self.text]
            self.keyboards.delete_button(self.text, self.Admin.pos)
            if type(value) is list and value and value[0] and len(value) == 1 and value:
                msg_id = self.keyboards.get_ch_msg_id(str(value[0]))
                try:
                    bot.deleteMessage((self.Admin.channel_id, msg_id))

                except:
                    pass

            self.keyboards.Open_Keyboard(self.Admin.chat_id, self.Admin.pos, "تم حذف الزر بنجاح", shape=True)
            self.Admin.set_change_request("")

        elif self.change_request == "add_mat_request":
            self.keyboards.sel_btn_add_mat(self.text, self.Admin.pos)
            bot.sendMessage(self.Admin.chat_id, "ارسل المحتوي الذي تريد اضافته")
            self.Admin.set_change_request('add_mat_new_mat')

        elif self.change_request == "add_menu_request":
            new_pos = self.keyboards.create_new_keyboard(self.Admin.pos, self.text)
            self.Admin.add_self_pos()
            self.keyboards.Open_Keyboard(self.Admin.chat_id, new_pos, 'تم اضافة القائمة بنجاح',shape= True)
            db.set_pos(self.Admin.chat_id, new_pos)
            self.Admin.set_change_request('')

        elif self.change_request == "send_questions_request":
            self.keyboards.sel_add_multi_qustions(self.text, self.Admin.pos)
            bot.sendMessage(self.Admin.chat_id, 'ارسل جميع الاسئلة التي تريد اضافتها الي الزر وبعد الانتهاء ارسل stop')
            self.Admin.set_change_request('send_multi_questions')

        elif self.change_request == "move_btn_request":
            self.Admin.set_event(self.text)
            new_keyboard = self.keyboards.add_btn_keyboard(self.Admin.pos)
            bot.open_menu(self.Admin.chat_id, new_keyboard, 'اختر المكان الجديد للزر')
            self.Admin.set_change_request('move_btn_new_place')

        else:
            bot.sendMessage(self.Admin.chat_id, ms.select_from_bottom)

    def not_press_key_methods(self):
        if self.change_request == "add_btn_request":
            is_created_keyboard = self.keyboards.create_Q_button(self.text, self.Admin.pos)
            if is_created_keyboard:
                self.keyboards.Open_Keyboard(self.Admin.chat_id, self.Admin.pos, "ارسل اسم الزر")
                self.Admin.set_change_request('add_btn_new_name')

            else:
                bot.sendMessage(self.Admin.chat_id, ms.select_from_bottom)

        elif self.change_request == "add_btn_new_name":
            self.keyboards.rename_button('?', self.text, self.Admin.pos)
            self.keyboards.Open_Keyboard(self.Admin.chat_id, self.Admin.pos, "تم اضافة الزر بنجاح", shape= True)
            self.Admin.set_change_request('')

        elif self.change_request == "rename_btn_new_name":
            self.keyboards.rename_button('?', self.text, self.Admin.pos)
            self.keyboards.Open_Keyboard(self.Admin.chat_id, self.Admin.pos, "تم تغيير الاسم بنجاح",shape= True)
            self.Admin.set_change_request('')

        elif self.change_request == "move_btn_new_place":
            button_name = self.Admin.get_event
            value_button = self.keyboards.Keys[self.Admin.pos][button_name]
            self.keyboards.rename_button(button_name, 'new_name', self.Admin.pos)
            is_created_keyboard = self.keyboards.create_Q_button(self.text, self.Admin.pos, button_name, value_button)
            if is_created_keyboard:
                self.keyboards.delete_button('new_name', self.Admin.pos)
                self.keyboards.Open_Keyboard(self.Admin.chat_id, self.Admin.pos, 'تم نقل الزر بنجاح', shape= True)
                self.Admin.set_change_request('')

            else:
                bot.sendMessage(self.Admin.chat_id, ms.select_from_bottom)

        elif self.change_request == "post_request":
            if not self.text:
                bot.sendMessage(self.Admin.chat_id, 'عفوا غير مسموح باي رسائل غير نصية\nالرجاء ارسال رسالة نصية فقط')

            else:
                msg_id = bot.sendMessage(main_group_id, self.text)['message_id']
                bot.copyMessage(self.Admin.channel_id, main_group_id, msg_id)
                bot.sendMessage(self.Admin.chat_id,"تم النشر بنجاح")
                self.Admin.set_change_request('')

        else:
            bot.sendMessage(self.Admin.chat_id, ms.select_from_bottom)

    def cannot_be_canceled(self):
        is_done = True
        if self.change_request == "add_mat_new_mat":
            main_group_msg_id = bot.copyMessage(main_group_id, self.Admin.chat_id, self.msg_id)['message_id']
            self.keyboards.add_mat_to_btn(main_group_msg_id, self.Admin.pos)
            add_mat_parameters = self.Admin.add_mat_parameters
            if add_mat_parameters:
                sub, sub_pos, pin_msg_id = add_mat_parameters
                channel_msg_id = bot.copyMessage(self.Admin.channel_id, main_group_id, main_group_msg_id)['message_id']
                db.add_map_msg_id(main_group_msg_id, channel_msg_id)
                self.keyboards.arrang_Keys(self.Admin.pos)
                map = self.keyboards.make_dic_map(self.Admin.channel_url, sub_pos)
                sub = self.keyboards.handle_button(sub)
                text = f"Sub: {sub}\n\n{map}"
                bot.editMessageText(self.Admin.channel_id, pin_msg_id, text,
                                    parse_mode="MarkdownV2", disable_web_page_preview=True)

            bot.sendMessage(self.Admin.chat_id, 'لقد تم اضافة المحتوي بنجاح')
            self.Admin.set_change_request("")

        elif self.change_request == "send_multi_questions":
            if self.text:
                if self.text == "stop":
                    self.keyboards.rm_three_q_mark(self.Admin.pos)
                    bot.sendMessage(self.Admin.chat_id, "لقد تم اضافة جميع الاسئلة بنجاح")
                    self.Admin.set_change_request("")

                else:
                    bot.sendMessage(self.Admin.chat_id, ms.add_questions_only, reply_to_message_id=self.msg_id)

            elif self.is_poll:
                if self.is_forwarded:
                    bot.sendMessage(self.Admin.chat_id, ms.not_send_forward_question, reply_to_message_id=self.msg_id)

                else:
                    msg_id = bot.send_to_main_group(self.msg_id, self.Admin.chat_id)
                    self.keyboards.add_qustions_msg_id(msg_id, self.Admin.pos)

            else:
                bot.sendMessage(self.Admin.chat_id, ms.add_questions_only, reply_to_message_id=self.msg_id)

        else:
            is_done = False

        return is_done

    def run(self):
        if not self.cannot_be_canceled():

            if self.text == '/cancel':
                self.cancel()

            else:
                self.can_be_canceled()

    def can_be_canceled(self):
        if self.is_press_key:
            self.press_key_methods()
        else:
            self.not_press_key_methods()

    @property
    def is_press_key(self):
        return self.text in self.keyboards.Keys[self.Admin.pos] and self.text != "رجوع"

    def cancel(self):
        self.Admin.set_change_request("")
        self.keyboards.Open_Keyboard(self.Admin.chat_id, self.Admin.pos, shape= True)


class Admin_requests:
    def __init__(self, time, Admin: Admins, text) -> None:
        self.Time = time
        self.Admin = Admin
        self.text = text
        self.keyboards = Keyboards()

    def run(self):
        if not self.Admin.is_admin_area:
            bot.sendMessage(self.Admin.chat_id, ms.not_admin_area)

        elif self.text == '/add_btn':
            self.add_btn_Request()
            db.log(self.Time, self.Admin.chat_id,"add_btn")

        elif self.text == '/re_name':  #
            self.rename_btn_request()
            db.log(self.Time, self.Admin.chat_id,"re_name")

        elif self.text == '/rm_btn':  #
            if len(self.keyboards.Keyboards[self.Admin.pos]) != 1:
                self.remove_btn_request()
                db.log(self.Time, self.Admin.chat_id,"rm_btn")

            else:
                bot.sendMessage(self.Admin.chat_id, ms.no_button_to_remove)

        elif self.text == '/add_mat':  #
            self.add_mat_request()
            db.log(self.Time, self.Admin.chat_id,"add_mat")

        elif self.text == '/add_menu':  #
            self.add_menu_request()
            db.log(self.Time, self.Admin.chat_id,"add_menu")

        elif self.text == '/start_mult_q':  #
            self.send_questions_request()
            db.log(self.Time, self.Admin.chat_id,"start_mult_q")

        elif self.text == '/move_btn':
            self.move_btn_request()
            db.log(self.Time, self.Admin.chat_id,"move_btn")

        elif self.text == '/post':
            self.post_request()
            db.log(self.Time, self.Admin.chat_id,"post")
        else:
            Master(self.Admin, self.text).requests()

    def post_request(self):
        bot.sendMessage(self.Admin.chat_id, 'ارسل المنشور الذي تريد ارساله في القناة')
        self.Admin.set_change_request('post_request')

    def send_questions_request(self):
        bot.sendMessage(self.Admin.chat_id, "اختر الزر الذي تريد اضافة الاسئلة اليه")
        self.Admin.set_change_request("send_questions_request")

    def rename_btn_request(self):
        bot.sendMessage(self.Admin.chat_id, "اختر الزر الذي تريد تغيير اسمه")
        self.Admin.set_change_request("rename_btn_request")

    def add_menu_request(self):
        bot.sendMessage(self.Admin.chat_id, "اختر الزر الذي تريد اضافة قائمة اليه")
        self.Admin.set_change_request("add_menu_request")

    def add_mat_request(self):
        bot.sendMessage(self.Admin.chat_id, "اختر الزر الذي تريد اضافة المحتوي اليه")
        self.Admin.set_change_request("add_mat_request")

    def remove_btn_request(self):
        bot.sendMessage(self.Admin.chat_id, "اختر الزر الذي تريد حذفه")
        self.Admin.set_change_request("remove_btn_request")

    def move_btn_request(self):
        bot.sendMessage(self.Admin.chat_id, 'اختر الزر الذي تريد تغيير مكانه')
        self.Admin.set_change_request("move_btn_request")

    def add_btn_Request(self):
        new_keyboard = self.keyboards.add_btn_keyboard(self.Admin.pos)
        bot.open_menu(self.Admin.chat_id, new_keyboard, 'اختر مكان الزر الجديد')
        self.Admin.set_change_request("add_btn_request")
