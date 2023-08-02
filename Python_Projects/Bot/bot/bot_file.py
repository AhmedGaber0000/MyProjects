from Update import *


bot.setwebhook()
bot.set_commands()
bot.sendMessage(master_id, "Hello, Eng Ahmed Gaber")
app = Flask(__name__)


@app.route('/', methods=["POST"])
def Mybot():
    r = request.get_json()
    update = Update(r)
    try:

        if update.type == "private":
            Pri_msg(update.message).run()

        elif update.type == "my_chat_member":
            db.add_channel_id(update.channel_name, update.channel_id)

        elif update.type == 'poll_answer':
            if update.poll_id == main_poll_id_num:
                user = User(update.chat_id_poll).user_has_ans_poll()

        elif update.type == 'chat_join_request':
            user = User(update.chat_join_id)
            bot.invint_link(user.chat_id, user.is_approved, update.channel_id_link)

        elif update.type == 'callback_query':
            chat_id, msg_id = update.callback_query
            User(chat_id).approve_user(msg_id)

    except:
        trace_back = traceback.format_exc()
        trace_back.replace("\n", "\n\n")
        bot.sendMessage(master_id, update.string_update)
        bot.sendMessage(master_id, trace_back)

    db.Write_Data()
    return Response('ok', status=200)


if __name__ == '__main__':
    app.run()
