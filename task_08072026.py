"""
Робот получает строку команд и выполняет их. Написать интерпретатор.
Команды: F — вперёд на 1 шаг, B — назад на 1 шаг, L — повернуть влево на 90°, R — повернуть вправо на 90°, F3 — вперёд на 3 шага (число после буквы — количество повторений), REPEAT(cmd, n) — выполнить команду cmd ровно n раз.
Написать функцию parse_commands(program) — принимает строку с командами через пробел, возвращает список нормализованных команд (каждая команда — отдельный элемент, F3 разворачивается в ["F", "F", "F"], REPEAT(F,3) тоже).
Написать функцию execute(commands) — выполняет список команд. Начальная позиция (0, 0), направление — север (наверх).
Возвращает финальную позицию (x, y) и направление.
Использовать кортеж для направления: север (0,1), юг (0,-1), восток (1,0), запад (-1,0).
Написать функцию path_length(commands) — возвращает общее расстояние, пройденное роботом (только шаги F и B).
Что использовать:
.split() — разбить программу на команды
.startswith() и срезы — для разбора F3
match-case — для выполнения команд
Словарь поворотов — для L и R
Пример работы:
program = "F3 R F2 L F REPEAT(B,2)"

parse_commands(program) → ["F","F","F","R","F","F","L","F","B","B"]

execute(...)  → позиция (2, 2), направление север
path_length(...) → 9 шагов
"""


def parse_commands(program: str):
    commands = program.split()
    out_commands = list()
    for cmd in commands:
        if 'REPEAT' in cmd:
            command_data = cmd.replace('REPEAT', '')
            command_data = command_data.replace('(', '').replace(')', '') # "B,2"
            command, count = command_data.split(',')
            for _ in range(int(count)):
                out_commands.append(command)
        elif cmd[-1].isdecimal():
            command, count = cmd[0], int(cmd[1:])
            for _ in range(int(count)):
                out_commands.append(command)
        else:
            out_commands.append(cmd)
    return out_commands


def execute(parsed_commands):
    position = [0, 0]  # Y, X
    walk = {"F": [1, -1], "B": [-1, 1]}
    dir_walk = {"R": 1, "L": -1}
    direction = 0  # 0: Север, 1: Восток, 2: Юг, 3: Запад
    for cmd in parsed_commands:
        if cmd in walk:
            position[direction % 2] += walk[cmd][direction // 2]
        if cmd in dir_walk:
            direction = (direction + dir_walk[cmd]) % 4
    print(position, direction)


def path_length(parsed_commands: list):
    return parsed_commands.count('F') + parsed_commands.count('B')


if __name__ == '__main__':
    commands = parse_commands("F3 R F2 L F REPEAT(B,2)")
    execute(commands)
    print(path_length(commands))
