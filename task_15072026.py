def science():
	"""Валидатор научных формул, задание от 15.07.2026
	В научных формулах скобки должны быть сбалансированы, а некоторые конструкции запрещены. Написать валидатор.
	Написать функцию balanced_brackets(formula) — проверяет что все открывающие скобки (, [, { закрыты в правильном порядке.
	Использовать стек (список с append и pop). Возвращает (bool, str) — результат и описание ошибки если есть.
	Написать функцию tokenize(formula) — разбивает формулу на токены: числа, операторы + - * / ^, скобки,
	названия переменных (последовательности букв). Пробелы игнорировать. Возвращает список токенов.
	Написать функцию validate_formula(formula) — комплексная проверка: сбалансированность скобок,
	не идут ли два оператора подряд, не начинается ли и не заканчивается ли формула оператором * / ^.
	Возвращает список всех найденных ошибок.
	Что использовать:
	• Список как стек: append() для push, pop() для pop
	• Словарь пар скобок: {")": "(", "]": "[", "}": "{"}
	• for по строке — для токенизации
	• .isdigit() и .isalpha() — для определения типа символа
	Пример работы:
		balanced_brackets("(a + [b * c])")   → (True, "")
		balanced_brackets("(a + [b * c)")    → (False, "Ожидалась ], найдена )")
		balanced_brackets("a + b)")          → (False, "Лишняя закрывающая скобка")

	tokenize("kjshrbgslejrbg2342*2 + (b^3)")  → ["a", "*", "2", "+", "(", "b", "^", "3", ")"]

	validate_formula("a * + b")  → ["Два оператора подряд: * и +"]
	validate_formula("*a + b")   → ["Формула начинается с оператора *"]
	"""


def balanced_brackets(formula):
	""" Пример формулы: (a + b) * (c * [r + g + d - {5-3]}) """
	bracket_dict = {
		")": "(",
		"}": "{",
		"]": "[",
	}
	opened_brackets = list()
	for char in formula:
		if char in "([{":
			opened_brackets.append(char)
		if char in ")]}":
			if bracket_dict[char] == opened_brackets[-1]:
				opened_brackets.pop()
	return len(opened_brackets) == 0, "описание ошибки"


def tokenize(formula):
	tokens_list = list()
	formula = formula.replace(" ", "")
	variable_index = -1
	for i, char in enumerate(formula):
		# kjshrbgslejrbg2342*2 + (b^3)")  → ["a", "*", "2", "+", "(", "b", "^", "3", ")
		if char in "(){}[]*^+-/":
			if variable_index > -1:
				tokens_list.append(formula[variable_index:i])
				variable_index = -1
			tokens_list.append(char)
		elif variable_index == -1:
			variable_index = i
	print(tokens_list)


def validate_formula(formula):
	brackets_is_balanced = balanced_brackets(formula)
	formula = formula.replace(" ", "")
	double_operators = False
	prev_char = False
	for char in formula:
		if char in "+-*/^":
			if prev_char:
				double_operators = True
				print(char)
			prev_char = True
		else:
			prev_char = False
	start_and_end_operators = "*/^"
	start_and_end = any([
		formula.startswith(_op) or formula.endswith(_op)
		for _op in start_and_end_operators
	])
	print(brackets_is_balanced)
	print(not double_operators)
	print(not start_and_end)
	print("Status:", brackets_is_balanced and not double_operators and not start_and_end)


if __name__ == '__main__':
	# balanced_brackets("(a + b) * (c * [r + g] + d - {5-3})")
	validate_formula("kjshrbgslejrbg2342*2 + (b234^2342343)")
