from user import *
from data import *
from keyboards import Keyboards
from logging_lib import Log


class Pri_msg_det:
    def __init__(self, msg) -> None:
        self.msg = msg
        self.chat_id = msg['chat']['id']
        self.msg_id = msg['message_id']
        self.text = self.pure_text
        self.user = User(self.chat_id, self.text)

    @property
    def run(self):
        if self.is_the_first:  # checked
            self.user.start_new  # checked
        elif not self.user.is_ans_poll:  #
            self.user.sendMessage("عفوا الرجاء التصويت بالاعلي علي الاستفتاء اولا")  # checked
        elif not self.user.is_sub_gen:  #
            if not self.user.check_sub_gen:  # checked
                self.user.sendMessage(gen_channel_text)  # checked

            else:
                self.user.sendMessage(depart_chennel_text)  # checked
        elif not self.user.is_sub_depart:  # checked
            if not self.user.check_sub_depart:  # checked
                self.user.sendMessage(depart_chennel_text)  # checked

            else:
                self.user.open_keyboard_start  # checked

        elif self.user.change_button:  # checked
            num_change = self.user.change_button  # checked

            if num_change == 7:  # checked
                self.user.add_mat_to_btn(self.msg_id)  # checked

            elif num_change == 11:  # checked
                if self.text:  # checked
                    if self.text == "stop":  # checked
                        self.user.stop_send_q  # checked

                    else:
                        self.user.sendMessage('عفوا لا يمكن اضافة اي شئ غير الاسئلة')  # checked

                elif "poll" in self.msg:  # checked
                    if 'forward_date' in self.msg:  # checked
                        self.user.sendMessage(
                            "عفوا هذا السؤال لن يتم اضافته الي الزر لانه قد تم تحويلة الرجاء ارسال السؤال بدون تحويل")  # checked

                    else:  # checked
                        self.user.add_question(self.msg_id)  # checked

                else:
                    self.user.sendMessage('عفوا لا يمكن اضافة اي شئ غير الاسئلة')  # checked

            elif self.text == "/cancel":  # checked
                self.user.cancel  # checked

            elif num_change == 1:  # checked
                self.user.add_Q_button(self.text)  # checked

            elif num_change == 2:  # checked
                if self.is_press_key:  # checked
                    self.user.sendMessage("عفوا الاسم موجود بالفعل")  # checked

                else:  # checked
                    self.user.rename_Q_button(self.text)  # checked

            elif num_change == 3:  # checked
                if self.is_press_active_key:  # checked
                    self.user.rename_button_to_Q(self.text)  # checked

                else:  # checked
                    self.user.sendMessage("عفوا الرجاء الاختيار من الازرار التي بالاسفل")  # checked

            elif num_change == 4:  # checked
                if self.is_press_key:  # checked
                    self.user.sendMessage("عفوا الاسم موجود بالفعل")  # checked

                else:  # checked
                    self.user.rename_Q_button(self.text)  # checked

            elif num_change == 5:  # checked
                if self.is_press_active_key:  # checked
                    self.user.delete_button(self.text)  # checked

                else:
                    self.user.sendMessage("عفوا الرجاء الاختيار من الازرار التي بالاسفل")  # checked

            elif num_change == 6:
                self.user.sel_btn_add_mat(self.text)  # checked

                else:  # checked
                    self.user.sendMessage("عفوا الرجاء الاختيار من الازرار التي بالاسفل")  # checked

            elif num_change == 8:  # checked
                if self.is_press_active_key:  # checked
                    self.user.add_menu(self.text)  # checked

                else:  # checked
                    self.user.sendMessage("عفوا الرجاء الاختيار من الازرار التي بالاسفل")  # checked

            elif num_change == 10:  # checked
                if self.is_press_active_key:  # checked
                    self.user.sel_send_multi_qustions(self.text)  # checked

                else:  # checked
                    self.user.sendMessage("عفوا الرجاء الاختيار من الازرار التي بالاسفل")  # checked

            elif num_change == 13:
                if self.is_press_active_key:
                    self.user.name_btn_moving(self.text)

                else:
                    self.user.sendMessage("عفوا الرجاء الاختيار من الازرار التي بالاسفل")

            elif num_change == 14:
                self.user.move_btn_done(self.text)
        elif self.is_send_text:  # checked
            if self.is_press_key:  # checked
                if self.is_request_data:  # checked
                    if not self.data or not self.data[0] or self.data[0] == "???":  # checked
                        self.user.sendMessage('لم تتم اضافة المحتوي حتي الان')  # checked

                    elif len(self.data) == 1:  # checked
                        self.user.send_data(self.data)  # checked

                    else:  # checked
                        self.user.send_questions(self.data)  # checked

                else:
                    if self.data == "###":
                        self.user.sendMessage('لم تتم اضافة المحتوي حتي الان')  # checked

                    else:
                        self.user.open_keyboard_pos(self.data)  # checked

            elif self.text == "/start":  # checked
                self.user.open_keyboard_start  # checked

            elif self.user.is_admin or str(self.chat_id) == master_id:  #
                if self.text == '/add_btn':  # checked
                    if self.is_admin_area:
                        self.user.add_btn_req

                    else:
                        self.user.not_area
                elif self.text == '/move_btn':
                    if self.is_admin_area:
                        self.user.move_btn
                    else:
                        self.user.not_area

                elif self.text == '/rm_btn':  #
                    if self.is_admin_area:
                        if len(self.user.Keyboards) != 1:
                            self.user.rm_btn_req

                        else:
                            self.user.sendMessage('عفوا لا يوجد ازرار لحذفها')

                    else:
                        self.user.not_area

                elif self.text == '/add_mat':  #
                    if self.is_admin_area:
                        self.user.add_mat_req

                    else:
                        self.user.not_area

                elif self.text == '/add_menu':  #
                    if self.is_admin_area:
                        self.user.add_menu_req

                    else:
                        self.user.not_area

                elif self.text == '/re_name':  #
                    if self.is_admin_area:
                        self.user.rename_req

                    else:
                        self.user.not_area

                elif self.text == '/start_mult_q':  #
                    if self.is_admin_area:
                        self.user.send_questions_req

                    else:
                        self.user.not_area

                elif self.chat_id == int(master_id):
                    try:  #
                        point = self.text.index("\n")
                        specify = self.text[:point]
                        text = self.text[point+1:]

                    except:
                        specify = self.text

                    if specify == "/all_user":
                        "all users"
                        self.all_users()

                    elif specify == "/add_admin":  #
                        lines = text.splitlines()
                        chat_id = lines[0]
                        user = User(chat_id)
                        user.level = lines[1]
                        user.depart = lines[2]
                        user.channel_id = lines[3]
                        user.channel_url = lines[4]

                        user.is_admin = 1
                        user.write
                        Files_actions().append('bot/admins', f'{chat_id}\n')
                        bot.set_commands()
                        User(chat_id).sendMessage(
                            f'لقم تم رفعك كادمن للمستوي رقم {user.level}\n القسم رقم {user.depart}\n الترم رقم {now_term} ')
                        User(master_id).sendMessage('Done')

                        return

                    elif specify == '/num_users':
                        "num users"
                        self.num_users()

                    elif specify == '/his_user':
                        "his user"

                    elif specify == '/chat_file':
                        "chat_file"

                    elif specify == '/change_pos':
                        "change postion"

                    elif specify == '/blocked_users':
                        "blocked users"

                    elif specify == '/block_user':
                        "block user"

                    elif specify == '/unblock_user':
                        "unblock user"

                    elif specify == '/his_day':
                        "his day"

                    elif specify == "/start_bot":
                        pass

                    else:
                        self.user.sendMessage('لا يوجد امر هكذا')

                else:
                    self.user.open_keyboard_pos(self.user.pos, "تم اغلاق ارسال الرسائل")
            else:
                self.user.open_keyboard_pos(self.user.pos, "تم اغلاق ارسال الرسائل")
        else:
            self.user.open_keyboard_pos(self.user.pos, "تم اغلاق ارسال الرسائل")
        self.user.write

    @property
    def pure_text(self):
        if 'text' in self.msg:
            text = self.msg['text']
            if len(text) > 4 and text[0] in shaps and text[-1] in shaps:
                return Keyboards().from_shap_to_keyboard(text)

            else:
                return text

        else:
            return ''

    @property
    def is_press_active_key(self):
        a = self.is_press_key
        b = self.text != "رجوع"
        c = self.text != "القائمة الرئيسية"
        return a and b and c

    @property
    def is_admin_area(self):
        if str(self.chat_id) == master_id:
            return True

        Map = Files_actions().read_json("bot/Map.json")[self.user.level][self.user.depart][now_term]
        for sub in Map:
            if self.user.pos in Map[sub]:
                return True
        return False

    @property
    def is_admin(self):
        x = self.user.is_admin
        if x or self.chat_id == str(master_id):
            return True
        return False

    @property
    def another(self):
        return self.data[0] == '#'

    @property
    def is_request_data(self):
        self.data = self.user.Keys[self.text]
        return type(self.data) is list

    @property
    def is_press_key(self):
        x = self.text in self.user.Keys
        return x

    @property
    def is_the_first(self):
        return not self.user.is_has_enter

    @property
    def user_msg_id_from(self):
        if 'forward_sender_name' in self.reply:
            name = self.reply['forward_sender_name']
        else:
            name = self.reply['forward_from']['first_name']+" " + \
                self.reply['forward_from']['last_name'] if 'last_name' in self.reply['forward_from'] else self.reply['forward_from']['first_name']
        forward_date = self.reply['forward_date']
        if '\\' in name:
            name = name.replace('\\', ".")
        if '/' in name:
            name = name.replace('/', ".")
        r = self.readlines(f'bot/forward_msg/{name}{forward_date}')
        user_id = r[0][:-1]
        msg_id = r[1]
        return user_id, int(msg_id)

    @property
    def is_reply_to_forward_msg(self):
        x = self.user.is_admin and "reply_to_message" in self.msg and "forward_date" in self.msg['reply_to_message']
        if x:
            self.user_id, self.msg_id_from = self.user_msg_id_from
            return x
        return False

    @property
    def is_new(self):
        return not self.user.is_old

    def is_blocked(self, chat_id):
        return User(chat_id).is_block

    @property
    def is_send_text(self):
        x = "text" in self.msg
        if x:
            self.text = self.pure_text
            return True
        return False
