from pri_msg import *


class Message:
    def __init__(self, msg) -> None:
        self.msg = msg
        self.chat_id = str(msg['chat']['id'])
        self.id = msg['message_id']
        self.keyboards = Keyboards()

    @property
    def time(self):
        return self.msg['date']

    @property
    def text_handeled(self):
        return self.keyboards.handle_button(self.text)

    @property
    def is_forwarded(self):
        return 'forward_date' in self.msg

    @property
    def is_poll(self):
        return 'poll' in self.msg

    @property
    def text(self):
        if not self.is_text:
            return ""
        text = self.msg['text']
        if len(text) > 4 and text[0] in shaps and text[-1] in shaps:
            return self.keyboards.from_shap_to_keyboard(text)
        return text

    @property
    def is_text(self):
        return 'text' in self.msg


class Update:

    def __init__(self, request) -> None:
        self.__request = request
        self.id = request['update_id']
        save_update(self.id, self.string_update)
        db.add_update(request)

    @property
    def callback_query(self):
        x = self.__request['callback_query']
        return x['data'], x['message']['message_id']

    @property
    def chat_id_poll(self):
        return self.__request['poll_answer']['user']['id']

    @property
    def channel_id_link(self):
        return self.__request['chat_join_request']['chat']["id"]

    @property
    def channel_name(self):
        return self.__request['my_chat_member']['chat']["title"]

    @property
    def channel_id(self):
        return self.__request['my_chat_member']['chat']["id"]

    @property
    def poll_id(self):
        return self.__request['poll_answer']['poll_id']

    @property
    def chat_join_id(self):
        return self.__request['chat_join_request']['from']['id']

    @property
    def message(self):
        return Message(self.__request['message'])

    @property
    def type(self):
        type = list(self.__request)[1]
        if type == 'message':
            if self.__request['message']['chat']['type'] == 'private':
                return 'private'
            else:
                return "Group"
        return type

    @property
    def string_update(self):
        return json.dumps(self.__request, indent=4, ensure_ascii=False)
