import time

from fontTools.misc.cython import returns
from openpyxl.utils import coordinate_to_tuple
from copy import deepcopy
from random import randint


def check_even(number: int):
    """ 📌 Задача 1. Чётный или нечётный

    Необходимо написать функцию:
    `check_even(number)`

    Функция должна принимать число и с помощью тернарного оператора возвращать строку "Чётное" или "Нечётное".

    Пример:
    print(check_even(4))
    print(check_even(7))
    print(check_even(0))

    Ожидаемый вывод:
    Чётное
    Нечётное
    Чётное
    """
    numbers = "Чётное" if number % 2 == 0 else "Нечётное"
    return numbers


def lab_access(name):
    """📌 Задача 2. Пропуск в лабораторию

Необходимо написать функцию:
lab_access(name)

Функция должна с помощью тернарного оператора вернуть строку "Добро пожаловать, Артём!" если имя равно "Артём", и "Доступ запрещён" в любом другом случае.

Пример:
print(lab_access("Артём"))
print(lab_access("Иван"))

Ожидаемый вывод:
Добро пожаловать, Артём!
Доступ запрещён
"""
    entrance = "Добро пожаловать, Артём" if name == "Артём" else "Доступ запрещён"
    return entrance


def robot_zone(distance):
    """
    📌 Задача 3. Датчик робота

Необходимо написать функцию:
robot_zone(distance)

Функция принимает расстояние в сантиметрах и с помощью тернарного оператора возвращает:
- "СТОП" — если расстояние меньше 10
- "ЕДЕМ" — если расстояние 10 и больше

Пример:
print(robot_zone(5))
print(robot_zone(25))
print(robot_zone(10))

Ожидаемый вывод:
СТОП
ЕДЕМ
ЕДЕМ
    """
    movement = "ЕДЕМ" if distance >= 10 else "СТОП"
    return movement


def check_part(parts, part_name):
    """
📌 Задача 4. Инвентарь

Необходимо написать функцию:
check_part(parts, part_name)

Функция принимает список деталей `parts` и название детали `part_name`. С помощью тернарного оператора возвращает:
- "Есть в наличии" — если деталь есть в списке
- "Нет в наличии" — если детали нет

Пример:
parts = ["мотор", "датчик", "кабель", "колесо"]

print(check_part(parts, "мотор"))
print(check_part(parts, "камера"))

Ожидаемый вывод:
Есть в наличии
Нет в наличии

    """
    presence = "Есть в наличии" if part_name in parts else "Нет в наличии"
    return presence


def minecraft(coordinates: tuple):
    """
    📌 Задача 1. Координаты дома
У дома в minecraft есть координаты – они хранятся в кортеже.
Необходимо распаковать кортеж в три отдельные переменные: x, y, z
Затем вывести каждую координату на отдельной строке.
    """
    x,y,z = coordinates
    return f"координаты дома x = {x},y = {y},z = {z}",


def commands(command: list):
    """
    📌 Задача 2. Команда разработчиков
Список содержит имена трёх участников команды. Необходимо распаковать список в три переменные: lead, developer, tester. Затем вывести каждого в формате, указанном ниже.

Ожидаемый вывод:
Лид: Артём
Разработчик: Максим
Тестировщик: Катя
    """
    lead, developer, tester = command
    return f"Лид: {lead}\nРазработчик: {developer}\nТестировщик: {tester}"


def squares():
    """
    📌 Задача 3. Таблица квадратов
Необходимо с помощью list comprehension и range создать список квадратов чисел от 1 до 10.

Ожидаемый вывод:
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    """
    line = [i ** 2 for i in range(1,11)]
    return line


def details(parts):
    line = [i.upper() for i in parts]
    return line


def check_battery(charge):
    """
    📌 Задача 1. Заряд батареи
Необходимо написать функцию:
check_battery(charge)
Функция принимает заряд батареи в процентах и с помощью тернарного оператора возвращает:
"Заряд в норме" — если заряд 20 и выше
"Зарядите батарею!" — если заряд меньше 20
Пример:
print(check_battery(85))
print(check_battery(15))
print(check_battery(20))
Ожидаемый вывод:
Заряд в норме
Зарядите батарею!
Заряд в норме
    """
    battery = "Заряд в норме" if charge >= 20 else "Зарядите батарею!"
    return battery


def check_password(password):
    """
    📌 Задача 2. Пароль
Необходимо написать функцию:
check_password(password)
Функция принимает строку и с помощью тернарного оператора возвращает:
"Вход разрешён" — если длина пароля 8 символов и больше
"Пароль слишком короткий" — если меньше 8 символов
Пример:
print(check_password("qwerty"))
print(check_password("qwerty123"))
print(check_password("12345678"))
Ожидаемый вывод:
Пароль слишком короткий
Вход разрешён
Вход разрешён
    """
    password2 = "Вход разрешён" if len(password) >= 8 else "Пароль слишком короткий"
    return password2


