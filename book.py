class Book:
    def __init__(self, title: str, author: str, isbn: int, pages: int, genre: str = '', year_published: int = None, _in_lists: list = None):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.pages = pages
        self.genre = genre if genre is not None else 'Unknown Genre'
        self.year_published = year_published if year_published is not None else 'Unknown year published'
        self._in_lists = _in_lists if _in_lists is not None else []
        self._rating =None

    def match(self, filter_text: str):
        return filter_text.lower() in self.title.lower() or filter_text.lower() == self.isbn  or \
             filter_text.lower() in self.author.lower() or filter_text == self.pages

    def __str__(self):
        return f'{self.title} by {self.author}, {self.pages} pages, published in {self.year_published}(ISBN: {self.isbn})'

    def __repr__(self):
        return "Book({}{}{}{}{}{}{})".format(self.title, self.author, self.isbn, self.pages, self.genre, self.year_published, self._in_lists)

    def __gt__(self, other):
        return self.rating > other.rating

    def __lt__(self, other):
        return self.rating < other.rating

    def __eq__(self, other):
        return self.rating == other.rating

    def to_short_string(self):
        if "books_read" in self._in_lists:
            return f'Book: {self.title} by {self.author} - (ISBN: {self.isbn}) | READ: {self.date_read}'
        if "want_to_read" in self._in_lists:
            return f'Book: {self.title} by {self.author} - (ISBN: {self.isbn})'

    def profile_string(self):
        print(f'{self.title} by {self.author}, {self.pages} pages')
        print(f'Genre: {self.genre}')
        print(f'Published: {self.year_published}, ISBN: {self.isbn}')
        lists = self.in_lists
        print(f'In lists: {lists}')

    @property
    def rating(self):
        return self._rating

    @rating.setter
    def rating(self, value):
        self._rating = float(value)

    @property
    def date_read(self):
        return self.date_read

    @date_read.setter
    def date_read(self, value):
        self.date_read = value

    @property
    def in_lists(self):
        return self._in_lists

    @in_lists.setter
    def in_lists(self, value, value2 = None, value3 = None):
        self._in_lists.append(value)
        if value2 is not None:
            self._in_lists.append(value2)
        if value3 is not None:
            self._in_lists.append(value3)
