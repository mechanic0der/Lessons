from openpyxl.styles.builtins import total


def yt():
    f = "return"
    print(f[1:])
    d = "Артемаааааа ааааа аааааааа".split(" ")
    print(d)
    age = int(input())
    status = "взрослый" if age >= 18 else "ребёнок"
    print(status)
    for i in range(6):
        if i == 3:
            continue
        print(i)
    g = ['6','7']
    for i in range(len(g)):
        print(g[i])


def list_method(numbers: list):
    numbers.append(67)
    numbers.remove(67)
    numbers.sort(reverse = True)
    numbers.insert(1,696752)
    numbers.reverse()
    print(numbers)
    r = [i for i in range(1,6)]
    print(r)
    f = [i * 3 for i in r]
    print(f)
    kk = 1,2
    t = list(kk)
    t.append(3)
    kk = tuple(t)
    print(kk)


def test_tuple(numbers_tuple: tuple):
    x,y = numbers_tuple
    print(x)
    print(y)


def test_set(numbers: set):
    numbers.add(676767676776767676767676)
    numbers.remove(676767676776767676767676)
    a = {1,2,3}
    b = {3,4,5}
    print(a & b)
    print(a ^ b)
    print(a | b)
    print(a - b)


def dict_1(r,it=67):
    students = {"name": "Вася","age": 21}
    students["city"] = "Москва"
    students["age"] = 22
    for i in students.values():
        print(i)
    city = students.pop("city","6767676767676767676767676767677676767676767676767676767676767676767676767676767676767")
    print(students)
    print(city)
    students.popitem()
    print(students)
    students_2 = {"age": 6767676767676767676767676767677676767676767676767676767676767676767676767676767676767}
    students.update(students_2)
    print(students)
    keys = ["name","age","city"]
    user = dict.fromkeys(keys)
    print(user)


def pank(*args):
    print(args)


def pank_2(**kwargs):
    print(kwargs)


number2 = lambda x: x ** 2


def list_comprehension(line: list):
    line_2 = [i for i in line if i % 2 == 0 ]
    line_3 = [i if i % 2 == 0 else 0 for i in line]
    line_4 = ["большой" if i > 5 else "маленький" for i in line if i % 2 == 0]
    age = 7
    status = "Взрослый" if age >= 18 else "Детский"
    a = "Привет"
    return line_2, line_3, status,repr(a),line_4


def test_error_2():
    try:
        a = int(input())
        b = int(input())
        print(a / b)
    except Exception as error:
        print(f"произошла ошибка: {error}")
    else:
        print("error - no")
    finally:
        print("k - s")


def check_age(age):
    if age < 0:
        raise ValueError("возраст не может быть отрицательным")
    return age


def test_else():
    numbers = [67,67,67,5]
    for i in numbers:
        if i == 5:
            print("5!!!!!!!")
            break
    else:
        print("5 - нет")


def test_morj67():
    data = [9,4,"m"]
    n = len(data)
    if n > 2:
        print(n)
    if (m := len(data)) > 2:
        print(m)


def file_error():
    with open("jkd,cdl;cdf;.txt","r") as file:
        file.read()


def f_str(number):
    for i in range(number):
        r = f"Мне {number} лет"
        print(r)


def f_file(name = 67):
    try:
        with open(f"{name}.txt","r") as file:
            print(file.read())
    except FileNotFoundError:
        with open("67.txt","r") as file:
            print(file.read())



def file_(number):
    r = number * 5
    total = (r + number) ** 2
    return total


def file_2(total):
    with open("total.txt","w+") as file:
        file.write(f"{total}")
        file.seek(0)
        return file.read()


def glas_(line:str):
    result = 0
    glas = "аоеёюяэуыи"
    for i in line.lower():
        if i in glas:
            result += 1
    return result


def chet(f):
    return f % 2 == 0


def hero2(x):
    return x ** 2


def len_1(word):
    return len(word)


def i (text):
    return text.lower().replace(" ","") == text[::-1].lower().replace(" ","")


def format1():
    s = {}
    with open(f"{input("")}.txt","r") as file:
        a = file.read().split()
    with open(f"{input("")}.txt","a") as _:
        for i in a:
            if i in s:
                s[i] += 1
            else:
                s[i] = 1
    print(s)


class Person:
    def __init__(self, name,surname, strength, age):
        self.name = name
        self.surname = surname
        self.strength = strength
        self.age = age
    def goal(self):
        print(f"{self.name} {self.surname} забивает гол")




if __name__ == "__main__":
    futbol1 = Person("Lamine","Yamal",72358953407845678964578934567890,21)
    futbol1.goal()
    futbol2 = Person("Leo","Messi",676776767676767767676767676767767676776894578965789,37)

