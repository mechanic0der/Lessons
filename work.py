def lesson_1():
    b = int(input("Введите первое число:"))
    a = int(input("Введите второе число:"))
    print(a + b)
    print(a - b)
    print(a * b)
    print(a / b)
    print(a % b)
    print(a // b)


def lesson_2():
    """
    Добрый день! Задание к следующему занятию:
    Написать программу, которая выполняет следующие действия:
    1. Запрашивает у пользователя его имя и сохраняет в переменную.
    2. Запрашивает возраст пользователя и сохраняет в переменную.
    3. Выводит приветствие с именем пользователя.
    4. Вычисляет и выводит возраст пользователя через год (текущий возраст + 1) в формате:
    "Через год Вам будет: X", где X - результат вычисления
    """
    # 1. Запрашивает у пользователя его имя и сохраняет в переменную.
    name = input("Введите ваше имя: ").strip()  # Тип - строка
    while len(name) == 0:
        print("Вы не ввели имя!")
        name = input("Введите ваше имя: ").strip()
    # Имя пользователя уже точно не пустое
    age = input("Введите ваш возраст: ").strip()
    age_len = len(age)
    age_is_digit = all([s.isdigit() for s in age])
    while age_len == 0 or not age_is_digit:
        print("Введите настоящий возраст!")
        age = input("Введите ваш возраст: ").strip()
        age_len = len(age)
        age_is_digit = all([s.isdigit() for s in age])
    age = int(age)  # Тип - целое число, называется Integer, а функция int() позволяет преобразовать строку в число
    print("Привет,", name)
    print("Через год Вам будет:", age + 1)


def lesson_3():
    name = input("Введите название товара: ")
    count = int(input("Введите количество товара: "))
    price = int(input("Введите цену товара: "))
    summary = count * price
    d = int(input("Введите количество денег: "))
    if d >= summary:
        print(f"Вы можете купить товар {name}. Ваша сдача: {d - summary}")
    else:
        print(f"Вы не можете купить товар. Вам не хватает денег: {summary - d}")


def lesson_4():
    name = input("Введите название фильма: ")
    price = int(input("Введите цену билета: "))
    age = int(input("Введите возраст зрителя: "))
    count = int(input("Введите количество билетов: "))
    if age < 6:
        print("Вы не можете смотреть этот фильм!")
    else:
        print(f"Фильм:{name}\nБилетов: {count}\nСумма к оплате: {price * count} руб.")


def lesson_5():
    name = input("Введите название товара: ")
    price = int(input("Введите цену товара: "))
    delivery = input("Нужна доставка: ")
    if delivery == "да Да":
        print(f"Товар: {name}\nЦена товара: {price} руб.\nДоставка: есть.\nИтог к оплате: {price + 200} руб.")
    else:
        print(f"Товар: {name}\nЦена товара: {price} руб.\nДоставка: нет.\nИтог к оплате: {price} руб.")


def lesson_6():
    print("\U0001f988")


def lesson_7():
    name = input("Введите слово: ")
    print(f"{name[0]}\n {name[-1]} {len(name)}")


def lesson_8():
    name = input("Введите слово: ")
    print(f"{name[::-1]}\n{name[:3]}")


def lesson_9():
    name = input("Введите слово: ")
    a = (input("какую букву вы хотите заменить: "))
    d = (input("на какую букву вы хотите заменить: "))
    print(f"{name.replace(a, d)}")


def lesson_10():
    name, surname = input('введите имя-фамилия: ').split("-")[:2]
    print(f"Имя: {name}\nФамилия: {surname}")


def lesson_11():
    name = input("Введите слово:")
    print(f"{name[1]}\n{name[1:-1]}\n{name[0:-1]}")


def lesson_12():
    a = int(input("Введите первое число: "))
    b = int(input("Введите второе число: "))
    c = input("Введите действие: ")
    if c == "+":
        print(a + b)
    elif c == "-":
        print(a - b)
    elif c == "*":
        print(a * b)
    elif c == "/":
        if b == 0:
            print("Деление на ноль невозможно!")
        else:
            print(a / b)
    else:
        print("Вы ввели не верное действие")


def lesson_13():
    a = int(input("Введите первое число: "))
    b = int(input("Введите второе число: "))
    if not (a != 7 or (a >= 4 and b == 2)):
        print(
            "fjhdkjfghdjkfghdkjfghdkjfghdkjfghdkjfghdkjfghdkjfghdkjfghdkjfghdkjfghdkjfghdkjfghdkjfghdkjfghdkjfghdkjfghdkjfghdk")


def lesson_14():
    name = input("Введите строку : ")
    if "z" in name:
        print("Нельзя вводить z")


def lesson_15():
    name = int(input("Введите дельное число : "))
    if name % 2 == 0:
        print("Число четное")
    else:
        print("Число не четное")


def lesson_16():
    name = input("Введите пароль : ")
    ssss = input("Введите пароль еще раз : ")
    if name == ssss:
        print("Пароли совпадают")
    else:
        print("Пароли не совпадают")


def lesson_17():
    name = int(input("Введите число : "))
    if name == 7:
        print("ты угадал")
    elif name < 7:
        print("число меньше")
    else:
        print("число больше")


def lesson_18():
    name = input("Введите почту : ")
    if "@" and "." in name:
        print("Почта верная")
    else:
        print("Почта не верная")


def lesson_19():
    a = 5
    b = 100
    poiuyt = 0
    while a < 2 and b > 95:
        print("vdcadfaygsifugasdifuysdifyuiyfouweyoruwy;rouwya;yieuryiuyglusfdyfedfwsrRTE")
        a -= 1
    name = input("Введите почту : ")
    while "@" and "." in name:
        print(
            "sdjjgcdcfwjegrhlewjtowjehtowjehtowjehtowjehtowjehtowjehtowjehtowjehtowjehtowjehtowjehtowjehtowjehtowjehtowjehtowjehto")
        name = input("Введите почту : ")
        poiuyt += 1
    print(poiuyt)


def lesson_20():
    name = int(input("Введите число : "))
    if name % 10 == 5:
        print("Число оканчивается на 5")
    else:
        print("Число не оканчивается на 5")


def lesson_21():
    n = int(input("Введите число : "))
    v = 0
    while v < n:
        v += 1
        print(v)


def lesson_22():
    """ Задача № 3 от 19.03.2026
        Обратный отсчёт
        Пользователь вводит число.
        Программа выводит числа от него до 0.
        Пример:
        Ввод: 5
        Вывод: 5 4 3 2 1 0
    """
    b = int(input("Введите число : "))
    while -1 < b:
        print(b)
        b -= 1


def lesson_23():
    """ Задача № 4 от 19.03.2026
        Сумма чисел
        Пользователь вводит число n.
        Найти сумму чисел от 1 до n
    """
    n = int(input("Введите число : "))
    v = 0
    a = 0
    while v < n:
        v += 1
        a += v
    print(a)


def lesson_24():
    """
        Задача № 5 от 19.03.2026
        Найти максимальное
        Пользователь вводит числа, пока не введёт 0.
        Нужно найти самое большое число, которое ввёл пользователь
    """
    print("Вводите числа по очереди. Если хотите закончить то введите 0.")
    a = int(input("Введите число: "))
    e = 1000000000000000000000000000000000000000000000000000000000000000000000000000000
    while a != 0:
        if e > a:
            e = a
        a = int(input("Введите число: "))
    print(e)


def lesson_25():
    """ Задача № 6 от 19.03.2026
        Чётные числа
        Пользователь вводит число n.
        Вывести все чётные числа от 1 до n
    """
    n = int(input("Введите число : "))
    a = 1
    while a < n + 1:
        if a % 2 == 0:
            print(a)
        a += 1


def lesson_26():
    n = int(input("Введите число : "))
    e = 0
    while n > e:
        e += 1
        print(e)
    name = input("Введите имя : ")
    print(f"{name[::-1]}")
    g = 0
    b = 0
    r = int(input("Введите число : "))
    while r > b:
        b += 1
        g += b
        print(g)
    i = input("Введите строку : ")
    print(f"{len(i)}")
    y = int(input("Введите стоимость товара : "))
    h = int(input("Введите количество товара : "))
    if h > 10:
        print("Скидка 100% вы должны заплатить 0 рублей")
    else:
        print(f"Вы должны заплатить {y * h} рублей")
    x = int(input("Введите число : "))
    while x != 0:
        print("Введите число 0")
        x = int(input("Введите число : "))


def lesson_27():
    n = int(input("Введите число : "))
    if n > 0:
        print("Положительное число")
    elif n < 0:
        print("Отрицательное число")
    else:
        print("Ноль")


def lesson_28():
    n = 0
    while n < 5:
        n += 1
        print(n)


def lesson_29():
    n = int(input("Введите число : "))
    e = 0
    while e < n:
        e += 1
        print(e)


def lesson_30():
    n = int(input("Введите число : "))
    r = 1
    while n != 0:
        r += 1
        n = int(input("Введите число : "))
    print(r)


def lesson_31():
    n = int(input("Введите число : "))
    e = 0
    while n != 0:
        e += n
        n = int(input("Введите число : "))
    print(e)


def lesson_32():
    n = int(input("Введите число : "))
    print(n % 10)


def lesson_33():
    n = int(input("Введите число : "))
    if n % 10 == 5:
        print("Число оканчивается на 5")
    else:
        print("Число не оканчивается на 5")


def lesson_34():
    n = int(input("Введите число : "))
    if n % 3 == 0:
        print("Число делится на 3")
    else:
        print("Число не делится на 3")


def lesson_35():
    qwerty = "werdfg"
    qwerty = qwerty.replace("g", "🦈")
    print(qwerty)
    print(len(qwerty))
    print(2 // 3)
    a = 5
    print(a + 1)
    print(a)


def lesson_36():
    n = 0
    while n < 8:
        n += 1
        print(f"Отработано {n} часов")
    print("Отработано 8 часов")


def lesson_37():
    n = int(input("Введите каличество денег : "))
    p = int(input("Введите цену товара : "))
    print(f"Вы можете купить {n // p} товаров")
    print(f"У вас останится {n % p} денег")


def lesson_38():
    n = 7
    m = int(input("Введите число : "))
    while m != n:
        if m < n:
            print("Число больше")

        else:
            print("Число меньше")
        m = int(input("Введите число : "))

    print("Вы угадали")


def lesson_39():
    """ Считаем сумму цифр числа """
    n = int(input("Введите число : "))  # 5454 -> 5450
    e = 0
    while n > 0:
        o = n % 10
        e += o
        n //= 10
    print(e)


def lesson_40():
    n = int(input("Введите число : "))
    e = 0
    while n > 0:
        n //= 10
        e += 1
    print(e)


def lesson_41():
    n = int(input("Введите число : "))
    while n > 0:
        print(n)
        n -= 1


def lesson_42():
    name = input("Введите строку: ")
    print(len(name))


def lesson_43():
    name = input("Введите слово: ")
    print(name.upper())


def lesson_44():
    name = input("Введите слово: ")
    print(name.lower())


def lesson_45():
    name = input("Введите строку: ")
    print(f"{name} теперь :{name.replace(name, "йцукенгш")}")


def lesson_46():
    name = input("Введите число: ")
    print(name.isdigit())


def lesson_47():
    for i in range(10):
        print(i + 1)
    for i in range(55555, 100000):
        print(i)
    for i in range(10, 100, 89):
        print(i)


def lesson_48():
    name = int(input("Введите число: "))
    for i in range(2, name + 1):
        print(i)


def lesson_49():
    name = int(input("Введите число: "))
    for i in range(0, name, 2):
        print(i)


def lesson_50():
    name = int(input("Введите число: "))
    for i in range(name):
        if i % 3 == 1:
            print(i)


def lesson_51():
    for i in range(10, 0, -1):
        print(i)


def lesson_52():
    for i in range(1, 10):
        print(i)


def lesson_53():
    for i in range(5, 15):
        print(i)


def lesson_54():
    for i in range(10, 0, -1):
        print(i)


def lesson_55():
    for i in range(1, 20, 2):
        print(i)


def lesson_56():
    for i in range(1, 20):
        if i % 2 == 0:
            print(i)


def lesson_57():
    for i in range(1, 30):
        if i % 3 == 2:
            print(i)


def lesson_58():
    for i in range(1, 50):
        if i % 5 == 0:
            print(i)


def lesson_59():
    e = 0
    for i in range(1, 101):
        if i % 2 == 0:
            e += i
    print(e)


def lesson_60():
    for i in range(1, 10):
        print(i)
        if i == 5:
            break
    print("asdfghjkl")


def lesson_61():
    for i in range(1, 10):
        if i == 22:
            continue
        print(i)
        print("asdfghjkl")


def lesson_62():
    for i in range(1, 10):
        if i // 7 == 1:
            pass
        print(i)
        if i == 3:
            print("slqguggshdkglkhsadlkghsadlkhgasdfghjklqasdfghjkl")


def lesson_63():
    name = input("Введите стих : ")
    for i in name:
        print(i)


def lesson_64():
    name = input("Введите пароль : ")
    for i in name:
        if i == "1":
            print("пароль верный")
            break
    else:
        print("пароль не верный добавте 1")


def lesson_65():
    name = int(input("Введите  число : "))
    while name != 1:
        print("Введите 1")
        name = int(input("Введите  число : "))


def lesson_66():
    n = int(input("Введите число : "))
    for i in range(1, n):
        if i % 3 == 0:
            print(f"Число {i} делится на 3")
        if i % 5 == 0:
            print(f"Число {i} делится на 5")
        if i % 2 and i % 6 == 0:
            print(f"Число {i} делится на 2 и на 6")
        if i % 10 == 0 or i % 10 == 1:
            print(f"Число {i} оканчивается на 0 или на 1")
        if not i % 4 == 0:
            print(f"Число {i} не делится на 4")


def lesson_67():
    n = int(input("Введите число : "))
    for i in range(1, n):
        if i % 2 == 0 and i % 3 != 0:
            print(i)


def lesson_68():
    name = input("Введите пароль : ")
    if "1" in name:
        print("Пароль верный")
    else:
        print("Напишите 1")


def lesson_69():
    n = input("Введите строку : ")
    for i in n:
        print(i)


def lesson_70():
    e = 0
    n = input("Введите строку : ")
    for i in n:
        if i == "а":
            e += 1
    print(e)


def lesson_71():
    s = input("Введите строку : ")
    if "ж" in s:
        print("Ж есть")
    else:
        print("Ж нету")


def lesson_72():
    name = input("Введите строку : ")
    c = False
    for i in name:
        if i.lower() == "ж":
            c = True
    if c == True:
        print("ж есть")
    else:
        print("ж нету")


def lesson_73():
    for i in range(1, 20):
        if i % 3 == 0:
            continue
        print(i)


def lesson_74():
    name = input("Введите строку : ")
    for i in name:
        if i == "а":
            print("первая А")
            break


def lesson_75():
    name = input("Введите строку : ")
    for i in name:
        if i.isdigit():
            print("Нашли цифру")
        else:
            pass


def lesson_76():
    print("1 = 123\n2 = 456\n3 = 789")
    m = int(input("Введите номер кнопки : "))
    match m:
        case 1 | 0:
            print("123")
        case 2:
            print("456")
        case 3:
            print("789")
        case _:
            print("Алё")


def lesson_77():
    print("1 = 123\n2 = 456\n3 = 789")
    m = input("Введите номер кнопки : ")
    if m == "1" or m == "0":
        print("123")
    elif m == "2":
        print("456")
    elif m == "3":
        print("789")
    else:
        print("Алё")


def lesson_78():
    print("1 = привет\n2 = как дела?\n3 = пока")
    name = int(input("Введите строку : "))
    match name:
        case 1:
            print("привет")
        case 2:
            print("как дела?")
        case 3:
            print("пока")
        case _:
            print("нет такой команды")


def lesson_79():
    print("Введите номер дня недели  ")
    name = int(input("Введите строку : "))
    match name:
        case 1:
            print("Понедельник")
        case 2:
            print("Вторник")
        case 3:
            print("Среда")
        case 4:
            print("Четверг")
        case 5:
            print("Пятница")
        case 6:
            print("Суббота")
        case 7:
            print("Воскресенье")
        case _:
            print("ошибка")


def lesson_80():
    print("доступные операции :\n+\n-\n*\n/\n**\n%\n// ")
    name = input("Введите операцию : ")
    a = int(input("Введите первое число : "))
    b = int(input("Введите второе число : "))
    match name:
        case "+":
            print(a + b)
        case "-":
            print(a - b)
        case "*":
            print(a * b)
        case "/":
            if b == 0:
                print("На ноль делить нельзя")
            else:
                print(a / b)
        case "**":
            print(a ** b)
        case "%":
            print(a % b)
        case "//":
            print(a // b)
        case _:
            print("ошибка операции")


def lesson_81():
    print('я сказал \'привет\'')
    n = "asdfgh"
    print(rf"\t{n}\n")


def lesson_82():
    name = int(input("Введите число : "))
    print("Вывод: ")
    for i in range(1, name + 1):
        print(f"{i} | {i // 2} | {i % 2}")
    print("")
    print(
        "asdfghjk"
    )


def lesson_83():
    """
    📌 Задача 1 — работа со строкой
Пользователь вводит имя.
Вывести:
- первую букву
- последнюю букву
- длину имени
- имя в верхнем регистр
    """
    name = input("Введите имя : ")
    print(name[0])
    print(name[-1])
    print(len(name))
    print(name.upper())


def lesson_84():
    """
    📌 Задача 2 — проверка числа
Пользователь вводит число.
Определить:
- положительное / отрицательное
- чётное / нечётное
    """
    number = int(input("Введите число : "))
    if number >= 0:
        print("Положительное")
    else:
        print("Отрицательное")
    if number % 2 == 0:
        print("Чётное")
    elif number % 2 != 0:
        print("Нечётное")


def lesson_85():
    """
    📌 Задача 3 — последняя цифра числа
Пользователь вводит число.
Вывести:
- последнюю цифру числа
- оканчивается ли число на 5
    """
    number = int(input("Введите число : "))
    print(number % 10)
    if number % 10 == 5:
        print("Число оканчивается на 5")
    else:
        print("Число не оканчивается на 5")


def lesson_86():
    """
    📌 Задача 4 — сумма цифр числа
Пользователь вводит число.
Найти сумму цифр числа через while.
Пример:
123 → 6
    """
    number = int(input("Введите число : "))
    amount = 0
    while number > 0:
        actions = number % 10
        amount += actions
        number //= 10
    print(amount)


def lesson_87():
    """
    📌 Задача 5 — перебор строки через for
Пользователь вводит строку.
Посчитать количество букв:
а
    """
    line = input("Введите строку : ")
    amount = 0
    for i in line:
        if i == "а":
            amount += 1
    print(amount)


def lesson_88():
    """
    📌 Задача 6 — есть ли цифры в строке
Пользователь вводит строку.
Проверить:
есть ли в строке цифры
    """
    line = input("Введите строку : ")
    numbers = False
    for i in line:
        if i.isdigit():
            numbers = True
    if numbers == True:
        print("В строке есть цифры")


def lesson_89():
    """
📌 Задача 7 — continue
Вывести числа от 1 до 20.
Пропустить числа, которые делятся на 3.
    """
    for i in range(1, 21):
        if i % 3 == 0:
            continue
        print(i)


def lesson_90():
    """
    📌 Задача 8 — работа с range(start, stop, step)
Вывести числа:
от 30 до 10 через одно, например: 30, 28, 26 и тд.
    """
    for i in range(30, 10, -2):
        print(i)


def lesson_91():
    """
    📌 Задача 9 — мини-анализ строки (финальная задача)
Пользователь вводит строку.
Программа должна:
если встретилась цифра написать:
В строке есть цифра
и завершить проверку (break)
если встретилась буква:
пропустить символ (continue)
остальные символы:
ничего не делать (pass)
    """
    line = input("Введите строку : ")
    for i in line:
        if i.isdigit():
            print("В строке есть цифра")
            break
        elif i.isalpha():
            print("В строке есть буква")
            continue
        else:
            pass


def lesson_92():
    numbers = [1, 2, 3, 3, 56, 6, 7, 67, 69, 52]
    print(numbers)
    data = [10, "dafaghgk", True, 12.3]
    print(data)
    print(type(data))
    print(data[1])
    value = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(value)


def lesson_93():
    """
    📌 Задача 1 — проверка логина
    Пользователь вводит логин пока не введёт корректный логин, количество попыток не ограничено.
    Логин должен:
    - быть длиннее 5 символов;
    - не содержать пробелов;
    - не содержать цифр.
    Если подходит вывести "Логин принят"
    иначе: "Ошибка логина"
    """
    login_correct = False
    print("Введите логин, он должен быть больше 5 символов и не содержать пробелов и цифр")
    while not login_correct:
        login = input("Введите логин : ")
        # Логин должен быть больше 5 символов
        login_len = len(login) > 5
        # Логин не должен содержать пробелы
        without_spaces = " " not in login
        # Логин не должен содержать цифр
        no_digits = len([i for i in login if i.isdigit()]) == 0
        login_correct = login_len and without_spaces and no_digits
        if not login_correct:
            print("ошибка логина")
    print('Логин принят')


def lesson_94():
    """
    📌 Задача 2 — перенести последнюю цифру числа в начало
Пользователь вводит число.
Программа должна перенести последнюю цифру числа в начало.
Примеры:
123 → 3123
4567 → 74567
667 → 7667
    """
    number = int(input("Введите число : "))
    o = number % 10
    print(f"{o}{number}")


def lesson_95():
    line = ["bsdasjhd", 5667437, True, 12.3, 100]
    line[0] = 100
    print(line)
    print(len(line))
    for i in line:
        print(i)
    for i in range(len(line)):
        print(line[i])
    line.append(1000000000000000000000000000000000000000000000000000000000000)
    print(line)
    value = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(len(value))
    #hehehehehe.append(line)
    print(len(value))
    print(value)
    value.extend(line)
    print(value)
    print(len(value))
    value.extend([456782865467746464664646466466464667, "nfgjjt", True, False, 12.3])
    print(value)
    print(len(value))
    value.pop()
    print(value)
    value.pop(15)
    print(value)
    value.remove(456782865467746464664646466466464667)
    value.remove("nfgjjt")
    print(value)
    print("----------------------------------------")
    value.sort()
    print(value)
    print(-3 * True)
    value.sort(reverse=True)
    print(value)
    ages = [1, 3, 2, 10, 4, 5, 6, 7, 8, 9]
    ages.reverse()
    print(ages)


def lesson_96():
    """
    📌 Задача 1 — создать список чисел
создать список от 1 до 10 через range().
Вывести:
- список;
- длину списка;
- последний элемент списка.
    """
    line = [i for i in range(1, 10)]
    print(line)
    print(len(line))
    print(line[-1])


def lesson_97():
    """
   📌 Задача 2 — сумма элементов списка
    создать список чисел:
    [5, 8, 2, 10, 3]
    Найти сумму всех элементов списка.
    """
    linae = [5, 8, 2, 10, 3]
    amount = 0
    for i in linae:
        amount += i
    print(amount)
    print(sum(linae))


def lesson_98():
    """
    📌 Задача 3 — найти максимальный элемент
    создать список чисел.
    Найти:
    максимальный элемент списка
    """
    line = [12, 13, 10, 10, 100, 20]
    print(max(line))


def lesson_99():
    """
        📌 Задача 4 — добавление элементов
        создать список:
        [1, 2, 3]
        Добавить число 4
        вывести список.
    """
    line = [1, 2, 3]
    line.append(4)
    print(line)


def lesson_100():
    """
        📌 Задача 5 — удаление элементов
        создать список:
        [5, 3, 8, 3, 10]
        Удалить число 3 и последний элемент списка
        вывести результат.
    """
    line = [5, 3, 8, 3, 10]
    line.remove(3)
    line.pop(-1)
    print(line)


def lesson_101():
    """
    📌 Задача 6 — анализ списка
создать список:
[4, 7, 2, 7, 9]
Найти:
сколько раз встречается число 7
индекс первого числа 7
    """
    line = [4, 7, 2, 7, 9]
    amount = 0
    for i in line:
        if i == 7:
            amount += 1
    print(amount)
    print(line.index(7))


def lesson_102():
    """
    📌 Задача 7 — сортировка списка
создать список:
[8, 3, 1, 6, 2]
Вывести:
- отсортированный список
- список в обратном порядке
    """
    line = [8, 3, 1, 6, 2]
    line.sort()
    print(line)
    line.sort(reverse=True)
    print(line)


def lesson_103():
    """
    📌 Задача 8 — список квадратов чисел
cоздать список:
от 1 до 10
через list comprehension:
[1, 4, 9, 16 ...]
    """
    line = [i ** 2 for i in range(1, 10)]
    print(line)


def lesson_104():
    line = [1, 2, 3]
    b = line
    b.append(4)
    print(line)
    print(b)
    c = line.copy()
    c.append(5)
    print(c)
    print(line)
    d = 3
    a = d
    a += 1
    print(d)
    print(a)


def lesson_105():
    line = input("Введите текст : ")
    line = line.split(" ")
    line.append("🦈")
    print(line[-2])
    print(len(line))


def lesson_106():
    print("1 - добавить гостя\n2 - удалить гостя\n3 - список гостей\n4 - количество гостей")
    guests = ["Анна", "Иван", "Мария"]
    choose = int(input("Введите номер : "))
    match choose:
        case 1:
            name = input("Введите имя : ")
            if name in guests:
                print("Такой гость уже есть")
            else:
                guests.append(name)
                print("Гость добавлен")
        case 2:
            name = input("Введите имя : ")
            if name not in guests:
                print("Такого гостя нету")
            else:
                guests.remove(name)
                print("Гость удалён")
        case 3:
            for i in guests:
                print(i)
        case 4:
            print(len(guests))
        case _:
            print("Ошибка")


def lesson_107():
    """
        Прикрепляю домашнее задание:
        📌 Мини-проект 1 — список покупок
        Создать список:
        shopping_list = ["хлеб", "молоко", "сыр"]
        Сделать меню программы:
        1 — добавить товар
        2 — удалить товар
        3 — показать список покупок
        4 — проверить наличие товара
        5 — показать количество товаров
        Логика работы программы
        1. Добавить товар
        Пользователь вводит название товара.
        Если товара нет в списке:
        Товар добавлен
        Если уже есть:
        Товар уже есть в списке
        2. Удалить товар
        Если товар есть:
        Товар удалён
        Если нет:
        Товара нет в списке
        3. Показать список покупок
        Вывести список:
        Список покупок:
        хлеб
        молоко
        сыр
        4. Проверить наличие товара
        Пользователь вводит название товара
        Вывести:
        Товар найден
        или
        Товар не найден
        5. Показать количество товаров
        Вывести:
        Всего товаров: ...
    """
    print(
        "1 - добавить товар\n2 - удалить товар\n3 - показать список покупок\n"
        "4 - проверить наличие товара\n5 - показать количество товаров"
    )
    products = ["хлеб", "молоко", "сыр"]
    number = int(input("Введите номер : "))
    match number:
        case 1:
            name = input("Введите название товара : ")
            if name in products:
                print("Такой товар уже есть")
            else:
                products.append(name)
                print("Товар добавлен")
        case 2:
            name = input("Введите название товара : ")
            if name not in products:
                print("Такого товара нету")
            else:
                products.remove(name)
                print("Товар удалён")
        case 3:
            print("Список покупок : ")
            for i in products:
                print(i)
        case 4:
            name = input("Введите название товара : ")
            if name in products:
                print("Товар найден")
            if name not in products:
                print("Товар не найден")
        case 5:
            print("Всего товаров : ")
            print(len(products))


def lesson_108():
    line = [5,4,2,1,3]
    line.reverse()
    print(line)
    line.insert(10,0)
    print(line)


def lesson_109():
    a = [[1,2,3],[4,5,6],[7,8,9],10]
    print(a[0][0])


def lesson_110():
    products = ["хлеб", "молоко", "сыр","яйца"]
    # for i in products:
    # print(f"{products.index(i) + 1} {i}")
    for i in range(len(products)):
        print(f"{i + 1} {products[i]}")


def lesson_111():
    """
    📌 Задача 1. Вывести таблицу с индексами строк
    Есть список:
    table = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
    ]
    Пример вывода:
    Строка 0: [1, 2, 3]
    Строка 1: [4, 5, 6]
    Строка 2: [7, 8, 9]
    """
    table = [[1,2,3],[4,5,6],[7,8,9]]
    for i in range (len(table)):
        print(f"Строка {i} : {table[i]}")




def lesson_112():
    """
    📌 Задача 2. Найти сумму всех элементов таблицы
    Дан список:
    numbers = [
    [5, 10],
    [15, 20],
    [25, 30]
    ]
    """
    numbers = [[5,10],[15,20],[25,30]]
    amount = 0
    for i in numbers:
        amount += sum(i)
    print(amount)


def lesson_113():
    """
    📌 Задача 3. Добавить строку в таблицу через insert()
Есть список:
students = [
    ["Анна", 5],
    ["Иван", 4],
    ["Мария", 5]
]
Добавить нового ученика:
["Олег", 3]
на второе место списка.
Результат:
["Анна", 5]
["Олег", 3]
["Иван", 4]
["Мария", 5]
    """
    students = [["Анна",5],["Иван",4],["Мария",5]]
    students.insert(1,["Олег",3])
    print(students)


def lesson_114():
    """
    📌 Задача 4. Мини-анализ оценок
Есть список:
grades = [5, 4, 3, 5, 2, 4, 5]
Программа должна:
1. вывести количество оценок
2. вывести среднюю оценку
3. вывести количество пятёрок
4. проверить есть ли двойка
Пример результата:
Количество оценок: 7
Средняя оценка: 4.0
Количество пятёрок: 3
Есть двойка
    """
    grades = [5,4,3,5,2,4,5]
    amount = 0
    print(f"Количество оценок : {len(grades)}")
    print(f"Средняя оценка : {sum(grades) / len(grades)}")
    for i in grades:
        if i == 5:
            amount += 1
    print(f"Количество пятёрок : {amount}")
    if 2 in grades:
        print("Есть двойка")


def lesson_115():
    """
    📌 Мини-проект. Учёт книг в домашней библиотеке
Программа хранит список книг.
Создать список:
books = ["Гарри Поттер", "Незнайка на Луне", "Маленький принц"]
Нужно сделать бесконечное меню:
1 — Добавить книгу
2 — Удалить книгу
3 — Показать список книг
4 — Найти книгу
5 — Показать количество книг
6 — Показать количество книг
7 — Показать количество книг
8 — Показать количество книг
0 — Выход
Что должна делать программа:
1. Добавить книгу
Пользователь вводит название книги.
Если такой книги ещё нет:
Книга добавлена
Если уже есть:
Такая книга уже есть
2. Удалить книгу
Пользователь вводит название книги.
Если книга есть:
Книга удалена
Если нет:
Такой книги нет
3. Показать список книг
Вывести список с нумерацией:
Список книг:
1. Гарри Поттер
2. Незнайка на Луне
3. Маленький принц
4. Найти книгу
Пользователь вводит название.
Если книга есть:
Книга найдена
Если нет:
Книга не найдена
5. Показать количество книг
Вывести:
Всего книг: 3
6. Показать первую книгу
Вывести:
Первая книга: Гарри Поттер
7. Добавить книгу в начало списка
Использовать:
insert(0, книга)
8. Очистить список книг
Сделать список пустым.
0. Выход
Программа завершает работу:
Программа завершена

    """

    lego = ["халк бастер","сокл тысячи летия","R2 D2"]
    while True:
        print("1 - добавить лего\n2 - удалить лего\n3 - показать список лего\n4 - Найти лего\n"
              "5 - Показать количество лего\n6 - Показать первую лего\n"
              "7 - Добавить лего в начало списка\n8 - Очистить список лего\n0 - Выход"
              )
        number = int(input("Введите номер : "))
        match number:
            case 1:
                name = input("Введите название лего : ")
                if name in lego:
                    print("Такое лего уже есть")
                else:
                    lego.append(name)
                    print("Лего добавлено")
            case 2:
                name = input("Введите название лего : ")
                if name not in lego:
                    print("Такого лего нету")
                else:
                    lego.remove(name)
                    print("Лего удалено")
            case 3:
                if len(lego) == 0:
                    print("Список пуст")
                else:
                    print("Список лего: ")
                    for i in range(len(lego)):
                        print(f"{i}.{lego[i]}")
            case 4:
                name = input("Введите название лего : ")
                if name in lego:
                    print("Лего найдено")
                else:
                    print("Лего не найдено")
            case 5:
                print(f"Всего лего: {len(lego)}")
            case 6:
                print(f"Первое лего: {lego[0]}")
            case 7:
                name = input("Введите название лего : ")
                if name in lego:
                    print("Такое лего уже есть")
                else:
                    lego.insert(0,name)
                    print("Лего добавлено")
            case 8:
                lego.clear()
                print("Список очищен")
            case 0:
                print("Программа завершена")
                break
            case _:
                print("Ошибка")


def lesson_116():
    """
    📌 Мини-проект 1 — LEGO Star Wars: выбор персонажа
Создать список:
heroes = ["Люк", "Вейдер", "Йода"]
Сделать бесконечное меню:
1 — Показать персонажей
2 — Добавить персонажа
3 — Удалить персонажа
4 — Посчитать персонажей
0 — Выход
Использовать:
while True
Что делает программа
1 — Показать персонажей
Вывод:
Список персонажей:
1. Люк
2. Вейдер
3. Йода
2 — Добавить персонажа
Пользователь вводит имя.
Если героя ещё нет:
Герой добавлен
Если есть:
Такой герой уже есть
3 — Удалить персонажа
Если есть:
Герой удалён
Если нет:
Такого героя нет
4 — Посчитать персонажей
Вывести:
Всего героев: 3
0 — Выход
Использовать:
break
    """
    heroes = ["Люк","Вейдер","Йода"]
    while True:
        print("1 - Показать персонажей\n2 - Добавить персонажа\n3 - Удалить персонажа\n4 - Посчитать персонажей\n"
              "0 - Выход")
        number = int(input("Введите номер : "))
        match number:
            case 1:
                print("Список персонажей : ")
                for i in heroes:
                    print(i)
            case 2:
                name = input("Введите персонажа : ")
                if name in heroes:
                    print("Такой герой уже есть")
                else:
                    heroes.append(name)
                    print("Герой добавлен")
            case 3:
                name = input("Введите персонажа : ")
                if name not in heroes:
                    print("Такого героя нету")
                else:
                    heroes.remove(name)
                    print("Герой удалён")
            case 4:
                for i in range(len(heroes)):
                    print(i)
            case 0:
                break


def lesson_117():
    """
    📌 Мини-проект 2 — LEGO-магазин
Создать список:
sets = ["Тысячелетний сокол", "Звезда Смерти", "Бэтмобиль"]
Меню:
1 — Показать наборы
2 — Купить набор
3 — Добавить набор
4 — Сколько наборов осталось
0 — Выход
Логика
Показать наборы
Выводим пользователю все наборы из списка
Купить набор
Пользователь вводит название.
Если набор есть:
Набор куплен
(удаляем из списка)
Если нет:
Такого набора нет
Добавить набор
Добавляем новый набор.
Сколько наборов осталось
Выводим количество оставшихся наборов
    """
    sets = ["Тысячелетний сокол","Звезда Смерти","Бэтмобиль"]
    while True:
        print("1 - Показать наборы\n2 - Купить набор\n3 - Добавить набор\n4 - Сколько наборов осталось\n0 - Выход")
        number = int(input("Введите номер : "))
        match number:
            case 1:
                for i in sets:
                    print(i)
            case 2:
                name = input("Введите набор : ")
                if name in sets:
                    print("Набор куплен")
                    sets.remove(name)
                else:
                    print("набор не куплен")
            case 3:
                name = input("Введите набор : ")
                if name not in sets:
                    sets.append(name)
                    print("Набор добавлен")
                else:
                    print("Такой набор уже есть")
            case 4:
                for i in range(len(sets)):
                    print(i)
            case 0:
                break


def lesson_118():
    line = input("Введите текст : ")
    line_number = False
    for i in line:
        if i.isdigit():
            line_number = True
    if line_number:
        print("В строке есть цифра")
    else:
        print("В строке нет цифры")


def lesson_119():

    points = (13,14,79)
    print(type(points))
    print(points)
    print(points[1])
    x,y,z = points
    print(x)
    print(y)
    print(z)
    line = [1,2,3]
    x,y,z = line
    print(x)
    print(y)
    print(z)
    a = "123"
    x,y,z = a
    print(x)
    print(y)
    print(z)
    print("🦧🦧🦧🦧🦧🦧🦧🦧🦧🦧🦧🦧🦧🦧🦧🦧🦧🦧🦧🦧🦧🦧🦧🦧🦧🦧🦧🦧🦧🦧🦧🦧🦧🦧🦧🦧🦧🦧🦧🦧")
    print("\U0001F947")
    Artem = ("🦧🦧🦧🦧🦧🦧🦧🦧🦧🦧",)
    Edgar = Artem + points
    print(Edgar)
    lola = '5'
    lolaint = int(lola)
    print(lolaint)
    print(type(lolaint))
    print("-------------------------------------------------------------------------------------")
    sirius = ("🦧🦧🦧🦧🦧🦧🦧🦧🦧🦧",1,2,3)
    sirius_list = list(sirius)
    sirius_list.append(4)
    print(sirius_list)
    print(type(sirius_list))
    sirius_tuple = tuple(sirius_list)
    print(sirius_tuple)
    print(type(sirius_tuple))


def lesson_120():
    """
    📌 Задача 1. Проверка пароля
Пользователь вводит пароль.
Нужно проверить есть ли в пароле символ "!" или "?"
Использовать флаг.
Если есть - вывести:
Надёжный пароль
Иначе:
Добавьте спецсимвол!
    """
    login = input("Введите логин : ")
    login_correct = False
    if "!" in login or "?" in login:
        login_correct = True
    if login_correct:
        print("Надёжный пароль")
    else:
        print("Добавьте спецсимвол")


def lesson_121():
    """
    📌 Задача 2. Информация о человеке
Создать кортеж:
person = ("Иван", 16, "Самара")
Вывести:
Имя: Иван
Возраст: 16
Город: Самара
    :return:
    """
    person = ("Иван",16,"Самара")
    name, age, town = person
    print(f"Имя: {name}")
    print(f"Возраст: {age}")
    print(f"Город: {town}")


def lesson_122():
    """
    📌 Задача 3. Перебор кортежа
Есть кортеж:
colors = ("красный", "зелёный", "синий", "жёлтый")
Вывести все цвета через цикл.
    """
    colors = ("красный", "зелёный", "синий", "жёлтый")
    for i in colors:
        print(i)


def lesson_123():
    """
    📌 Задача 4. Длина кортежа
Есть кортеж:
animals = ("кот", "пёс", "слон", "жираф")
Вывести:
Количество животных: 4
    """
    animals = ("кот","пёс","слон","жираф")
    amount = 0
    for i in range(len(animals)):
        amount += 1
    print(f"Количество животных: {amount}")


def lesson_124():
    """
    📌 Задача 5. Найти максимальное число
Есть кортеж:
numbers = (5, 12, 3, 18, 7)
Найти максимальное число с помощью функции и через цикл.
    """
    numbers = (5,12,3,18,7)
    max_number = 1234567898765432134567890898123456789087654323456789009876543234567890987654323456789098765432345678904
    print(max(numbers))
    for i in numbers:
        if i < max_number:
            max_number = i
    print(max_number)




def lesson_125():
    """
    📌 Задача 6. Проверка оценок
Есть кортеж:
grades = (5, 4, 3, 5, 2, 4)
Проверить:
есть ли двойка.
Использовать флаг.
Если есть вывести текст: "Есть двойка"
Если нет: "Отлично!"
    """
    grades = (5,4,3,5,2,4)
    grades_correct = False
    if 2 in grades:
        grades_correct = True
    if grades_correct:
        print("Есть двойка")
    else:
        print("Отлично!")


def lesson_126():
    student = {"name": "Иван", "age": 16, "city": "Самара"}
    print(student["name"])
    print(student.get("pepe"))
    student["pepe"] = "mortis"
    print(student)
    student["pepe"] = "derril"
    for key in student:
        print(f"{key}:{student[key]}")
        print(type(key))
    print("🦧🦧🦧🦧🦧🦧🦧🦧🦧🦧🦧🦧🦧🦧🦧🦧🦧🦧🦧🦧🦧🦧🦧🦧🦧🦧🦧🦧🦧🦧🦧🦧🦧🦧🦧🦧🦧🦧🦧🦧")
    print(student.keys())
    a = student.keys()
    print(type(a))
    for i in student.keys():
        print(i)
    print(student.values())
    for i in student.values():
        print(i)
        print(type(i))
    print(student.items())
    for i in student.items():
        print(i)
        print(type(i))
        print("\U0001f9e8")
    for i in student.items():
        print(i[0])
    print("🦇🦇🦇🦇🦇🦇🦇🦇🦇🦇🦇🦇🦇🦇🦇🦇🦇🦇🦇🦇🦇🦇🦇🦇🦇🦇🦇🦇🦇🦇🦇🦇🦇🦇🦇🦇🦇🦇🦇🦇🦇🦇")
    for key,value in student.items():
        print(f"{key}:{value}")
    print("🧨🧨🧨🧨🧨🧨🧨🧨🧨🧨🧨🧨🧨🧨🧨🧨🧨🧨🧨🧨🧨🧨🧨🧨🧨🧨🧨🧨🧨🧨🧨🧨🧨🧨🧨🧨🧨🧨🧨🧨🧨🧨🧨🧨")
    student.pop("~_~","не найдено")
    print(student)
    print("\U0001f9c7")
    print(student.pop("~_~","не найдено"))
    print("🧇🧇🧇🧇🧇🧇🧇🧇🧇🧇🧇🧇🧇🧇🧇🧇🧇🧇🧇🧇🧇🧇🧇🧇🧇🧇🧇🧇🧇🧇🧇🧇🧇🧇🧇🧇🧇🧇🧇🧇🧇🧇🧇🧇")


def lesson_127():
    """
    📌 Задача 1. Карточка ученика
    Создать словарь:
    student = {
    "name": "Андрей",
    "age": 15,
    "city": "Москва"
    }
    Вывести:
    Имя: Иван
    Возраст: 15
    Город: Самара
    """
    student = {"name": "Андрей","age": "15","city":"Самара"}
    print(f"Имя:{student["name"]}\nВозраст:{student["age"]}\nГород:{student["city"]}")


def lesson_128():
    """
    📌 Задача 2. Изменение значения
Есть словарь:
car = {
    "brand": "Toyota",
    "year": 2018,
    "color": "white"
}
Изменить цвет машины на black
Вывести обновлённый словарь.
    """
    car = {"brand": "Toyota","year": 2018,"color": "white"}
    car["color"] = "black"
    print(car)


def lesson_129():
    """
   📌 Задача 3. Добавление элемента
Есть словарь:
book = {
    "title": "Волшебник Изумрудного города",
    "author": "Александр Волков"
}
Добавить ключ:
year
со значением:
1939
    """
    book = {"title": "Волшебник изумрудного города", "author": "Александр Волков"}
    book["year"] = 1939


def lesson_130():
    """
    📌 Задача 4. Проверка товара
Есть словарь:
products = {
    "яблоко": 100,
    "банан": 80,
    "груша": 120
}
Пользователь вводит название товара.
Через .get() вывести цену.
Если товара нет:
Такого товара нет
    """
    products = {"яблоко": 100,"банан": 80,"груша": 120}
    name = input("Введите название товара: ")
    if products.get(name):
        print(products.get(name))
    else:
        print("Такого товара нет")


def lesson_131():
    """
    📌 Задача 5. Удаление элемента
Есть словарь:
user = {
    "name": "Иван",
    "age": 16
    "city": "Хабаровск"
}
Удалить ключ city
Вывести словарь.
    """
    user = {"name": "Иван","age": 16,"city": "Хабаровск"}
    user.pop("city")
    print(user)


def lesson_132():
    """
    📌 Задача 6. Безопасное удаление
Есть словарь:
user = {
    "name": "Иван",
    "age": 16,
    "city": "Хабаровск"
}
Попробовать удалить ключ phone
без ошибки.
Использовать безопасный .pop().
Если ключа нет:
Нечего удалять
    """
    user = {"name": "Иван","age": 16,"city": "Хабаровск"}
    user.pop("phone","не найдено")
    print(user)


def lesson_133():
    """
    📌 Задача 7. Вывести только ключи
Есть словарь:
movie = {
    "title": "Лего фильм",
    "year": 2014,
    "genre": "комедия"
}
Вывести все ключи через .keys()
    """
    movie = {"title": "лего фильм","year": 2014,"genre": "комедия"}
    print(movie.keys())


def lesson_134():
    """
    📌 Задача 8. Вывести только значения
Вывести все значения через .values()
    """
    movie = {"title": "лего фильм","year": 2014,"genre": "комедия"}
    print(movie.values())


def lesson_135():
    """
    📌 Задача 9. Вывести пары ключ-значение
Вывести:
title -> Лего фильм
year -> 2014
genre -> комедия
Использовать:
.items()
    """
    movie = {"title": "лего фильм","year": 2014,"genre": "комедия"}
    print(movie.items())


def lesson_136():
    """
    📌 Задача 10. Перебор по ключам
Есть словарь:
grades = {
    "Математика": 5,
    "Физика": 4,
    "Информатика": 5
}
Вывести предметы.
Использовать:
for key in grades:
или
for key in grades.keys():
    """
    grades = {"математика": 5,"физика": 4,"информатика": 5}
    for key in grades:
        print(key)


def lesson_137():
    """
    📌 Задача 11. Перебор значений
Вывести только оценки.
Использовать .values()
    """
    grades = {"математика": 5,"физика": 4,"информатика": 5}
    print(grades.values())


def lesson_138():
    """
    📌 Задача 12. Найти среднюю оценку
Посчитать среднюю оценку по словарю.
Использовать перебор значений.
    """
    grades = {"математика": 5,"физика": 4,"информатика": 5}
    for i in grades.values():
        if 5 > i > 2:
            print(i)

def lesson_139():
    movie = {"title": "лего фильм", "year": 2014, "genre": "комедия"}
    nike = {"pepe": "эдгар", "fffffff": "uhjf"}
    movie.popitem()
    print(movie)
    nike.update(movie)
    print(nike)
    nike.clear()
    print(nike)
    keys = ["имя", "город", "зарплата"]
    values = ["Петя", "Москва", 123456789]
    value = "не задано"
    person = dict.fromkeys(keys, value)
    print(person)
    double = {i: i * 2 for i in range(1, 7)}
    print(double)
    print("-------------------------------")
    a = ["jfjdjnfjfjn"]
    b = a.copy()
    b.clear()
    print(a)
    print(b)


def lesson_140():
    """
    📌 Задача 1. Обновление профиля
Есть словарь:
user = {
    "name": "Иван",
    "age": 20
}
Пользователь вводит:
город
возраст (новый)
Обновить словарь
Вывести обновлённый словарь.
    """
    user = {"name": "Иван", "age": 20}
    nike = {"city": input(), "age": int(input())}
    user.clear()
    user.update(nike)
    print(user)


def lesson_141():
    """
    📌 Задача 2. Объединение словарей
Есть:
a = {"x": 1, "y": 2}
b = {"z": 3, "y": 10}
Объединить словари через .update() и вывести результат.
    """
    a = {"x": 1, "y": 2}
    b = {"z": 3, "y": 10}
    a.update(b)
    print(a)


def lesson_142():
    """
    📌 Задача 3. Удаление последнего элемента
Есть словарь:
data = {
    "a": 1,
    "b": 2,
    "c": 3
}
Удалить последний элемент
Вывести словарь до и после.
    """
    data = {"a": 1, "b": 2, "c": 3}
    print(data)
    data.popitem()
    print(data)


def lesson_143():
    """
    📌 Задача 4. Очистка словаря
Есть словарь:
cart = {
    "milk": 2,
    "bread": 1,
    "cheese": 3
}
Очистить словарь
Вывести результат.
    """
    cart = {"milk": 2, "bread": 1, "cheese": 3}
    cart.clear()
    print(cart)


def lesson_144():
    """
    📌 Задача 5. Копия словаря
Есть словарь:
original = {
    "name": "Анна",
    "score": 100
}
Создать копию этого словаря
Изменить копию и показать, что оригинал не изменился.
    """
    original = {"name": "Анна", "score": 100}
    b = original.copy()
    b.clear()
    print(original)
    print(b)


def lesson_145():
    """
    📌 Задача 6. Создание словаря из ключей
Создать список ключей:
keys = ["a", "b", "c"]
С помощью .fromkeys() создать словарь:
a → 0
b → 0
c → 0
    """
    keys = ["a", "b", "c"]
    person = dict.fromkeys(keys, 0)
    print(person)


def lesson_146():
    """
    📌 Задача 7. fromkeys с текстом
Создать словарь:
keys = ["name", "age", "city"]
Значение по умолчанию:
unknown
    """
    keys = ["name", "age", "city"]
    person = dict.fromkeys(keys, "неизвестно")
    print(person)


def lesson_147():
    """
    📌 Задача 8. Удвоенные числа
Создать словарь:
числа от 1 до 5 → их удвоенное значение
Результат:
1:2, 2:4, 3:6, 4:8, 5:10
    """
    numbers = {i: i * 2 for i in range(1, 6)}
    print(numbers)


def lesson_148():
    """
    📌 Задача 9. Чётные числа
Создать словарь:
от 1 до 10 → только чётные числа
    """
    numbers = {i for i in range(1, 11) if i % 2 == 0}
    print(numbers)


def lesson_149():
    """
    📌 Задача 10. Символ → длина строки
Есть список:
words = ["кот", "собака", "питон"]
Создать словарь:
кот → 3
собака → 6
питон → 5
    """
    words = ["кот", "собака", "питон"]
    words_dict = dict()
    for w in words:
        words_dict.update({w: len(w)})
    print(words_dict)


def lesson_150():
    """
    📌 Задача 11. Обновление и удаление
Есть словарь:
data = {"a": 1, "b": 2, "c": 3}
Необходимо:
- удалить последний элемент
- добавить "d": 4
- изменить "a" → 100
Использовать:
popitem, update
    """
    data = {"a": 1, "b": 2, "c": 3}
    data.popitem()
    data["d"] = 4
    data["a"] = 100
    print(data)


def lesson_151():
    numbers = {1, 2, 3, 4, 5}
    print(type(numbers))
    numbers.add(6)
    numbers.add(5)
    print(numbers)
    numbers.remove(5)
    print(numbers)
    ghjjhlhjk = {5, 3, "gfjg", 4, True, "bfvbfvb", 0, False}
    print(ghjjhlhjk)
    a = {1, 2, 3}
    b = {3, 4, 5}
    print(a | b)
    print(a & b)
    print(a - b)
    print(a ^ b)


def lesson_152():
    digits_list = [1, 1, 2, 2, 3, 4, 5, 5]
    print(digits_list)
    print(type(digits_list))
    digits_list = tuple(digits_list)
    print(digits_list)
    print(type(digits_list))
    digits_list = set(digits_list)
    print(digits_list)
    print(type(digits_list))
    digits_list = list(digits_list)
    print(digits_list)
    print(type(digits_list))


def lesson_153():
    """
    📌 Задача 1. Уникальные буквы
    Пользователь вводит слово.
    Создать множество из букв слова.
    Пример:
    hello
    Результат:
    {'h', 'e', 'l', 'o'}
    """
    hello = {"h", "e", "l", "l", "o"}
    print(hello)


def lesson_154():
    """
    📌 Задача 2. Добавление элемента
Есть множество:
fruits = {"яблоко", "банан"}
Добавить:
груша
    """
    fruits = {"яблоко", "банан"}
    fruits.update("груша")
    print(fruits)


def lesson_155():
    """
    📌 Задача 3. Удаление элемента
Удалить:
банан
    """
    fruits = {"яблоко", "банан"}
    fruits.remove("банан")
    print(fruits)


def lesson_156():
    """
    📌 Задача 4. Вывести элементы множества
Есть множество:
colors = {"красный", "синий", "зелёный"}
Вывести все элементы через цикл for.
    """
    colors = {"красный", "синий", "зелёный"}
    for i in colors:
        print(i)


def lesson_157():
    """
    📌 Задача 5. Подсчёт элементов
Вывести количество элементов множества
    """
    colors = {"красный", "синий", "зелёный"}
    print(len(colors))


def lesson_158():
    """
    📌 Задача 6. Общие элементы
Есть множества:
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
Найти общие элементы.
    """
    a = {1, 2, 3, 4}
    b = {3, 4, 5, 6}
    print(a & b)


def lesson_159():
    """
    📌 Задача 7. Все уникальные элементы
Найти все элементы из двух множеств.
    """
    a = {1, 2, 3, 4}
    b = {3, 4, 5, 6}
    print(a | b)


def lesson_160():
    """
    📌 Задача 8. Разница множеств
Найти элементы, которые есть только в первом множестве
    """
    a = {1, 2, 3, 4}
    b = {3, 4, 5, 6}
    print(a^b-b)


def lesson_161():
    """
    📌 Задача 9. Уникальные слова
Пользователь вводит текст.
Вывести:
все уникальные слова текста
    """
    a = input()
    a = a.split()
    a = set(a)
    print(a)


def lesson_162():
    """
    📌 Задача 10. Проверка общих друзей
Есть множества:
user1 = {"Анна", "Иван", "Мария"}
user2 = {"Иван", "Олег", "Мария"}
Вывести:
общих друзей
    """
    user1 = {"Анна", "Иван", "Мария"}
    user2 = {"Иван", "Олег", "Мария"}
    print(user1 & user2)


def lesson_163():
    """
    📌 Задача 11. Какие предметы выбрал только один ученик
Есть множества:
student1 = {"математика", "физика", "информатика"}
student2 = {"математика", "биология", "химия"}
Вывести предметы, которые не совпадают.
    """
    student1 = {"математика", "физика", "информатика"}
    student2 = {"математика", "биология", "химия"}
    print(student1^student2)


def lesson_164():
    movies = [
        {"title": "Интерстеллар", "year": 2014, "rating": 8.7},
        {"title": "Начало", "year": 2010, "rating": 8.8},
        {"title": "Матрица", "year": 1999, "rating": 8.5}
    ]
    for value in movies:
        print(value['title'])
    for i in movies[1]:
        print(movies[1][i])
    print("----------------------------")
    mini = 2452879873979872982377
    for i in movies:
        if i['year']<mini:
            mini = i['year']
    print(mini)


def lesson_165():
    """
    📌 Задача 1. Мини-база игр
Создать список словарей:
games = [
    {"name": "Minecraft", "players": 200, "genre": "sandbox"},
    {"name": "CS2", "players": 150, "genre": "shooter"},
    {"name": "Terraria", "players": 90, "genre": "sandbox"}
]
Что должна делать программа
1. Показать все игры
Вывод:
Minecraft — sandbox — 200 игроков
CS2 — shooter — 150 игроков
Terraria — sandbox — 90 игроков
2. Найти игру с максимальным количеством игроков
Вывести:
Самая популярная игра: Minecraft
3. Показать только игры жанра sandbox
4. Добавить новую игру
Пользователь вводит:
название
жанр
онлайн
Добавить словарь в список.
    """
    games = [
        {"name": "Minecraft", "players": 200, "genre": "sandbox"},
        {"name": "CS2", "players": 150, "genre": "shooter"},
        {"name": "Terraria", "players": 90, "genre": "sandbox"}
    ]
    players_max = 0
    for i in games:
        print(i)
    for i in games:
        if i["players"]>players_max:
            players_max = i["players"]
    print(players_max)
    for i in games:
        if i["genre"] == "sandbox":
            print(i)
    name = input("name: ")
    players = int(input("players: "))
    genre = input("genre: ")
    games.append({"name": name})
    games[3]["players"] = players
    games[3]["genre"] = genre
    print(games[3])


def lesson_166():
    """
    📌 Задача 2 — база супергероев Marvel
Создать список словарей:
heroes = [
    {"name": "Железный человек", "power": 95, "team": "Мстители"},
    {"name": "Тор", "power": 100, "team": "Мстители"},
    {"name": "Локи", "power": 85, "team": "Асгард"}
]
Что должна делать программа
1. Вывести всех героев
Пример:
Железный человек — сила 95 — команда Мстители
Тор — сила 100 — команда Мстители
Локи — сила 85 — команда Асгард
2. Найти самого сильного героя
Вывести:
Самый сильный герой: Тор
3. Показать только героев команды "Мстители"
4. Добавить нового героя
Пользователь вводит:
имя
силу
команду
Добавить нового героя в список.
5. Дополнительное задание
Удалить героя по имени.
    """
    heroes = [
        {"name": "Железный человек", "power": 95, "team": "Мстители"},
        {"name": "Тор", "power": 100, "team": "Мстители"},
        {"name": "Локи", "power": 85, "team": "Асгард"}
    ]
    power_max = 0
    for i in heroes:
        print(f"{i["name"]} - сила {i["power"]} - команда {i["team"]}")
    for i in heroes:
        if i["power"]>power_max:
            power_max = i["power"]
    print(power_max)
    for i in heroes:
        if i["team"] == "Мстители":
            print(i)
    name = input("name: ")
    power = int(input("power: "))
    team = input("team: ")
    heroes.append({"name": name})
    heroes[3]["power"] = power
    heroes[3]["team"] = team
    print(heroes[3])
    man = input("Введите героя: ")
    if man in heroes[0]["name"]:
        print(heroes.remove(heroes[0]))
    if man in heroes[1]["name"]:
        print(heroes.remove(heroes[1]))
    if man in heroes[2]["name"]:
        print(heroes.remove(heroes[2]))
    if man in heroes[3]["name"]:
        print(heroes.remove(heroes[3]))


def lesson_167():
    """
    📌 Задача 3 — база LEGO-наборов
            Создать список словарей:
            lego_sets = [
                {"name": "Звезда Смерти", "pieces": 4016, "theme": "Star Wars"},
                {"name": "Бэтмобиль", "pieces": 1360, "theme": "DC"},
                {"name": "Мстители: Башня", "pieces": 5201, "theme": "Marvel"}
            ]
            Что должна делать программа
            1. Показать все наборы
            Пример:
            Звезда Смерти — 4016 деталей — Star Wars
            Бэтмобиль — 1360 деталей — DC
            Мстители: Башня — 5201 деталей — Marvel
            2. Найти набор с самым большим количеством деталей
            Вывести:
            Самый большой набор: ...
            3. Показать только наборы Star Wars
            4. Добавить новый набор
            Пользователь вводит:
            название
            количество деталей
            тему
            5. Дополнительное задание
            Посчитать общее количество деталей всех наборов
    """
    lego_sets = [
        {"name": "Звезда Смерти", "pieces": 4016, "theme": "Star Wars"},
        {"name": "Бэтмобиль", "pieces": 1360, "theme": "DC"},
        {"name": "Мстители: Башня", "pieces": 5201, "theme": "Marvel"}
    ]
    pieces = 0
    pieces_max = 0
    for i in lego_sets:
        print(f"{i["name"]} - {i["pieces"]} деталей {i["theme"]} ")
    for i in lego_sets:
        if i["pieces"]>pieces_max:
            pieces_max  = i["pieces"]
    print(pieces_max)
    for i in lego_sets:
        if i["theme"] == "Star Wars":
            print(i)
    name = input("name: ")
    pieces:int = int(input("pieces: "))
    theme = input("theme: ")
    lego_sets.append({"name": name})
    lego_sets[3]["pieces"] = pieces
    lego_sets[3]["theme"] = theme
    print(lego_sets[3])
    for i in lego_sets :
        pieces += i["pieces"]
    print(pieces)


def lesson_168():
    animals = [
              {"name": "Ася","view": "кошка","age": 6,"owner": "Артем"}
    ]
    max_age = 0
    for i in animals :
        if max_age < i["age"]:
            max_age = i["age"]
    print(max_age)


def lesson_169():
    """
    📌 Задача 1 — анализ пароля
Пользователь вводит пароль.
Программа должна:
1. вывести длину пароля
2. вывести пароль наоборот
3. проверить:
есть ли цифра
есть ли символ "!" или ?
4. вывести:
Надёжный пароль, если в пароле есть ! или ?  и цифра
или вывести Слабый пароль
    """
    login_correct = False
    login = input()
    print(len(login))
    print(login[::-1])
    for i in login:
        if i.isdigit() and  ("!" or "?" in login) :
            login_correct = True
    if login_correct:
        print("пароль надежный")
    else:
        print("пароль слабый")


def lesson_170():
    """
    📌 Задача 2 — работа с числом
Пользователь вводит число.
Программа должна:
1. найти последнюю цифру
2. удалить последнюю цифру
3. проверить:
чётное ли число
оканчивается ли оно на 5
    """
    numbers = int(input())
    f:int = numbers - numbers % 10
    print(numbers%10)
    l=f//10
    print(l)
    if numbers%2 == 0:
        print("число четное")
    else:
        print("число не четное")
    if numbers%10 == 5:
        print("число оканчивается на 5")
    else:
        print("число не оканчивается на 5")


def lesson_171():
    """
    📌 Задача 3 — бесконечное меню блоков
Создать список:
blocks = ["Земля", "TNT", "Камень"]
Сделать меню:
1 — показать блоки
2 — добавить блок
3 — удалить блок
4 — найти блок
0 — выход
    """
    blocks = ["Земля", "TNT", "Камень"]
    while True:
        print("1 — показать блоки\n2 — добавить блок\n3 — удалить блок\n4 — найти блок\n0 — выход")
        numbers = int(input())
        match numbers:
            case 1:
                for i in blocks:
                    if i != "TNT":
                        print(i)
            case 2:
                f = input()
                blocks.append(f)
            case 3:
                f = input()
                blocks.remove(f)
            case 4:
                f = int(input())
                print(blocks[f])
            case 0:
                break

def lesson_172():
    """
    📌 Задача 4 — переворот строки
Пользователь вводит строку.
Программа должна вывести:
1. строку наоборот
2. каждый второй символ (через один)
3. первые 3 символа
4. последние 3 символа
    """
    l = input()
    print(l[::-1])
    for i in l[1::2]:
        print(i)
    print(l[0:3])
    print(l[-3:])


def lesson_173():
    """
    📌 Задача 5 — подсчёт цифр числа
Пользователь вводит число.
Найти:
1. сумму цифр
2. количество цифр
Использовать:
while
%
//
    """

    number:int = int(input())
    len_number = 0
    amount = 0
    while number > 0:
        actions = number % 10
        amount += actions
        len_number += 1
        number //= 10
    print(amount)
    print(len_number)


def lesson_174():
    """
    📌 Задача 6 — работа с текстом
Пользователь вводит текст.
Программа должна:
1. перевести текст в верхний регистр
2. заменить все пробелы на "_"
3. проверить есть ли слово "python"
4. посчитать количество букв "а"
    """
    line = input()
    print(line.upper())
    print(line.replace(" ", "_"))
    print("python" in line)
    print(line.count("a"))


def lesson_175(name):
    print("привет",name)


def lesson_176(l,g):
    return l+g


def square(number):
    """
    📌 Задача 1. Квадрат числа
Создать функцию:
square(number)
которая возводит число в квадрат через:
и выводит результат.
Пример:
square(5)
↓
25
    """
    print(number ** 2)


def greet(name):
    """
    📌 Задача 2. Приветствие пользователя
Создать функцию:
greet(name)
которая выводит:
Привет, {имя_пользователя}!
    """
    print(f"привет, {name}")


def power(number,degree):
    """
    📌 Задача 3. Степень числа
Создать функцию:
power(number, degree)
которая возвращает:
number в степени degree
Пример:
power(2, 5)
↓
32
    """
    print(number ** degree)


def join_words(word1,word2):
    """
    📌 Задача 4. Соединение строк
Создать функцию:
join_words(word1, word2)
которая объединяет строки через пробел.
Пример:
join_words("Hello", "World")
↓
Hello World
    """

    print(word1 + " " + word2)
    print(word1,word2,sep=" ")







def last_digit(number):
    """
    📌 Задача 5. Последняя цифра числа
Создать функцию:
last_digit(number)
которая возвращает последнюю цифру числа.
Пример:
last_digit(123)
↓
3
    """
    print(number % 10)


def is_even(number):
    """
    📌 Задача 6. Проверка чётности
Создать функцию:
is_even(number)
которая возвращает:
True
если число чётное и
False
если нечётное.
    """
    if number % 2 == 0:
        return True
    else:
        return False

"""number = int(input())
    a = is_even(number)
    if a:
        print("число четное")
    else:
        print("число не четное")
    if is_even(number):
        print("число четное")
    else:
        print("число не четное")
        """


def greet_2(age,name = "свинка pepe"):
    return f"Привет {name}.\nТебе {age} лет"


def can_withdraw(balance, amount):
    """
    Задача 1. Банковская проверка
Необходимо написать функцию:
can_withdraw(balance, amount)
balance - текущий баланс
amount - сколько хотят снять
Функция должна проверять возможность снятия денег.
Правила:
если amount <= 0 → вернуть "Ошибка!
Нельзя снять отрицательное количество денег"

если amount > balance → вернуть
"Ошибка! Недостаточно средств на счёте"

иначе → вернуть "Снято ... денег. На балансе осталось ..." и подставить значения
Пример использования:
print(can_withdraw(100, 50))
print(can_withdraw(100, 150))
print(can_withdraw(100, -10))
    """
    if amount <= 0:
        return "Нельзя снять отрицательное количество денег"
    elif amount > balance:
        return "Ошибка! Недостаточно средств на счёте"
    else:
        return f"Снято {amount} денег.\nНа балансе осталось {balance - amount }"


def check_login(login):
    """
    Задача 2.
Проверка логина
Необходимо написать функцию: check_login(login)
Правила:
если длина меньше 4 → "Короткий"
если есть пробел → "Некорректный"
если есть цифры → "Хороший пароль с цифрами"
иначе → "Нормальный пароль"

Пример:
print(check_login("art"))
print(check_login("art 123"))
print(check_login("art123"))
print(check_login("artem"))
    """
    if len(login) < 4:
        return "Короткий"
    elif " " in login:
        return "Некорректный"
    elif not login.isalpha() :
        return "Хороший пароль с цифрами"
    else:
        return "Нормальный пароль"


def player_level(points):
    """
    Задача 3. Уровень игрока
Необходимо написать функцию:
player_level(points)
Правила:
0–99 → "новичок"
100–499 → "обычный"
500–999 → "профессионал"
1000+ → "легенда"

Пример:
print(player_level(50))
print(player_level(300))
print(player_level(700))
print(player_level(1500))

Ожидаемый вывод:
новичок
обычный
профессионал
легенда
    """
    if points <= 99:
        return "новичок"
    elif points >= 100 and points <= 499:
        return "обычный"
    elif points >= 500 and points <= 999:
        return "профессионал"
    else:
        return "легенда"


def format_user(first_name, last_name, city):
    """
    Задача 4. Форматирование пользователя (именованные аргументы)
Необходимо написать функцию:
format_user(first_name, last_name, city)
Функция должна возвращать строку:
Имя Фамилия из Город
ВАЖНО: Вызов функции должен быть только через именованные аргументы:
format_user(city="Москва", last_name="Петров", first_name="Иван")
Пример вывода: Иван Петров из Москва
    """
    return f"{first_name} {last_name} из {city}"


def report(title, items=0, status="черновик"):
    """
    Задача 5. Отчёт (значения по умолчанию)
Необходимо написать функцию:
report(title, items=0, status="черновик")
Функция должна возвращать строку:
Отчёт: <title> | количество: <items> | статус: <status>
Пример:
print(report("Продажи"))
print(report("Склад", 15))
print(report("Финансы", 30, "завершён"))
Ожидаемый вывод:
Отчёт: Продажи | количество: 0 | статус: черновик
Отчёт: Склад | количество: 15 | статус: черновик
Отчёт: Финансы | количество: 30 | статус: завершён
    """
    return f"Отчёт: {title} | количество: {items} | статус: {status}"


def secure_check(password):
    """
    Задача 6. Проверка пароля
Необходимо написать функцию: secure_check(password)

Правила:
если длина меньше 6 → "слабый"
если нет цифры → "нет цифр"
если нет заглавной буквы → "нет заглавной буквы"
иначе → "надёжный"

Пример:
print(secure_check("abc"))
print(secure_check("abcdef"))
print(secure_check("abcdef1"))
print(secure_check("Abcdef1"))
Ожидаемый вывод:
слабый
нет цифр
нет заглавной буквы
надёжный
    """
    if len(password) < 6:
        return "слабый"
    elif password.isalpha():
        return "нет цифр"
    elif password.islower():
        return "нет заглавной буквы"
    else:
        return "надёжный"


def teleport(x, y, z, shift=10):
    """
    Задача 7. Телепорт координат
Необходимо написать функцию: teleport(x, y, z, shift=10)
Функция должна возвращать новые координаты:
x + shift
y + shift
z + shift
Возвращаемое значение: (x, y, z)
Пример:
print(teleport(1, 2, 3))
print(teleport(1, 2, 3, shift=5))
Ожидаемый вывод: (11, 12, 13) (6, 7, 8)
    """
    return x + shift,y + shift,z + shift

a = 10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000055665656
def lesson_177():
    r = 1,2,3
    b = a + 100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
    print(a)
    print(b)
    d = a + b
    print(d)
    print(y)
    h.append(d)
    print(h)


visits = 0

def add_visit():
    global visits
    """
    📌 Задача 1. Глобальный счётчик посещений
    Создай глобальную переменную:
    visits = 0
    Необходимо написать функцию:
    add_visit()
    При каждом вызове функция должна увеличивать количество посещений на 1 и выводить текущее значение счётчика.
    Пример:
    add_visit()
    add_visit()
    add_visit()
    Ожидаемый вывод:
    Посещений: 1
    Посещений: 2
    Посещений: 3
    """
    visits += 1
    print(visits)


def show_player():
    """
    📌 Задача 2. Локальная переменная игрока
Необходимо написать функцию:
show_player()
Внутри функции создать локальную переменную:
name = "Артём"
Вывести её значение.
После вызова функции попробовать вывести переменную name вне функции.
Ответить на вопрос:
Почему возникает ошибка?

Также, Артём, теперь ты можешь понять по этой задаче почему так важно использовать return и в чём заключается его основное назначение
В начале следующего занятия обязательно с тобой ещё раз это обсудим
    """
    name = "Артём"
    print(name)


def first_last(text):
    return f"Первая буква:{text[0]} , последняя буква:{text[-1]}"

secret_symbol = "#"
def check_symbol(text):
    """
    📌 Задача 4. Проверка секретного символа
Создать глобальную переменную:
secret_symbol = "#"
Необходимо написать функцию:
check_symbol(text)
Если первый символ строки совпадает с secret_symbol, вернуть:
Секретный код найден
Иначе вернуть:
Секретный код не найден
Использовать индексацию строки.
    """
    if text[0] == secret_symbol:
        return "Секретный код найден"
    else:
        return "Секретный код не найден"

settings = {
    "volume": 50,
    "brightness": 80
}
def change_volume(new_volume):
    """
    📌 Задача 5. Изменение глобального словаря
Создать глобальный словарь:
settings = {
    "volume": 50,
    "brightness": 80
}
Необходимо написать функцию:
change_volume(new_volume)
которая изменяет громкость в словаре.
После изменения вывести словарь.
    """
    settings["volume"] = new_volume
    print(settings)


def lesson_178(*æ2ǔ):
    print(æ2ǔ)
    print(type(æ2ǔ))\


def lesson_179(*args):
    amount = 0
    for i in args:
        amount += i
    return amount


def lesson_180(**kwargs):
    print(kwargs)
    print(type(kwargs))


def lesson_181(**kwargs):
    for key,value in enumerate(kwargs.items()):
        print(key,value)


def lesson_182(**kwargs):
    for key in kwargs:
        print(key,":",kwargs[key])


def lesson_183(*args,**kwargs):
    amount = 0
    for _ in args:
       amount += 1
    print(f"количество равно:{amount}")
    for key,value in kwargs.items():
        print(key,"-",value)


def magic_sum(*args):
    """
    📌 Задача 1. Магический калькулятор
Необходимо написать функцию:
magic_sum(*args)
Функция должна принимать любое количество чисел и возвращать их сумму.
Пример:
print(magic_sum(1, 2, 3))
print(magic_sum(10, 20, 30, 40))
Ожидаемый вывод:
6
100
    """
    amount = 0
    for i in args:
        amount += i
    print(amount)


def highest_mountain(*args):
    """
    📌 Задача 2. Самая высокая гора
Необходимо написать функцию:
highest_mountain(*args)
В функцию передаются высоты гор.
Функция должна вернуть самую высокую гору.
Пример:
print(highest_mountain(8849, 5642, 6960, 4808))
Ожидаемый вывод:
8849
    """
    maxx = 0
    for i in args:
        if i > maxx:
            maxx = i
    print(maxx)


def space_passport(**kwargs):
    """
    📌 Задача 3. Космический паспорт
Необходимо написать функцию:
space_passport(**kwargs)
Функция должна вывести всю информацию о космонавте.
Пример:
space_passport(
    name="Артём",
    planet="Марс",
    rank="Исследователь"
)
Ожидаемый вывод:
name: Артём
planet: Марс
rank: Исследователь
    """
    for key,value in kwargs.items():
        print(key,":",value)


def pet_profile(**kwargs):
    """
    📌 Задача 4. Профиль питомца
Необходимо написать функцию:
pet_profile(**kwargs)
Функция должна вывести все характеристики питомца.
Пример:
pet_profile(
    name="Барсик",
    age=3,
    color="рыжий",
    weight=5
)
Возможный вывод:
name: Барсик
age: 3
color: рыжий
weight: 5
    """
    for key,value in kwargs.items():
        print(key,":",value)


def repeat_word(word,count):
    """
    📌 Задача 5. Таинственный повторитель
Необходимо написать функцию:
repeat_word(word, count)
Функция должна вывести слово count раз.
При этом в цикле использовать:
for _ in range(...)
Пример:
repeat_word("Привет", 3)
Ожидаемый вывод:
Привет
Привет
Привет
    """
    for _ in range(count):
        print(word)



def backpack(*args):
    """
    📌 Задача 6. Туристический рюкзак
Необходимо написать функцию:
backpack(*args)
В функцию передаются вещи, которые турист берёт в поход.
Функция должна:
Вывести все вещи.
Вывести их количество.

Пример:
backpack(
    "палатка",
    "фонарик",
    "спальник",
    "котелок"
)
Ожидаемый вывод:
Палатка
Фонарик
Спальник
Котелок

Всего вещей: 4
    """
    amount = 0
    for i in args:
        print(i.title())
        amount += 1
    print(f"Всего вещей: {amount}")


def lesson_184(second):
    print(second)
    if second == 0:
        return "0"


def is_valid_callsign(callsign):
    reasons = []
    if len(callsign) < 4 or len(callsign) > 12:
        reasons.append("слишком большой или маленький позывной")
    if callsign.isalpha():
        reasons.append("нет цифр")
    if callsign.islower():
        reasons.append("нет буквы в верхнем регистре")
    if callsign.isspace():
        reasons.append("есть пробел")
    if callsign[0].isdigit() or callsign[-1].isdigit():
        reasons.append("первый или последний символ - цифра")
    return (len(reasons) == 0,",".join(reasons))





if __name__ == "__main__":
    a = is_valid_callsign("A1212we")
    print(a)