def multiples_3():
    """
    📌 Задача 3. Числа кратные 3
Необходимо с помощью list comprehension и range создать список чисел от 1 до 30, которые делятся на 3 без остатка.
Ожидаемый вывод:
[3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
    """
    line = [i for i in range(1,31) if i % 3 == 0]
    return line


def len_text(words):
    """
    📌 Задача 4. Длина каждого слова
Дан список слов. Необходимо с помощью list comprehension создать новый список, где каждый элемент — это длина соответствующего слова.
Пример:
words = ["робот", "EV3", "датчик", "мотор", "экран"]
Ожидаемый вывод:
[5, 3, 6, 5, 5]
    """
    number = [len(i) for i in words]
    return number


def excellent_students(grades):
    """
    📌 Задача 5. Фильтр отличников
Дан список оценок. Необходимо с помощью list comprehension создать новый список, в котором останутся только оценки 5, и заменить каждую на строку "Отлично".
Пример:
grades = [4, 5, 3, 5, 4, 5, 2, 5]
Ожидаемый вывод:
['Отлично', 'Отлично', 'Отлично', 'Отлично']
    """
    line = ["Отлично" for i in grades if i == 5]
    return line


area = lambda a,b: a*b


drop_last = lambda line_int:line_int // 10


max3 = lambda a,b,c: max(a,b,c)


full_name = lambda a,b: a.capitalize()+" "+b.capitalize()


def average(*args):
    """
    📌 Задача 5. Средний балл
Необходимо написать функцию:
average(*args)
Функция принимает любое количество оценок и возвращает их среднее значение, округлённое до 2 знаков после запятой. Использовать round().
Пример:
print(average(5, 4, 3, 5, 4))
print(average(3, 3, 4))
print(average(5, 5, 5, 5))
Ожидаемый вывод:
4.2
3.33
5.0
    """
    if not args:  # на случай, если оценок нет — чтобы не делить на ноль
        return 0
    return round(sum(args) / len(args), 2)


def part_card(**kwargs):
    """
    📌 Задача 6. Карточка детали
Необходимо написать функцию:
part_card(**kwargs)
Функция принимает характеристики детали и выводит каждую в формате ключ: значение. В конце выводит общее количество характеристик.
Пример:
part_card(name="Мотор",type="большой",voltage=9,rpm=160)
Ожидаемый вывод:
name: Мотор
type: большой
voltage: 9
rpm: 160
Всего характеристик: 4
    """
    for key, value in kwargs.items():
        print(f"{key}: {value}")
    print(f"Всего характеристик: {len(kwargs)}")


def number():
    """
    📌 Задача 1. Обработка чисел
Дан список:
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
Необходимо создать новый список:
для чётных чисел записать "чётное"
для нечётных чисел записать "нечётное"
Ожидаемый результат:
["нечётное", "чётное", "нечётное", "чётное", "нечётное", "чётное", "нечётное", "чётное"]
    """
    numbers = [1, 2, 3, 4, 5, 6, 7, 8]
    line = ["Чётное" if i % 2 == 0 else "Нечётное" for i in numbers]
    return line


def temperature():
    """
    📌 Задача 2. Температура
Дан список температур:
temperatures = [-10, 5, 18, -3, 25, 0, 12]
Необходимо создать новый список:
отрицательную температуру заменить на "мороз"
остальные значения оставить без изменений
Ожидаемый результат:
["мороз", 5, 18, "мороз", 25, 0, 12]
    """
    temperatures = [-10, 5, 18, -3, 25, 0, 12]
    line = ["Мороз" if i < 0 else i for i in temperatures]
    return line


def number_2():
    """
    📌 Задача 3. Квадраты чисел
Дан список:
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
Необходимо получить новый список, содержащий квадраты только нечётных чисел.
Ожидаемый результат:
[1, 9, 25, 49]
    """
    numbers = [1, 2, 3, 4, 5, 6, 7, 8]
    line = [i ** 2 for i in numbers if i % 2 != 0]
    return line


def price():
    """
    📌 Задача 4. Цены товаров
Дан список цен:
prices = [500, 1200, 750, 3000, 450, 2000]
Необходимо создать новый список, в котором:
товары дешевле 1000 рублей остаются без изменений;
на товары стоимостью 1000 рублей и больше предоставляется скидка 20%. (Чтобы была скидка в 20% нужно умножить число на 0.8)
Ожидаемый результат:
[500, 960.0, 750, 2400.0, 450, 1600.0]
    """
    prices = [500, 1200, 750, 3000, 450, 2000]
    line = [i if i < 1000 else i * 0.8 for i in prices]
    return line


