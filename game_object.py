import threading
import error_classes
import random
from error_classes import PlayerNotExistsError, PlayerAlreadyExistsError, GameAlreadyStartedError, NotItemClassError
import player_object
from bot_functions import send_message
import addition_functions


class Game(object):
    def __init__(self, m, test = False, teamplay = False, rats = False, bossfight = False, dungeon = False,
                 rat_difficulty = 1, dungeon_type = 'rhino', tournier = False, allrandom = False, pureduel = False, testequipgame = False,
                 magictournier = False, minimum_players = 2):
        self.id = None
        self.title = 'Неизвестно'
        self.players = {}
        self.msg = None
        self.turn = 1
        self.text = 'Ход 1:\n'
        self.started = False
        self.timer = None
        self.minimum_players = minimum_players
        self.effecttext = None
        self.stage = None
        self.canceltimer = None
        self.creator = m.from_user.id

    def get_player_by_id(self, id) -> player_object.Player:
        if id not in self.players:
            raise PlayerNotExistsError()
        return self.players[id]

    def add_player(self, id, name) -> player_object.Player:
        if id in self.players:
            raise PlayerAlreadyExistsError()
        player = player_object.Player(id, name)
        self.players.update({player.id: player})
        player_to_return = self.players[id]
        player_to_return.team = player_to_return.id
        return player_to_return

    def remove_player(self, id):
        del self.players[id]

    def check_player_in_game(self, id):
        if id in self.players:
            return True
        return False

    def get_players_amount(self):
        amount = 0
        for player in self.players:
            amount += 1
        return amount

    def init_game(self):
        if self.started:
            raise GameAlreadyStartedError
        self.started = True
        self.canceltimer.cancel()
        send_message(self.id, 'Игра начинается!')
        self.give_items_to_players()
        self.select_weapons()

    def give_items_to_players(self):
        for ids in self.players:
            player = self.get_player_by_id(ids.id)
            items_get = []
            from_list = player.controller.give_items()
            need_items = 2
            while len(items_get) < need_items:
                if len(from_list) == len(items_get):
                    break
                item = random.choice(from_list)
                try:
                    while addition_functions.check_existence_by_id(items_get, item.id):
                        item = random.choice(from_list)
                except AttributeError:
                    print('AttributeError in game_object.Game.give_items_to_players()')
                    return
                items_get.append(item)
            for ids in items_get:
                try:
                    player.take_item(ids)
                except NotItemClassError:
                    print('Попытка передать ', ids, ' вместо класса items.Item в функции game_object.Game.give_items_to_players()!')

    def select_weapons(self):
        for ids in self.players:
            player = self.get_player_by_id(ids.id)
            player.stage = 'select_weapons'
            player.ready = False


