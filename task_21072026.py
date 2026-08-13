"""
Roguelike: одна жизнь, один шанс
Написать текстовый roguelike — жанр игр, где каждое прохождение уникально и смерть означает конец.
Обязательная структура:
Карта — список списков 5×5. Клетки:
	"." — пустая,
	"#" — стена,
	"E" — враг,
	"T" — сокровище,
	"X" — выход,
	"@" — герой.
[
	[".", ".", "#", "#", "#"],
	[".", ".", "#", "T", "#"],
	["E", ".", "#", ".", "E"],
	[".", ".", ".", ".", "."],
	[".", "E", ".", ".", "X"],
]

Карту задать в коде — придумать самому.
Герой — словарь: hp, attack, defense, gold, position (кортеж (row, col)).

Функции которые написать:
show_map(dungeon, hero_pos) — выводит карту, обозначая позицию героя символом @.
move_hero(dungeon, hero, direction) — перемещает героя ("w"/"a"/"s"/"d"). Проверяет стены.
Если клетка — враг: бой. Если сокровище: прибавить золото. Если выход: победа. Возвращает строку с результатом хода.
fight(hero, enemy_hp, enemy_attack) — бой до смерти одного из участников. Ходят по очереди. Урон = max(1, attack - defense).
Возвращает (survived: bool, hero_hp_after: int).
generate_enemy() — возвращает словарь случайного врага с hp от 15 до 40 и attack от 5 до 15.
Использовать детерминированный псевдослучай через % —
например (day * 37 + position[0] * 13 + position[1] * 7) % 26 + 15 для hp, где day — счётчик ходов.
Главный цикл — принимать команды w/a/s/d/q, показывать карту и статус после каждого хода.
Игра заканчивается при смерти героя или достижении выхода.

Обязательные условия:
Минимум 5 функций
Карта хранится как список списков
Герой — словарь
match-case для разбора команд
while для главного цикла
Хоть одно множество или кортеж по смыслу
"""
from random import randint, choice


enemy_symbol = '😈'
exit_symbol = '🗝'
gold_symbol = '💰'
wall_symbol = '🟫'
dot_symbol = '•'
user_game_map = [
	[".", ".", "#", "#", "#"],
	["T", ".", "#", "T", "#"],
	["E", ".", "#", ".", "E"],
	[".", ".", ".", ".", "."],
	[".", "E", ".", ".", "X"],
]