def dlin():
    """
    📌 Задача 5. Обработка слов
Дан список:
words = ["cat", "elephant", "dog", "computer", "sun", "python"]
Необходимо создать новый список:
если длина слова больше 4 символов — привести его к верхнему регистру;
если длина слова 4 или меньше — оставить слово как есть;
в новый список должны попасть только слова, содержащие букву "o".
    """
    words = ["cat", "elephant", "dog", "computer", "sun", "python"]
    line = [i.upper() if len(i) > 4 else i for i in words if "o" in i]
    return line


def score():
    """
    📌 Задача 6. Результат игрока
Дан список игроков с набранными очками:
scores = [120, 45, 300, 80, 510, 210, 15]
Необходимо создать новый список:
игроки с результатом 100 и больше получают "прошёл"
игроки с результатом меньше 100 получают "не прошёл"
при этом в новый список должны попасть только результаты игроков, набравших нечётное количество очков.
Ожидаемый результат:
["не прошёл", "прошёл", "прошёл"]
    """
    scores = [120, 45, 300, 80, 510, 210, 15]
    line = ["Прошёл" if i >= 100 else "Не прошёл" for i in scores if i % 2 != 0]
    return line


def minecraft_():
    invetory = [
        ["меч","щит"],
        ["зелье","еда"]
    ]
    invetory_2 = deepcopy(invetory)
    invetory_2[1].append("факел")
    invetory_2[0][0] = ["лук"]
    return invetory, invetory_2


def profile():
    players = [
    {
    "name": "Иван",
    "level": 10,
    "items": ["меч", "зелье"]
    },
    {
    "name": "Олег",
   "level": 7,
    "items": ["лук"]
    }
    ]
    players_2 = deepcopy(players)
    players_2[0]["level"] = 15
    players_2[0]["items"].append("щит")
    players_2.append({"name": "Анна",
                      "level": 7,
                      "items": ["лук"]
                      })
    return players, players_2


def else_in_for(numbers):
    for i in numbers:
        if i == 4:
            print("4 нашлась")
            break
    else:
        print("4 не найдена")


def copy_settings():
    settings = {
    "graphics": {
    "quality": "high",
    "resolution": [1920, 1080]
    },
    "sound": {
    "music": 80,
    "effects": 70
    }
    }
    settings_2 = deepcopy(settings)
    settings_2["graphics"]["quality"] = "low"
    settings_2["graphics"]["resolution"] = [1280,720]
    print(settings)
    print(settings_2)


shop = lambda price: price * 0.8


check = lambda word: "длинное"if len(word) >= 10 else "короткое"


def total_prices(*prices):
    print(sum(prices))


def poisk(parts):
    for i in parts:
        if i == "камера":
            return "Камера есть!"

    else:
        return "Камеры нет"




def i_dont_no(grades):
    for i in grades:
        if i == 2:
            return "Есть двойка!"

    else:
        return "Отличная неделя!"


def countdown(n):
    print(n)
    if n == 1:
        return "Пуск!"
    else:
        return countdown(n - 1)


def sum_to(n):
    if n == 0:
        return 0
    else:
        return n + sum_to(n - 1)


def count_parts(box):
    total = 0
    for i in box:
        if isinstance(i, int):
            total += i
        elif isinstance(i, list):
            total += count_parts(i)
    return total


box = [3, [2, 5], [1, [4, 2]], 6]
(count_parts(box))


def count_depth(folder):
    max_depth = 1

    for item in folder:
        if isinstance(item, list):
            current_depth = 1 + count_depth(item)
            max_depth = max(max_depth, current_depth)

    return max_depth

folder = ["файл1.txt", ["файл2.txt", ["файл3.txt"]], "файл4.txt"]
(count_depth(folder))


def shoot(name):
    print(f"{name} стреляет!")

def super_attack(name):
    print(f"{name} использует супер!")

def heal(name):
    print(f"{name} лечится!")


actions = [shoot, super_attack, heal]

br_name = "Спайк"


def to_upper(text):
    return text.upper()

def to_lower(text):
    return text.lower()

def apply(func, text):
    return func(text)


def square(n):
    return n ** 2

def cube(n):
    return n ** 3
math_ops = {
    "square": square,
    "cube": cube
}


def cheap(prices):
    return prices * 0.9


def city(cities):
    return len(cities)


def age(ages):
    return ages >= 18


def i_dont_no_2(words):
    return len(words) > 0


sorted_numbers = lambda x: x % 3


word = lambda x:x[1]


def decorator(func):
    def wrapper(*args,**kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        end = time.time()
        print(f"время выполнения функции {end-start}")
        return result
    return wrapper

@decorator
def poisc(parts):
    for i in parts:
        if i.lower() == "камера":
            return "Камера есть!"

    else:
        return "Камеры нет"

@decorator
def i_dont_know_3(tttttt:str):
    return tttttt.upper()


if __name__ == '__main__':
    print(poisc(["камера","hfjfg","hdydy"]))
