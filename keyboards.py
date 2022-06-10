from telebot import types

def get_weapon_select_keyboard(player):
    kb = types.InlineKeyboardMarkup()
    kbs = []
    for ids in player.give_weapon_list():
        kbs.append(types.InlineKeyboardButton(text='a', callback_data='b'))
    for ids in kbs:
        kb.add(types.InlineKeyboardButton(text='a', callback_data='b'))
