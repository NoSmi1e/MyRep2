class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def get_info(self):
        return f'{self.title} — {self.author}'


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def find_by_author(self, author):
        titles = []
        for book in self.books:
            if book.author.lower() == author.lower():
                titles.append(book.title)
        return titles
