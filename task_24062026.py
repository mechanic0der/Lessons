"""Система инициативы в бою
В RPG перед боем каждый персонаж бросает кубик — у кого больше сумма кубика и модификатора ловкости, тот ходит первым.
Написать систему расчёта очерёдности ходов.
Написать функцию calculate_initiative(fighters), которая принимает список словарей. Каждый словарь — боец с полями name,
dex_mod (модификатор ловкости, может быть отрицательным), roll (результат броска кубика 1–20).
Функция возвращает новый список словарей, отсортированный по убыванию итоговой инициативы (roll + dex_mod).
При равной инициативе — сортировать по dex_mod убыванием.
Каждый словарь в результате дополнить полем initiative с итоговым значением и order с порядковым номером хода.
Что использовать:
sorted() с key= и reverse=True
for с enumerate() — для расстановки порядковых номеров
f-строки — для вывода очерёдности
Пример работы:
fighters = [
    {"name": "Арагорн",  "dex_mod": 3, "roll": 14},
    {"name": "Гэндальф", "dex_mod": 1, "roll": 18},
    {"name": "Леголас",  "dex_mod": 5, "roll": 12},
    {"name": "Гимли",    "dex_mod": -1, "roll": 17},
]
Результат:
1. Гэндальф  — инициатива 19 (бросок 18 + мод 1)
2. Леголас   — инициатива 17 (бросок 12 + мод 5)
3. Гимли     — инициатива 16 (бросок 17 + мод -1)
4. Арагорн   — инициатива 17 (бросок 14 + мод 3)
Подсказка: при равной инициативе у Леголаса и Арагорна (оба 17) — Леголас выше, потому что его dex_mod больше.
"""

all_fighters = [
	{"name": "Арагорн",  "dex_mod": 3, "roll": 14},
	{"name": "Гэндальф", "dex_mod": 1, "roll": 18},
	{"name": "Леголас",  "dex_mod": 5, "roll": 12},
	{"name": "Гимли",    "dex_mod": 14, "roll": 32},
	{"name": "Гимли2",    "dex_mod": -4, "roll": 6},
	{"name": "Гимли3",    "dex_mod": -80, "roll": 45},
	{"name": "Гимли4",    "dex_mod": -11, "roll": 2},
	{"name": "Гимли5",    "dex_mod": 45, "roll": 1},
]

def calculate_initiative(fighters: list):

	for fighter in fighters:
		print(fighter)
		fighter.update({"initiative": fighter["roll"] + fighter["dex_mod"]})
	fighters = sorted(fighters, key=lambda x: x["initiative"], reverse=True)
	initiative_set = sorted(set([fighter["initiative"] for fighter in fighters]), reverse=True)
	result = []
	print('Result')
	for initiative in initiative_set:
		initiative_fighters = [fighter for fighter in fighters if fighter["initiative"] == initiative]
		sorted_initiative_fighters = sorted(initiative_fighters, key=lambda x: x["dex_mod"], reverse=True)
		for fighter in sorted_initiative_fighters:
			result.append(fighter)
			print(fighter)


if __name__ == '__main__':
	calculate_initiative(all_fighters)
