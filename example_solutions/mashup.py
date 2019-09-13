import random
import textwrap
import itertools
from pathlib import Path

import htmap


def mashup(first_book, second_book):
    first_text = first_book.read_text()
    second_text = second_book.read_text()

    first_words = first_text.split()
    second_words = second_text.split()

    words = []
    for first_word, second_word in zip(first_words, second_words):
        words.append(random.choice((first_word, second_word)))

    text = ' '.join(words)
    wrapped = textwrap.wrap(text)[100:-500]
    final = '\n'.join(wrapped)

    return final


if __name__ == "__main__":
    books_dir = htmap.TransferPath.cwd() / 'books'
    book_paths = list(books_dir.iterdir())

    with htmap.build_map(mashup, tag = 'mashups') as builder:
        for first_book, second_book in itertools.combinations(book_paths, r = 2):
            builder(first_book, second_book)

    m = builder.map
    print(m.tag)
