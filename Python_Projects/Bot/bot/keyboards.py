from bot_lib import *


class Keyboards:
    def __init__(self):

        self.Keyboards = db.Data['keyboards']
        self.Keys = db.Data['keys']


    def get_channel_name_from_id(self,id):
        all_channels = db.Data['channel_ids']
        for name_channel in all_channels:
            if str(id) == str(all_channels[name_channel]):
                return name_channel

    def get_msg_ids(self, pos, indent=""):
        keyboard = self.Keys[pos]
        msg_ids = []
        for button_name in keyboard:
            value = keyboard[button_name]
            if type(value) is list and value and len(value) == 1 and value[0] and value[0] != "???":
                msg_ids.append(value[0])
            elif type(value) is str and value != "#" and value != "###" and button_name != "رجوع":
                msg_ids += self.get_msg_ids(value, indent=indent+"  ")
        return msg_ids

    def Open_Keyboard(self, chat_id, pos, text=ms.menu_msg,shape = False):
        keyboard = self.Keyboards[pos]
        if shape:
            keyboard = self.convert_to_shaped(keyboard)
        bot.open_menu(chat_id, keyboard, text)

    def arrang_Keys(self, pos):
        keyboard = self.Keyboards[pos]
        keys = self.Keys[pos]
        dic_keys = {}
        dic_trans = {}
        for row in keyboard:
            for button in row:
                button_name = button['text']
                if button_name in keys:
                    button_value = keys[button_name]
                    if type(button_value) is str:
                        dic_trans[button_name] = button_value
                    else:
                        dic_keys[button_name] = button_value
        dic_keys.update(dic_trans)
        self.Keys[pos] = dic_keys
        self.write_keyboard

    def from_shap_to_keyboard(self, button):
        lines = button.splitlines()
        e = ""
        if len(lines) > 1:
            for line in lines[:-1]:
                e += f"{line[2:-2]}\n"
        e += f"{lines[-1][2:-2]}"
        return e

    def convert_to_shaped(self, old_keyboard):
        new_keyboard = []

        def sh():
            r = random.random()*0.999999*len(shaps)
            x = shaps[int(r)]
            return x

        for row in old_keyboard:
            new_row = []
            for elem in row:
                button = elem['text']
                button = button.replace('\n', f' {sh()}\n{sh()} ')
                new_row.append({"text": f"{sh()} {button} {sh()}"})
            new_keyboard.append(new_row)
        return new_keyboard

    def rm_three_q_mark(self, pos):
        keyboard = self.Keys[pos]
        for button in keyboard:
            value = keyboard[button]
            if type(value) is list and value[0] == "???":
                self.Keys[pos][button].pop(0)
                self.write_keyboard
                return

    def add_qustions_msg_id(self, msg_id, pos):
        keyboard = self.Keys[pos]
        for button in keyboard:
            value = keyboard[button]
            if type(value) is list and value[0] == "???":
                self.Keys[pos][button].append(msg_id)
                self.write_keyboard
                return len(value) - 1

    def sel_add_multi_qustions(self, button, pos):
        self.Keys[pos][button] = ["???"]
        self.write_keyboard

    def delete_button(self, button, pos):
        keyboard = self.Keyboards[pos]
        num_row = len(keyboard)

        for row in range(0, num_row):
            num_elem = len(keyboard[row])

            for elem in range(0, num_elem):
                key = keyboard[row][elem]['text']

                if button == key:

                    if num_elem == 1:
                        self.Keyboards[pos].pop(row)

                    else:
                        self.Keyboards[pos][row].pop(elem)

                    self.Keys[pos].pop(key)

                    self.write_keyboard
                    return

    def rename_button(self, last_name, new_name, pos):
        keyboard = self.Keyboards[pos]
        num_row = len(keyboard)
        for row in range(0, num_row):
            num_elem = len(keyboard[row])
            for elem in range(0, num_elem):
                if last_name == self.Keyboards[pos][row][elem]['text']:
                    self.Keyboards[pos][row].pop(elem)
                    self.Keyboards[pos][row].insert(elem, {"text": new_name})
                    value = self.Keys[pos].pop(last_name)
                    self.Keys[pos][new_name] = value
                    self.write_keyboard
                    return

    @property
    def write_keyboard(self):
        db.write_keyboards(self.Keyboards, self.Keys)

    def create_Q_button(self, place: str, pos, button_name="?", value=[0]):
        try:
            Q_button = {"text": button_name}
            if '-' in place:
                place = place[1:-1]
                # elem
                ind_dash = place.index('-')
                row = int(place[:ind_dash])
                elem = int(place[ind_dash+1:])
                row_key = self.Keyboards[pos][row-1]
                num_elem = len(row_key)
                if elem > num_elem:
                    # last_elem
                    self.Keyboards[pos][row-1].insert(num_elem, Q_button)
                else:
                    self.Keyboards[pos][row-1].insert(elem-1, Q_button)

                self.Keys[pos][button_name] = value
                self.write_keyboard
                return True

            else:
                # row
                place = place[3:-3]
                row = int(place)
                keyboard = self.Keyboards[pos]
                num_row = len(keyboard)
                if row > num_row:
                    self.Keyboards[pos].insert(num_row, [Q_button])
                else:
                    self.Keyboards[pos].insert(row - 1, [Q_button])
                self.Keys[pos][button_name] = value
                self.write_keyboard
                return True
        except:
            return False

    @property
    def max_key(self):
        l = []
        for item in self.Keys:
            l.append(int(item))
        return max(l)

    def create_new_keyboard(self, last_pos, button):
        pos = str(self.max_key + 1)
        self.Keyboards[pos] = [[{"text": "رجوع"}]]
        self.Keys[pos] = {
            "رجوع": last_pos
        }
        self.Keys[last_pos][button] = pos
        self.write_keyboard
        return pos


    def get_postions_of_pos(self, pos):
        postions = []
        postions.append(pos)
        keyboard = self.Keys[pos]
        for button in keyboard:
            value = keyboard[button]
            if button != "رجوع" and type(value) is str and value != "#":
                postions += self.get_postions_of_pos(value)
        return postions

    def add_mat_to_btn(self, msg_id, pos):
        keys = self.Keys[pos]
        for button in keys:
            value = keys[button]
            if value == '###':
                self.Keys[pos][button] = [msg_id]
                self.write_keyboard
                return button

    def sel_btn_add_mat(self, button, pos):
        self.Keys[pos][button] = "###"
        self.write_keyboard

    def handle_button(self, button):
        button = button.replace('\n', " ")
        marks = ['_', '*', '[', ']', '(', ')', '~', '`', '>', '#', '+', '-', '=', '|', '{', '}', '.', '!']
        for mark in marks:
            if mark in button:
                button = button.replace(mark, f"\\{mark}")
        return button

    def count_write(self, l):
        db.count_write(l)

    @property
    def count_read(self):
        return db.Data["count"]

    def make_dic_map(self, channel_url, target, button_ex="", indent="   ", n=0):
        msg = ""
        Alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
        alpha = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
        if type(target) is str:
            if target != "#":

                f = self.count_read
                f['d'] = 0
                self.count_write(f)

                if str(n) in f['l']:
                    l = f['l'][str(n)]
                else:
                    l = 0
                    f['l'][str(n)] = 0
                if n:
                    f['l'][str(n)] += 1

                    button1 = self.handle_button(button_ex)
                    msg += f"{indent*n}{Alpha[l]}\\) {button1}\n"
                keyboard_target = self.Keys[target]

                for button in keyboard_target:
                    if button != "رجوع":
                        if button != "القائمة الرئيسية":
                            button_target = keyboard_target[button]
                            x = self.make_dic_map(channel_url, button_target, button, indent, n+1)
                            if x:
                                msg += x
                f['d'] = 0
                self.count_write(f)

        elif len(target) == 1:
            x = self.count_read
            d = x['d']

            button1 = self.handle_button(button_ex)
            ch_msg_id = self.get_ch_msg_id(target[0])
            if ch_msg_id:
                text = self.create_like_text(ch_msg_id, channel_url, button1)
                msg += f"{indent*n}{alpha[d]}\\- {text}\n"
                x['d'] += 1

            self.count_write(x)

        return msg

    def get_ch_msg_id(self, gr_msg_id):
        a = db.Data['map_msg_id']
        if str(gr_msg_id) in a:
            return a[str(gr_msg_id)]
        return False

    def create_like_text(self, msg_id, channel_url, text):
        return f"[{text}](https://t.me/{channel_url}/{msg_id})"

    def add_btn_keyboard(self, pos):
        keyboard = self.Keyboards[pos][:-1]
        countR = 0
        new_keyboard = []

        for row in keyboard:
            new_row = []
            countR += 1
            countE = 0
            new_keyboard.append([{'text': f'...{countR}...'}])

            for elem in row:
                countE += 1
                new_row.append({'text': f'.{countR}-{countE}.'})
                new_row.append(elem)
            new_row.append({'text': f".{countR}-{countE+1}."})
            new_keyboard.append(new_row)
        new_keyboard.append([{"text": f'...{countR+1}...'}])
        return new_keyboard
