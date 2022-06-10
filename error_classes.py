class PlayerNotExistsError(Exception):
    def __init__(self, message='Игрока с таким ID не существует!'):
        super().__init__(message)


class PlayerAlreadyExistsError(Exception):
    def __init__(self, message='Игрок с таким ID уже существует!'):
        super().__init__(message)


class GameAlreadyExistsError(Exception):
    def __init__(self, message='Игра с таким ID уже существует!'):
        super().__init__(message)


class BotTechWorkError(Exception):
    def __init__(self, message='Проводятся технические работы, невозможно создать/запустить игру!'):
        super().__init__(message)


class GameAlreadyStartedError(Exception):
    def __init__(self, message='Игра уже запущена!'):
        super().__init__(message)


class NotItemClassError(Exception):
    def __init__(self, message='В функцию был передан класс, отличный от класса items.Item!'):
        super().__init__(message)