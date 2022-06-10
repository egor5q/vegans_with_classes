class Weapon(object):
    def __init__(self):
        self.id = 1
        self.name = 'None'
        self.cubes = 3
        self.bonus_dmg = 0
        self.bonus_accuracy = 2
        self.ranged = False


class Pistol(Weapon):
    def __init__(self):
        self.id = 2
        self.name = 'Пистолет'
        self.cubes = 3
        self.bonus_dmg = 0
        self.bonus_accuracy = 3
        self.ranged = True


class Obrez(Weapon):
    def __init__(self):
        self.id = 3
        self.name = 'Обрез'
        self.cubes = 4
        self.bonus_dmg = 0
        self.bonus_accuracy = 2
        self.ranged = True


class Baseball(Weapon):
    def __init__(self):
        self.id = 4
        self.name = 'Бейсбольная бита'
        self.cubes = 3
        self.bonus_dmg = 0
        self.bonus_accuracy = 2
        self.ranged = False