class AttackEffect(object):
    def __init__(self):
        self.name = 'Неизвестно'
        self.chance = 50


class Stun(AttackEffect):
    def __init__(self):
        super().__init__()
        self.name = 'Оглушение'