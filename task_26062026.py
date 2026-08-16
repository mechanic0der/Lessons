"""
Анализ ДНК
Написать набор функций для анализа строки ДНК — последовательности из букв A, T, G, C.
Написать четыре функции:
is_valid_dna(sequence) — проверяет что строка содержит только символы A, T, G, C (в любом регистре). Возвращает bool.
gc_content(sequence) — возвращает процент G и C в последовательности, округлённый до 2 знаков.
find_motif(sequence, motif) — возвращает список всех позиций (индексов) с которых начинается подстрока motif внутри sequence. Если не найдена — пустой список.
Что использовать:
Множество {"A", "T", "G", "C"} — для проверки валидности
len() и счётчик — для GC-контента
for i in range(len(...)) и срез [i:i+len(motif)] — для поиска мотива
Пример работы:
seq = "ATGCATGCGG"

is_valid_dna(seq)          → True
is_valid_dna("ATGX")       → False
gc_content(seq)            → 50.0
find_motif(seq, "ATG")     → [0, 4]
find_motif(seq, "TTT")     → []
"""


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

if __name__ == '__main__':
    seq = "ATGCATGCGG"
    is_valid_dna(seq)
    is_valid_dna("ATGX")
    gc_content(seq)
    find_motif(seq, "ATG")
    find_motif(seq, "TTT")