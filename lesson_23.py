
def is_valid_dna(user_string: str) -> bool:
	return all([c in 'ACGT' for c in user_string.upper()])


def gc_content(user_string: str) -> float:
	# print(user_string.count('G'))
	# print(user_string.count('C'))
	# print(len(user_string))
	percent = (user_string.count('G') + user_string.count('C')) / len(user_string)
	return percent * 100.0

def find_motif(user_string: str, motif: str):
	indexes = []
	for index , letter in enumerate(user_string):
		part = user_string[index:index + len(motif)]
		if part == motif:
			indexes.append(index)
	return indexes


if __name__ == "__main__":
	current_str = "ATGCATGCGG"
	print(is_valid_dna(current_str))
	print(gc_content(current_str))
	print(find_motif(current_str, "ATC"))
