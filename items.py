class Item(object):
    def __init__(self):
        self.name = 'None'
        self.id = 0
        self.energy_cost = 0
        self.energy_require = 0


class Adrenaline(Item):
    def __init__(self):
        self.id = 1
        self.name = 'Адреналин'


class Grenade(Item):
    def __init__(self):
        self.id = 2
        self.name = 'Граната'
        self.energy_cost = 2
        self.energy_require = 2

class Molotov(Item):
    def __init__(self):
        self.id = 3
        self.name = 'Коктейль Молотова'
        self.energy_cost = 2
        self.energy_require = 2
