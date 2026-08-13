from random import randint


def create_character(**kwargs):
	hero = dict(
		**kwargs
	)
	return hero

def gain_xp(hero, xp):
	hero['xp'] += xp
	if hero['xp'] >= hero['level'] * 1000:
		hero['level'] += 1
		hero['xp'] = 0
	return hero


def battle(hero1, hero2):
	hero1_attacks = 0
	hero1_super_attacks = 0
	hero2_attacks = 0
	hero2_super_attacks = 0
	while hero1['health'] > 0 and hero2['health'] > 0:
		# Пока у обоих игроков есть жизнь
		if randint(1, 20) > 10:
			# Если случайным образом выбран игрок 1
			hero2_attack_value = int((hero2['attack'] - hero1['defense']) * (0.1 * hero2['level']))
			hero1['health'] -= hero2_attack_value
			hero1['health'] = max(0, hero1['health'])
			hero2 = gain_xp(hero2, hero2_attack_value)
			print(f"{hero2['name']} нанес урон {hero1['name']} равный {hero2_attack_value}")
			print(f"- Жизнь {hero1['name']} равна {hero1['health']}")
			print(f"- Опыт {hero2['name']} равен {hero2['xp']}")
			print(f"- Уровень {hero2['name']} равен {hero2['level']}")
			hero2_attacks += 1
		else:
			# Если случайным образом выбран игрок 2
			hero1_attack_value = int((hero1['attack'] - hero2['defense']) * (0.1 * hero1['level']))
			hero2['health'] -= hero1_attack_value
			hero2['health'] = max(0, hero2['health'])
			hero1 = gain_xp(hero1, hero1_attack_value)
			print(f"{hero1['name']} нанес урон {hero2['name']} равный {hero1_attack_value}")
			print(f"- Жизнь {hero2['name']} равна {hero2['health']}")
			print(f"- Опыт {hero1['name']} равен {hero1['xp']}")
			print(f"- Уровень {hero1['name']} равен {hero1['level']}")
			hero1_attacks += 1
		if randint(1, 100) < 10:
			# Если случайным образом выбран супер-удар
			if randint(1, 100) < 50:
				# И его делает игрок 1
				hero2_attack_value = int((hero2['super_attack'] - hero1['defense']) * (0.2 * hero2['level']))
				hero1['health'] -= hero2_attack_value
				hero1['health'] = max(0, hero1['health'])
				hero2 = gain_xp(hero2, hero2_attack_value * 2)
				print(f"{hero2['name']} нанес супер-урон {hero1['name']} равный {hero2_attack_value}")
				print(f"- Жизнь {hero1['name']} равна {hero1['health']}")
				print(f"- Опыт {hero2['name']} равен {hero2['xp']}")
				print(f"- Уровень {hero2['name']} равен {hero2['level']}")
				hero2_super_attacks += 1
			else:
				# И его делает игрок 2
				hero1_attack_value = int((hero1['super_attack'] - hero2['defense']) * (0.2 * hero1['level']))
				hero2['health'] -= hero1_attack_value
				hero2['health'] = max(0, hero2['health'])
				hero1 = gain_xp(hero1, hero1_attack_value * 2)
				print(f"{hero1['name']} нанес супер-урон {hero2['name']} равный {hero1_attack_value}")
				print(f"- Жизнь {hero2['name']} равна {hero2['health']}")
				print(f"- Опыт {hero1['name']} равен {hero1['xp']}")
				print(f"- Уровень {hero1['name']} равен {hero1['level']}")
				hero1_super_attacks += 1
	# Результаты
	print("{}: Attacks {}, Super attacks {}".format(hero1['name'], hero1_attacks, hero1_super_attacks))
	print("Hero2: Attacks {}, Super attacks {}".format(hero2['name'], hero2_attacks, hero2_super_attacks))
	print(f"Победил ", hero1['name'] if hero1['health'] > hero2['health'] else hero2['name'])


if __name__ == '__main__':
	roster = dict()
	roster.update({"Nori": create_character(
		name="Nori",
		health=3900,
		attack=2000,
		super_attack=3500,
		defense=1500,
		level=1,
		xp=0,
	)})
	roster.update({"Sirius": create_character(
		name="Sirius",
		health=3500,
		attack=2200,
		super_attack=4000,
		defense=1000,
		level=1,
		xp=0,
	)})
	print(roster)
	battle(roster.get("Nori"), roster.get("Sirius"))
