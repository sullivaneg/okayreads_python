
#     def to_short_string(self):
#         return f'Book: {self.name} - {self.author} - (ISBN: {self.isbn})'

class Book:
    def __init__(self, title: str, author: str, isbn: int, pages: int, genre: str, year_published: int):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.pages = pages
        self.genre = genre
        self.year_published = year_published

    def match(self, filter_text: str):
        return filter_text.lower() in self.title.lower() or filter_text.lower() == self.isbn or \
            (any(filter_text.lower() in str(g).lower() for g in self.genre) or \
             filter_text.lower() in self.author.lower() or filter_text == self.pages)

    def __str__(self):
        return f'{self.title} by {self.author}, {self.pages} pages, (ISBN: {self.isbn})'

    def __repr__(self):
        return "Book({}, {}, {}, {}, {})".format(self.title, self.author, self.pages, self.isbn, self.genre)

    @property
    def rating(self):
        return self.rating

    @rating.setter
    def rating(self, value):
        self.rating = float(value)

    @property
    def date_read(self):
        return self.date_read

    @date_read.setter
    def date_read(self, value):
