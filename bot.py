import random
import traceback
from telebot import types, TeleBot
import time
import threading
import telebot
import os
token = os.environ['token']
bot = TeleBot(token)
import game_object
import player_object
from error_classes import PlayerNotExistsError, PlayerAlreadyExistsError, GameAlreadyExistsError
from bot_functions import send_message

bot = telebot.TeleBot('1358702193:AAHC-wUOfvoOC_-7cU2dx8OZoevm_RBRT3M')


class Games(object):
    def __init__(self):
        self.games = {}

    def get_game_by_id(self, id) -> game_object.Game:
        return self.games[id]

    def add_game(self, m):
        new_game = game_object.Game(m)
        if new_game.id in self.games:
            raise GameAlreadyExistsError()
        self.games[new_game.id] = new_game
        self.games[new_game.id].set_cancel_timer(300)
        return self.games[new_game.id]

    def remove_game(self, game):
        if isinstance(game.canceltimer, threading.Timer):
            game.canceltimer.cancel()
        del self.games[id]

    def set_cancel_timer(self, game, seconds):
        t = threading.Timer(seconds, self.cancel_game, args=[game.id])
        t.start()
        game.canceltimer = t

    def cancel_game(self, id):
        try:
            self.remove_game(id)
        except KeyError:
            print('KeyError while cancelGame(', id, ')')
            return
        send_message(id, 'Игра отменена!')


games = Games()


@bot.message_handler(commands=['chatid'])
def giveweaponchatid(m):
    send_message(m.chat.id, str(m.chat.id))


@bot.message_handler(commands=['id'])
def idddd(m):
    if m.from_user.id != 441399484:
        return
    try:
        send_message(m.from_user.id, str(m.reply_to_message.from_user.id))
        send_message(m.chat.id, 'Got ID')
    except:
        send_message(m.chat.id, 'Error!')


@bot.message_handler(commands=['start'])
def start(m):
    send_message(m.chat.id, 'Приветствие')


@bot.message_handler(commands=['v_cancel'])
def cancelll(m):
    try:
        game = games.get_game_by_id(m.chat.id)
    except KeyError:
        send_message(m.chat.id, 'Игра еще не была создана (/v_prepare)!', reply_to_message_id=m.message_id)
        return
    if game.started:
        send_message(m.chat.id, 'Игра уже в процессе!', reply_to_message_id=m.message_id)
        return
    games.remove_game(game)
    send_message(m.chat.id, 'Игра удалена!')


@bot.message_handler(commands=['v_join'])
def join(m):
    try:
        game = games.get_game_by_id(m.chat.id)
    except KeyError:
        send_message(m.chat.id, 'Игра еще не была создана (/v_prepare)!', reply_to_message_id=m.message_id)
        return
    if game.started:
        send_message(m.chat.id, 'Игра уже в процессе!', reply_to_message_id=m.message_id)
        return
    try:
        player = game.add_player(m.from_user.id, m.from_user.first_name)
    except PlayerAlreadyExistsError:
        send_message(m.chat.id, 'Вы уже в игре!', reply_to_message_id = m.message_id)
        return
    send_message(m.chat.id, player.name+' присоединился!')


@bot.message_handler(commands=['flee'])
def fleee(m):
    try:
        game = games.get_game_by_id(m.chat.id)
    except KeyError:
        send_message(m.chat.id, 'Игра еще не была создана (/v_prepare)!', reply_to_message_id=m.message_id)
        return
    if game.started:
        send_message(m.chat.id, 'Игра уже в процессе!', reply_to_message_id=m.message_id)
        return
    try:
        game.remove_player(m.from_user.id)
        send_message(m.chat.id, m.from_user.first_name+' сбежал!')
    except KeyError:
        send_message(m.chat.id, 'Вы не в игре!', reply_to_message_id=m.message_id)
        return


@bot.message_handler(commands=['v_prepare'])
def startgame(m):
    try:
        games.add_game(m)
    except GameAlreadyExistsError:
        send_message(m.chat.id, 'Игра уже существует, /v_join для присоединения.', reply_to_message_id=m.message_id)
        return
    send_message(m.chat.id, 'Подготовка к игре запущена! /v_join для присоединения, /v_go для запуска.')


@bot.message_handler(commands=['v_go'])
def gogame(m):
    try:
        game = games.get_game_by_id(m.chat.id)
    except KeyError:
        send_message(m.chat.id, 'Игра еще не была создана (/v_prepare)!', reply_to_message_id=m.message_id)
        return
    if game.started:
        send_message(m.chat.id, 'Игра уже в процессе!', reply_to_message_id=m.message_id)
        return
    if game.get_players_amount < game.minimum_players:
        send_message(m.chat.id, 'Минимальное число игроков для данного режима - ', game.minimum_players, '!')
        return
    game.init_game()
