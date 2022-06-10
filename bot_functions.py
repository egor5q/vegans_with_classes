import bot_init
import traceback


def send_message(id, text, bot=bot_init.bot, reply_to_message_id=None):
    try:
        msg = bot.send_message(id, text)
        return msg
    except:
        print(traceback.format_exc())
        return None