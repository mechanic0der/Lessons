russian_alpha = "абвгдежзийклмнопрстуфхцчшщъыьэюя"


def encode_caesar(text: str, shift: int):
	return ''.join([
		russian_alpha[(russian_alpha.index(char) + shift) % len(russian_alpha)]
		if char in russian_alpha else char
		for char in text.lower()
	])

def decode_caesar(text: str, shift: int):
	return ''.join([
		russian_alpha[(russian_alpha.index(char) - shift) % len(russian_alpha)]
		if char in russian_alpha else char
		for char in text.lower()
	])


def crack_caesar(ciphertext):
	for i in range(32):
		decoded_text = decode_caesar(ciphertext, i).lower()
		print(f"Shift {i}: {decoded_text}: O count: {decoded_text.count('о')}")


if __name__ == '__main__':
	text = 'Питон это круто'
	encoded_text = encode_caesar(text, 2)
	print(encoded_text)
	# decoded_text = decode_caesar(encoded_text, 2)
	# print(decoded_text)
	crack_caesar(encoded_text)
