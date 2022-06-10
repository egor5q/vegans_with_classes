import items


class ControlClass(object):
    def __init__(self):
        self.name = 'None'
        self.controller = 'None'

    def give_items(self):
        pass

    def give_weapon_list(self):
        pass


class Human(ControlClass):
    def __init__(self):
        self.name = 'Человек'
        self.controller = 'human'

    def give_items(self):
        return [items.Grenade, items.Adrenaline, items.Molotov]


class Bot(ControlClass):
    def __init__(self):
        self.name = 'Бот'
        self.controller = 'bot'

    def give_items(self):
        return [items.Grenade, items.Adrenaline, items.Molotov]
