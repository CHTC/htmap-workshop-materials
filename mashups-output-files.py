import itertools
from pathlib import Path
import random
import textwrap

import htmap


@htmap.mapped
def mashup(first_book, second_book):
    first_text = first_book.read_text()
    second_text = second_book.read_text()

    first_words = first_text.split()
    second_words = second_text.split()

    words = []
    for first_word, second_word in zip(first_words, second_words):
        words.append(random.choice((first_word, second_word)))

    text = ' '.join(words)
    wrapped = textwrap.wrap(text)
    final = '\n'.join(wrapped)

    output_path = Path(f'{first_book.stem}+{second_book.stem}.txt')
    output_path.write_text(final)

    htmap.transfer_output_files(output_path)


if __name__ == "__main__":
    # mashed = mashup(
    #     htmap.TransferPath('books') / 'dracula.txt',
    #     htmap.TransferPath('books') / 'ulysses.txt',
    # )

    # print(mashed)

    books = list(htmap.TransferPath('books').iterdir())

    with mashup.build_map() as map_builder:
        for first, second in itertools.combinations(books, r = 2):
            map_builder(first, second)

    map = map_builder.map

    map.wait(show_progress_bar = True)

    for op in map.output_files:
        print(list(op.iterdir()))
