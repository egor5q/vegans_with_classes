import addition_functions
import items
import unit_control_classes
from error_classes import NotItemClassError
import weapons


class Player(object):
    def __init__(self, id, name, photo = None):
        self.id = id
        self.name = name
        self.photo = photo
        self.hp = 4
        self.maxhp = 4
        self.energy = 5
        self.maxenergy = 5
        self.skills = []
        self.weapon = None
        self.act = None
        self.ready = False
        self.team = None
        self.stage = None
        self.dead = False
        self.nearplayers = [id]
        self.perekatcd = 0
        self.outgoingdmgs = []
        self.incomingdmgs = []
        self.controller = unit_control_classes.Human()

    def is_bot(self):
        if self.controller.controller == 'human':
            return False
        return True

    def take_item(self, item):
        if not isinstance(item, items.Item):
            raise NotItemClassError
        uid = addition_functions.get_unique_id(self.inventory)
        self.inventory[uid] = item

    def give_weapon_list(self):
        if self.is_bot():
            return [weapons.Pistol, weapons.Obrez, weapons.Baseball]
        return [weapons.Pistol, weapons.Obrez, weapons.Baseball]


