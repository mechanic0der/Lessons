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


if __name__ == "__main__":
    test_set({1})