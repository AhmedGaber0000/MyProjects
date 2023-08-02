from edit_keyboard import *


class Pri_msg:
    def __init__(self, msg) -> None:
        self.msg = msg
        self.chat_id = msg.chat_id
        self.msg_id = msg.id
        self.is_text = msg.is_text
        self.text = msg.text
        self.is_poll = msg.is_poll
        self.is_forwarded = msg.is_forwarded
        self.Time = msg.time
        self.user = User(self.chat_id)
        self.keyboards = self.user.keyboards

    def run(self):

        if self.is_new:
            self.user.create_new_user()

        elif not self.user.is_ans_poll:
            bot.forwardMessage(self.chat_id, main_group_id, main_poll_id, protect_content=True)

        elif not self.user.is_approved:
            bot.not_approve_msg(self.user, self.msg)

        elif not self.user.is_in_channel:
            text = f'عفوا الرجاء الاشتراك بهذه القناة وذلك ليتم التواصل معنا بسهولة وحل المشكلات التي تواجهكم وابداء ارائكم عن البوت\nعلما بانه يمكنك الخروج منها متي شئت ولكن يجب الدخول لها ولو لمرة واحده وذلك لضمان جودة الخدمة\n\n{link_saraha_channel}\nبعد الاشتراك بالقناة يمكنك تصفح البوت بدون اي مشاكل\nشكرا لكم'
            bot.sendMessage(self.chat_id,text)

        elif Admins(self.chat_id).is_change_request:
            admin = Admins(self.chat_id)
            Edit_Keyboard(admin, self.msg_id, self.text, self.is_poll, self.is_forwarded).run()

        elif self.is_text:
            if self.is_press_key:
                db.log(self.Time, self.chat_id, [self.user.pos, self.text])
                if self.is_request_data:
                    if not self.data or not self.data[0] or self.data[0] == "???":
                        bot.sendMessage(self.chat_id, ms.no_material)

                    elif len(self.data) == 1:
                        bot.Send_Data(self.chat_id, self.data[0])

                    else:
                        bot.Send_Questions(self.chat_id, self.data)

                else:
                    if self.data == "###":
                        bot.sendMessage(self.chat_id, ms.no_material)

                    else:
                        self.keyboards.Open_Keyboard(self.chat_id, self.data, shape= True)
                        self.user.set_pos(self.data)

            elif self.text == "/start":
                self.keyboards.Open_Keyboard(self.chat_id, "0", shape= True)
                self.user.set_pos('0')

            elif Admins(self.chat_id).is_admin:  #
                admin = Admins(self.chat_id)
                Admin_requests(self.Time, admin, self.text).run()

            else:
                self.keyboards.Open_Keyboard(self.chat_id, self.user.pos, ms.messages_closed,shape= True)

        else:
            self.keyboards.Open_Keyboard(self.chat_id, self.user.pos, ms.messages_closed, shape= True)

    @property
    def is_request_data(self):
        self.data = self.keyboards.Keys[self.user.pos][self.text]
        return type(self.data) is list

    @property
    def is_press_key(self):
        return self.text in self.keyboards.Keys[self.user.pos]

    @property
    def is_new(self):
        return not self.chat_id in db.Data['has_enter']