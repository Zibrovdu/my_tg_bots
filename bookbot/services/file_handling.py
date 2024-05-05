import os
import sys

BOOK_PATH = 'book/book.txt'
PAGE_SIZE = 1050

book: dict[int, str] = {}


def _get_part_text(text: str, start: int, page_size: int) -> tuple[str, int]:
    spec = [",", ".", ";", ":", "!", "?"]
    end = -1
    if text[start: start + page_size][end] in spec and text[start: start + page_size + 1][end] in spec:
        text = text[: start + page_size - 2]
    if text[start: start + page_size][end] in spec:
        return text[start: start + page_size], len(text[start: start + page_size])
    return _get_part_text(text, start, page_size - 1)


def prepare_book(path: str) -> None:
    i = 1
    with open(path, 'r', encoding='utf-8') as f:
        data = f.read()
        f.close()
    while len(data) > 0:
        book[i] = _get_part_text(data, 0, PAGE_SIZE)[0].lstrip()
        data = data[_get_part_text(data, 0, PAGE_SIZE)[1]:]
        i += 1


prepare_book(os.path.join(sys.path[0], os.path.normpath(BOOK_PATH)))
