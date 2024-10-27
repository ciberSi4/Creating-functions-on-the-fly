# Домашнее задание по теме "Создание функций на лету"

# Lambda-функция
first = 'Мама мыла раму'
second = 'Рамена мало было'
result = list(map(lambda x, y: x == y, first, second))
print(result)

# Замыкание
def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'a', encoding="utf8") as file:
            for item in data_set:
                file.write(str(item) + '\n')
    return write_everything

# Использование функции
write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

# Метод __call__
from random import choice

class MysticBall:
    def __init__(self, *words):
        self.words = words

    def __call__(self):
        return choice(self.words) # случайным образом выбирает одно из слов переданных при создании объекта класса

# Использование класса
first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())

# Эти три примера демонстрируют различные аспекты программирования на Python: использование lambda-функций, замыканий и методов классов