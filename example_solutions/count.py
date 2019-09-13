from pathlib import Path

import htmap


def count(path_to_book):
    text = path_to_book.read_text()

    counter = 0

    for letter in text:
        if letter == 'e':
            counter += 1

    return counter


if __name__ == "__main__":
    books_dir = htmap.TransferPath.cwd() / 'books'

    book_paths = list(books_dir.iterdir())

    m = htmap.map(count, book_paths, tag = 'counts')

    print(m.tag)
