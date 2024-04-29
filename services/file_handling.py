import os
import sys

BOOK_PATH = "book/book.txt"
PAGE_SIZE = 1050

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

text = 'Раз. Два. Три. Четыре. Пять. Прием!'
print(*_get_part_text(text, 5, 9), sep='\n')

# Функция, формирующая словарь книги
def prepare_book(path: str) -> None:
    pass

# Вызов функции prepare_book для подготовки книги из текстового файла
prepare_book(os.path.join(sys.path[0], os.path.normpath(BOOK_PATH)))