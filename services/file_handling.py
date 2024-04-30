import os
import sys

BOOK_PATH = "book/book.txt"
PAGE_SIZE = 100

book: dict[int, str] = {}


# Функция, возвращающая строку с текстом страницы и ее размер
def _get_part_text(text: str, start: int, size: int) -> tuple[str, int]:
    crop_text = text[start:size + start]  # обрезаем текст до нужного момента
    len_crop_text = len(crop_text)
    index = len_crop_text
    separators = [",", ".", "!", ":", ";", "?"]
    for i in range(len_crop_text - 1, -1, -1):
        if ((i == 0 or crop_text[i-1] not in separators)
                and (crop_text[i] in separators)
                and (i == len_crop_text - 1 or crop_text[i+1] not in separators)):
            index = i+1
            break
    part = crop_text[:index]
    return (part, len(part))

# Функция, формирующая словарь книги
def prepare_book(path: str) -> None:
    with open(path, 'rt', encoding='utf-8') as f:
        text: str = f.read().strip()
        len_text = len(text)
        start = 0
        index = 1
        while len_text > 0:
            part = _get_part_text(text, start, PAGE_SIZE)
            book[index] = part[0].lstrip()
            index += 1
            start += part[1]
            len_text -= part[1]

# Вызов функции prepare_book для подготовки книги из текстового файла
prepare_book(os.path.join(sys.path[1], os.path.normpath(BOOK_PATH)))

for i, txt in book.items():
    print(i, txt)