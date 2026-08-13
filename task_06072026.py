"""
Дана звёздная карта в виде списка списков (матрица) —
каждая клетка либо пустое пространство 0, либо астероид 1, либо станция 2. Написать навигационные функции.
Написать функцию count_neighbors(grid, row, col) —
возвращает количество астероидов 1 в соседних клетках (8 направлений) от указанной позиции. Не выходить за границы карты.
Написать функцию find_stations(grid) — возвращает список кортежей (row, col) со всеми позициями станций 2.
Что использовать:
Вложенный for — для обхода матрицы
Список visited — чтобы не посещать клетки дважды
Кортежи (row, col) — для координат
in — для проверки посещённых клеток
Пример работы:
grid = [
    [0, 1, 0, 0, 2],
    [0, 0, 0, 1, 0],
    [1, 0, 2, 0, 0],
    [0, 0, 0, 1, 0],
]

count_neighbors(grid, 1, 2)  → 2  (астероиды на [0][1] и [1][3])
find_stations(grid)           → [(0,4), (2,2)]
"""


def count_neighbors(grid, row, col):
	asteroids = 0
	for r in range(row - 1, row + 2):
		for c in range(col - 1, col + 2):
			if r < 0 or c < 0 or r > len(grid) + 1 or c > len(grid[0]) + 1:
				continue
			if grid[r][c] == 1:
				asteroids += 1
	return asteroids


def find_stations(grid):
	stations = []
	for r in range(len(grid)):
		for c in range(len(grid[0])):
			if grid[r][c] == 2:
				stations.append((r, c))
	return stations


if __name__ == '__main__':
	grid = [
		[0, 1, 0, 0, 2],
		[0, 0, 0, 1, 0],
		[1, 0, 2, 0, 0],
		[0, 0, 0, 1, 0],
	]
	print(count_neighbors(grid, 2, 3))
	print(find_stations(grid))
