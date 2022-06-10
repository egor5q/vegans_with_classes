import random


def get_unique_id(from_dict): # Генерирует и возвращает случайный уникальный ID для переданного словаря
    random_id = random.randint(1, 10000)
    while random_id in from_dict:
        random_id = random.randint(1, 10000)
    return random_id

def check_existence_by_id(from_dict, id): # Проверяет, существует ли в переданном словаре from_dict объект с полем id, равном по значению переданной переменной id
    for ids in from_dict:
        if ids.id == id:
            return True
    return False
