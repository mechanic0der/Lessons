"""Написать функцию is_valid_callsign(callsign), которая проверяет позывной агента по правилам:
Длина от 4 до 12 символов
Содержит хотя бы одну цифру
Содержит хотя бы одну букву в верхнем регистре
Не содержит пробелов
Не начинается и не заканчивается цифрой
Функция возвращает кортеж (bool, str) — прошёл ли позывной проверку и причина отказа если не прошёл (Если их несколько, то все причины). Если прошёл — причина пустая строка.
Что использовать:
Методы строк: .isupper(), .isdigit(), .isspace() на отдельных символах
for по строке — для проверки символов
Индексы [0] и [-1] — первый и последний символ
len() — длина
Пример работы:
is_valid_callsign("WOLF7")        → (True, "")
is_valid_callsign("wolf7")        → (False, "Нет заглавной буквы")
is_valid_callsign("W7")           → (False, "Слишком короткий")
is_valid_callsign("7WOLF")        → (False, "Начинается с цифры")
is_valid_callsign("WOLFPACK")     → (False, "Нет цифры")
is_valid_callsign("WO LF7")       → (False, "Содержит пробел")
"""

def is_valid_callsign(callsign: str):
	errors = []
	passed = True
	if len(callsign) not in range(4, 13):
		errors.append("Длина должна быть от 4 до 12 символов")
		passed = False
	if not any(c.isdigit() for c in callsign):
		errors.append("Должна быть хотя бы одна цифра")
		passed = False
	if not any(c.isupper() for c in callsign):
		errors.append("Должна быть хотя бы одна заглавная буква")
		passed = False
	if ' ' in callsign:
		errors.append("Не должно быть пробелов")
		passed = False
	if callsign[0].isdigit():
		errors.append("Первый символ не должен быть цифрой")
		passed = False
	if callsign[-1].isdigit():
		errors.append("Последний символ не должен быть цифрой")
		passed = False
	print(passed, ', '.join(errors))


if __name__ == "__main__":
	is_valid_callsign("WOLF7")
	is_valid_callsign("wolf7")
	is_valid_callsign("W7")
	is_valid_callsign("7WOLF")
	is_valid_callsign("WOLFPACK")
	is_valid_callsign("WO LF7")
	is_valid_callsign("WOL3F")