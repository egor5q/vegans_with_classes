class Skill(object):
    def __init__(self):
        self.id = None
        self.name = 'Неизвестно'
        self.cd = 3  # время перезарядки скилла после применения
        self.cd_on_start = 0 # время перезарядки скилла при старте игры
        self.energy_cost = 0 # сколько энергии отнимет применение скилла
        self.energy_require = 0 # сколько энергии нужно, чтобы скилл можно было активировать
        self.kb = None
