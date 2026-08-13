"""
Симулятор колонии на Марсе

	Написать симулятор управления марсианской колонией. Колония — словарь с ресурсами и населением.
	Написать функцию create_colony(name, **resources) — создаёт колонию. Обязательные ресурсы по умолчанию:
	oxygen=100, water=100, food=100, population=10, day=1.

	Написать функцию next_day(colony) — симулирует один день. Каждый житель потребляет:
	кислород -2, воду -1.5, еду -1. Если любой ресурс падает до 0 — население уменьшается на тех кто не получил ресурс.
	Если население 0 — колония погибла. День прибавить на 1. Возвращать словарь с изменениями за день.
	Написать функцию supply_drop(*resources, colony) — пополнение запасов.
		*resources — кортежи (название_ресурса, количество).
		Прибавить к соответствующим полям колонии.

	Написать функцию colony_report(colony) — выводит красивый отчёт:
	день, ресурсы на человека и сколько дней протянет колония при текущем потреблении.

	Главный цикл — симулировать дни до победы (день 30) или гибели колонии:
	while colony["day"] <= 30 and colony["population"] > 0:
		Пример отчёта:
	=== КОЛОНИЯ ЗАРЯ | ДЕНЬ 5 ===
	Население:  10 человек
	Кислород:   900 ед. (90.0 на чел.) — хватит на 45 дней
	Вода:       925 ед. (92.5 на чел.) — хватит на 61 день
	Еда:        950 ед. (95.0 на чел.) — хватит на 95 дней
"""
from math import ceil, floor


day_doses = {
	"oxygen": 2,
	"water": 1.5,
	"food": 1,
	"wood": 1,
}

resource_russians = {
	"oxygen": "Кислород",
	"water": "Вода",
	"food": "Еда",
	"wood": "Дерево",
}

def create_colony(name: str, **resources):
	# oxygen=100, water=100, food=100, population=10, day=1
	colony_res = {}

	# Добавляем (обновляем) ресурсы по умолчанию
	colony_res.update({
		"oxygen": 100,
		"water": 100,
		"food": 100,
		"population": 10,
		"day": 0,
		"name": name,
	})

	# Добавили ресурсы пользователя
	colony_res.update(resources)
	return colony_res


def next_day(colony: dict):
	rip_population = 0
	out_colony = colony.copy()
	for resource, value in colony.items():
		if resource in ["population", "day", "name"]:
			continue
		resource_by_day = colony["population"] * day_doses[resource]
		# Если потратить надо больше, чем есть
		if resource_by_day > value:
			# Считаем число людей которым не хватило
			resource_rip = ceil((resource_by_day - value) / day_doses[resource])
			# Обновляем число погибших в этот день
			rip_population = max(resource_rip, rip_population)
			out_colony[resource] = 0
		else:
			out_colony[resource] = value - resource_by_day
	# Цикл по ресурсам завершен
	out_colony["day"] = colony["day"] + 1
	out_colony["population"] = max(colony["population"] - rip_population, 0)
	return out_colony


def colony_report(colony: dict):
	"""
	=== КОЛОНИЯ ЗАРЯ | ДЕНЬ 5 ===
	Население:  10 человек
	Кислород:   900 ед. (90.0 на чел.) — хватит на 45 дней
	Вода:       925 ед. (92.5 на чел.) — хватит на 61 день
	Еда:        950 ед. (95.0 на чел.) — хватит на 95 дней
	"""
	colony_population = colony["population"]
	colony_name = colony["name"]
	colony_day = colony["day"]
	print(f"=== КОЛОНИЯ {colony_name} | ДЕНЬ {colony_day} ===")
	print(f"Население:  {colony_population} человек")
	for resource, value in colony.items():
		if resource in ["population", "day", "name"]:
			continue
		resource_russian = resource_russians.get(resource)
		resource_days = floor(value / (day_doses[resource] * colony["population"]))
		print(f"{resource_russian}:   {value} ед. ({day_doses[resource]} на чел.) — хватит на {resource_days} дней")


def colony_life():
	my_colony = create_colony("Смородинка", **{
		"wood": 3295,
		"oxygen": 5983,
		"water": 5202,
		"food": 4877,
		"population": 100,
	})
	print(my_colony)
	while my_colony["day"] < 30:
		my_colony = next_day(my_colony)
		if my_colony["population"] == 0:
			print("Колония умерла")
			return
		colony_report(colony=my_colony)
	print("Колония выжила месяц")


if __name__ == '__main__':
	colony_life()