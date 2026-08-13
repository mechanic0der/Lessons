"""
Дефектор кода самоуничтожения
Система безопасности проверяет коды доступа. Написать набор алгоритмических функций.
Написать функцию is_armstrong(n) — число Армстронга: сумма цифр каждая в степени количества цифр равна самому числу. Например 153 = 1³ + 5³ + 3³. Возвращает bool.
Написать функцию digit_root(n) — цифровой корень: складывать цифры числа пока не останется одна цифра. Например 9875 → 9+8+7+5=29 → 2+9=11 → 1+1=2. Возвращает итоговую цифру.
Написать функцию encode_number(n, key) — кодирует число: каждую цифру заменить на (цифра + key) % 10. Возвращает новое число.
Написать функцию decode_sequence(codes) — принимает список закодированных чисел, находит среди них все числа Армстронга после декодирования (перебрать все ключи от 0 до 9), возвращает список (оригинальный_код, ключ, декодированное_число) для найденных совпадений.
Пример работы:
is_armstrong(153)   → True
is_armstrong(370)   → True
is_armstrong(100)   → False

digit_root(9875)    → 2

encode_number(153, 3)   → 486  # 1+3=4, 5+3=8, 3+3=6

decode_sequence([486, 703, 963])
→ [(486, 3, 153), (703, 7, 370)]  # Armstrong numbers found
"""
# def is_armstrong(number: int = 153):
# Более долгий способ
# 	arm_sum = 0
# 	p = len(str(number))
# 	for i in str(number):
# 		arm_sum += int(i) ** p
# 	return arm_sum == number


def is_armstrong(number: int = 153):
	arm_sum = 0
	p = len(str(number))
	while_number = number
	while while_number > 0:
		arm_sum += (while_number % 10) ** p
		while_number //= 10
	return arm_sum == number

def digit_root(number: int = 9875):
	# Например 9875 → 9+8+7+5=29 → 2+9=11 → 1+1=2. Возвращает итоговую цифру.
	while_number = number
	while len(str(while_number)) > 1:
		result = 0
		while while_number > 0:
			result += while_number % 10
			while_number //= 10
		while_number = result
	return while_number


# Написать функцию encode_number(n, key) — кодирует число: каждую цифру заменить на (цифра + key) % 10. Возвращает новое число.
def encode_number(n, key):
	# encode_number(153, 3)   → 486  # 1+3=4, 5+3=8, 3+3=6
	line = []
	while n > 0:
		line.append((n + key) % 10)
		n //= 10
	return int(''.join(map(str, line[::-1])))


# Написать функцию decode_sequence(codes) — принимает список закодированных чисел,
# после декодирования (перебрать все ключи от 0 до 9) находит среди них все числа Армстронга,
# возвращает список (оригинальный_код, ключ, декодированное_число) для найденных совпадений.
def decode_sequence(codes: list):
	results = list()
	# decode_sequence([486, 703, 963]) → [(486, 3, 153), (703, 7, 370)]  # Armstrong numbers found
	for code in codes:
		for key in range(10):
			line = []
			code_number = code
			while code_number > 0:
				line.append((code_number - key) % 10)
				code_number //= 10
			decoded_number = int(''.join(map(str, line[::-1])))
			if is_armstrong(decoded_number):
				results.append((code, key, decoded_number))
	print(results)



if __name__ == '__main__':
	decode_sequence([486, 703, 963])
