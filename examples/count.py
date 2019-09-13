from pathlib import Path


def count_e(path_to_book):
    text = path_to_book.read_text()

    counter = 0

    for letter in text:
        if letter == 'e':
            counter += 1

    return counter


if __name__ == "__main__":
    books_dir = Path.cwd() / 'books'
    print(count_e(books_dir / 'frankenstein.txt'))