# region Map
def create_map(
		size: int = 5,
		wall_coef: float = 0.3,
		gold_coef: float = 0.1,
		enemy_coef: float = 0.1,
) -> list | None:
	if size > 40:
		print('Слишком большой размер карты')
		return None
	cells_count = size ** 2
	new_game_map = [
		[dot_symbol for _ in range(size)]
		for _ in range(size)
	]
	# show_map(game_map, (0,0))
	# Определяем выход
	exit_position = (randint(0, size - 1), randint(size // 2, size - 1))
	new_game_map[exit_position[0]][exit_position[1]] = exit_symbol

	# Создание золота
	gold_points_count = int(cells_count * gold_coef)
	gold_points_count = randint(gold_points_count // 2, gold_points_count)
	gold_points = {
		(randint(0, size - 1), randint(0, size - 1))
		for _ in range(gold_points_count)
	}
	gold_points.discard(exit_position)
	for point in gold_points:
		new_game_map[point[0]][point[1]] = gold_symbol
	# print(f"Золото: {len(gold_points)}", gold_points)

	# Создание стен
	walls_points = set()
	walls_points_count = int(cells_count * wall_coef)
	walls_points_count = randint(walls_points_count // 2, walls_points_count)
	while walls_points_count > 0:
		wall_point = (randint(0, size - 1), randint(0, size - 1))
		if wall_point not in gold_points:
			walls_points.add(wall_point)
			walls_points_count -= 1
	walls_points.discard(exit_position)
	for point in walls_points:
		new_game_map[point[0]][point[1]] = wall_symbol
	# print(f"Стены: {len(walls_points)}", walls_points)

	# Создание врагов
	enemy_points = set()
	enemy_points_count = int(cells_count * enemy_coef)
	enemy_points_count = randint(enemy_points_count // 2, enemy_points_count)
	while enemy_points_count > 0:
		point = (randint(0, size - 1), randint(0, size - 1))
		if point not in walls_points and point not in gold_points:
			enemy_points.add(point)
			enemy_points_count -= 1
	enemy_points.discard(exit_position)
	for point in enemy_points:
		new_game_map[point[0]][point[1]] = enemy_symbol
	# print(f"Врагов: {len(enemy_points)}", enemy_points)
	print(f"Сгенерирована карта размером {len(new_game_map)}x{len(new_game_map)}")
	print(f"Параметры карты: {len(walls_points)} стен, {len(enemy_points)} врагов, {len(gold_points)} золота")
	print(f'Выход: {exit_position}')
	return new_game_map


def show_map(
		game_map_to_show: list,
		hero_position: tuple | None = None
) -> None:
	print("Карта игры:")
	for i, row in enumerate(game_map_to_show):
		print(i, "\t", end='')
		for j, cell in enumerate(row):
			if hero_position is not None and (i, j) == hero_position:
				print(' \U0001F600 ', end='')
			else:
				print(cell.center(3), end='')
		print()
# endregion Map


# region Hero
def get_start_hero_position(game_map) -> tuple:
	map_size = len(game_map)
	left_dot_points = [
		(i, j) for i in range(map_size)
		for j in range(map_size)
		if game_map[i][j] == dot_symbol and j < map_size // 2
	]
	if len(left_dot_points) > 0:
		return choice(left_dot_points)
	return 0, 0


def create_hero(start_position: tuple | None = None) -> dict:
	return {
		"health": randint(20, 100),
		"defense": randint(20, 100),
		"attack": randint(20, 50),
		"gold": randint(5, 30),
		"position": start_position or (0, 0)
	}


def move_hero(
		game_map: list,
		hero: dict,
		direction: str,
		show_empties: bool = False,
) -> dict | str | bool:
	# Готовим необходимые переменные
	map_size = len(game_map)
	action_message = f"Ход {direction.upper()} | "
	hero_pos_i, hero_pos_j = hero.get("position")

	# В зависимости от направления определяем новые координаты героя
	match direction:
		case 'w':
			hero_pos_i, hero_pos_j = hero_pos_i - 1, hero_pos_j
		case 'a':
			hero_pos_i, hero_pos_j = hero_pos_i, hero_pos_j - 1
		case 's':
			hero_pos_i, hero_pos_j = hero_pos_i + 1, hero_pos_j
		case 'd':
			hero_pos_i, hero_pos_j = hero_pos_i, hero_pos_j + 1

	# Проверка на выход за границы поля
	if hero_pos_i not in range(0, map_size) or hero_pos_j not in range(0, map_size):
		if show_empties:
			print(action_message, 'Попытка выйти за границы поля пресечена!')
		return hero

	# Определяем следующую клетку на которую хочет переместиться герой
	allow_position_update = True  # Изначально разрешаем перемещение в новую позицию
	next_cell = game_map[hero_pos_i][hero_pos_j]
	action_message += f"({hero_pos_i}:{hero_pos_j}) [{next_cell}] |"
	if next_cell == dot_symbol:
		if show_empties:
			print(action_message, f"Герой наступил на пустую клетку!")
	elif next_cell == wall_symbol:
		if show_empties:
			print(action_message, "Герой уперся в стену!")
		allow_position_update = False  # Запретить обновление позиции
	elif next_cell == gold_symbol:
		found_gold = randint(5, 15)
		hero['gold'] += found_gold
		print(action_message, "Герой нашел", found_gold , "золота! (теперь у него", hero['gold'], "золота)")
		show_map(game_map, (hero_pos_i, hero_pos_j))
	elif next_cell == enemy_symbol:
		new_enemy = create_enemy()
		print(
			action_message,
			f"Герой нашел врага (здоровье {new_enemy['health']}, атака: {new_enemy['attack']}) - ",
			end=''
		)
		new_hero_health = fight(hero, new_enemy)
		if new_hero_health == 0:
			print("Герой погиб")
			return False
		hero['health'] = new_hero_health
		print(f"победа, осталось {new_hero_health} здоровья")
	elif next_cell == exit_symbol:
		return action_message + f" Герой выиграл, унес с собой {hero['gold']} золота и {hero['health']} здоровья!"
	# Обновляем положение героя на карте
	if allow_position_update:
		hero.update({"position": (hero_pos_i, hero_pos_j)})
		game_map[hero_pos_i][hero_pos_j] = '.'
	return hero
# endregion Hero


# region Enemy
def create_enemy() -> dict:
	# возвращает словарь случайного врага с hp от 15 до 40 и attack от 5 до 15.
	return {
		"health": randint(15, 60),
		"attack": randint(5, 25)
	}


def fight(hero: dict, enemy: dict) -> int:
	hero_hp = hero.get("health")
	hero_attack = hero.get("attack")
	hero_defense = hero.get("defense")
	enemy_hp = enemy.get("health")
	enemy_attack = enemy.get("attack")
	while hero_hp > 0 and enemy_hp > 0:
		hero_hp = max(0, hero_hp - max(1, enemy_attack - hero_defense))
		enemy_hp = max(0, enemy_hp - hero_attack)
	return hero_hp
# endregion Enemy


def run_game():
	# Создаем карту или берем созданную вручную, задаем начальную позицию героя, показываем карту
	test_game_map = create_map(
		size=20,
		enemy_coef=0.2,
	) or user_game_map
	start_hero_position = get_start_hero_position(test_game_map)
	print("Начальная позиция героя:", start_hero_position)
	show_map(test_game_map, start_hero_position)

	# Создаем героя
	hero = create_hero(start_position=start_hero_position)
	print(f"Создан герой со следующими характеристиками:", hero)
	moves = 0
	available_moves = ["w", "a", "s", "d"]
	# Играем
	while True:
		moves += 1
		move_direction = choice(available_moves)
		hero = move_hero(test_game_map, hero, direction=move_direction, show_empties=True)
		if isinstance(hero, str):
			print(hero)
			print(f"Количество ходов: {moves}")
			return True
		elif isinstance(hero, bool):
			print("Герой погиб после сражения с врагом!")
			print(f"Количество ходов: {moves}")
			return False
		elif not isinstance(hero, dict):
			raise TypeError("Неверный тип данных!")


if __name__ == '__main__':
	run_game()