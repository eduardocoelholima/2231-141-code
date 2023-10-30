from dataclasses import dataclass

@dataclass
class Book:
    title: str
    author: str
    copies: int

def load_library(filename:str) -> list:
    library = []
    with open(filename) as file:
        for line in file:
            stripped = line.strip()
            bookdata = stripped.split(',')
            title = bookdata[0]
            author = bookdata[1]
            copies = int(bookdata[2])
            newbook = Book(title, author, copies)
            library.append(newbook)
    return library

def create_author_catalog(books:list) -> dict:
    author_catalog = {}
    for book in books:
        if not(book.author in author_catalog):
            author_catalog[book.author] = []
        author_catalog[book.author].append(book)
    return author_catalog

def main():
    library = load_library('books.csv')
    # for book in library:
    #     print(book)
    books_by_author = create_author_catalog(library)
    # print(books_by_author)
    for author in sorted(books_by_author.keys()):
        if len(books_by_author[author]) > 1:
            print(author)
            for book in books_by_author[author]:
                print('   ', book)
            print()

if __name__ == '__main__':
    main()
