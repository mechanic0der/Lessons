"""
🏆 Турнирная сетка
Написать систему проведения турнира на выбывание. Участники — список имён,
их количество должно быть степенью двойки (4, 8, 16...).
Написать функцию validate_bracket(participants) — проверяет что количество участников — степень двойки.
Подсказка: n & (n - 1) == 0 работает только для степеней двойки.

Написать функцию simulate_match(fighter1, fighter2, scores) —
принимает двух участников и словарь их рейтингов scores. Победитель — у кого рейтинг выше.
При равном рейтинге — первый по алфавиту. Возвращает имя победителя и описание матча строкой.

Написать функцию run_tournament(participants, scores) — проводит весь турнир.
На каждом раунде разбивает участников на пары (первый против второго, третий против четвёртого и т.д.),
симулирует все матчи, победители идут в следующий раунд. Выводить результаты каждого раунда. Возвращает имя чемпиона.
Что использовать:
while len(participants) > 1 — главный цикл турнира
for i in range(0, len(participants), 2) — разбивка на пары
f-строки — для красивого вывода каждого раунда
Пример вывода:
=== РАУНД 1 ===
Арагорн (90) vs Боромир (75)  → Арагорн
Леголас (85) vs Гимли (80)    → Леголас

=== РАУНД 2 (ФИНАЛ) ===
Арагорн (90) vs Леголас (85)  → Арагорн

🏆 ЧЕМПИОН: Арагорн

"""


def validate_bracket(participants: list):
	# print(len(participants), bin(len(participants)))
	# print(len(participants) - 1, bin(len(participants) - 1))
	# & - амперсанд, выполняет конъюнкцию
	return True if len(participants) & (len(participants) - 1) == 0 else False


def simulate_match(fighter1_name, fighter2_name, fighters_scores: dict):
	# Арагорн (90) vs Боромир (75)  → Арагорн
	out_string = f"{fighter1_name} ({fighters_scores[fighter1_name]}) vs {fighter2_name} ({fighters_scores[fighter2_name]})"
	winner = None
	fighter1_score = fighters_scores.get(fighter1_name)
	fighter2_score = fighters_scores.get(fighter2_name)
	if fighter1_score > fighter2_score:
		out_string += " -> " + fighter1_name
		winner = fighter1_name
	elif fighter2_score > fighter1_score:
		out_string += " -> " + fighter2_name
		winner = fighter2_name
	else:
		out_string += " -> " + (fighter1_name if fighter1_name > fighter2_name else fighter2_name)
		winner = fighter1_name if fighter1_name > fighter2_name else fighter2_name

	print(out_string)
	return winner


def run_tournament(participants, scores):
	"""
	На каждом раунде разбивает участников на пары (первый против второго, третий против четвёртого и т.д.),
	симулирует все матчи, победители идут в следующий раунд. Выводить результаты каждого раунда. Возвращает имя чемпиона.
	Что использовать:
	while len(participants) > 1 — главный цикл турнира
	for i in range(0, len(participants), 2) — разбивка на пары
	f-строки — для красивого вывода каждого раунда
	"""
	if not validate_bracket(participants):
		return False
	while len(participants) > 1:
		print(len(participants))
		winners = []
		for i in range(0, len(participants), 2):
			fighter_1 = participants[i]
			fighter_2 = participants[i + 1]
			winner = simulate_match(fighter_1, fighter_2, scores)
			winners.append(winner)
		participants = winners
	print(f"Чемпион: {participants[0]}")


if __name__ == '__main__':
	# simulate_match("Арагорн", "Боромир", {
	# 	"Арагорн": 90,
	# 	"Боромир": 75,
	# })
	run_tournament(
		["Арагорн", "Боромир", "Гарри", "Хоумлэндер",],
		{
			"Арагорн": 90,
			"Боромир": 75,
			"Гарри": 66,
			"Хоумлэндер": 92,
		}
	)
