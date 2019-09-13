import random
import textwrap
from pathlib import Path


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
    books_dir = Path.cwd() / 'books'
    print(mashup(
        books_dir / 'the-adventures-of-sherlock-holmes.txt',
        books_dir / 'ulysses.txt',
    ))
