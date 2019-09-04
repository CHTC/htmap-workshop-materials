import string

import htmap


# note!
# outside of a tutorial, you should be using a collections.Counter
# https://docs.python.org/3/library/collections.html
# which does all of this without nearly as much code :)

@htmap.mapped
def count_letters(path_to_book):
    text = path_to_book.read_text()

    counter = dict()

    for letter in text:
        if letter in string.ascii_letters:
            if letter not in counter:
                counter[letter] = 0
            counter[letter] += 1

    return counter


if __name__ == "__main__":
    # counter = count_letters(Path('books/dracula.txt'))

    # for letter, count in sorted(counter.items()):
    #     print(letter, count)

    book_paths = list(htmap.TransferPath('books').iterdir())
    # for path in book_paths:
    #     print(type(path), path)

    counters = count_letters.map(book_paths)
    counters.wait(show_progress_bar = True)

    totals = {letter: 0 for letter in string.ascii_letters}
    for counter in counters:
        for letter in string.ascii_letters:
            totals[letter] += counter.get(letter, 0)

    for letter, count in sorted(totals.items(), key = lambda lc: lc[1], reverse = True):
        print(letter, count)
