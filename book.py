"""File for the book class which stores book attributes

Author: Emma Sullivan
Class: CSI-260-01
Assignment: Final Project
Due Date: 05/02/2025 11:59 PM

Certification of Authenticity:
I certify that this is entirely my own work, except where I have given
fully-documented references to the work of others. I understand the definition
and consequences of plagiarism and acknowledge that the assessor of this
assignment may, for the purpose of assessing this assignment:
- Reproduce this assignment and provide a copy to another member of academic
- staff; and/or Communicate a copy of this assignment to a plagiarism checking
- service (which may then retain a copy of this assignment on its database for
- the purpose of future plagiarism checking)

Note: For some persistent bugs I used Perplexity AI to help me debug.
"""

# Original Code from CSI-260-01 Library Project
# Group: Abigail Gehlbach, Charles Justus, Emma Sullivan, Sebastian Dominguez
# Authors: Abigail Gehlbach, Charles Justus, Emma Sullivan

class Book:
    """
    This class represents a book object that the user can add to different lists and interact with.

    Attributes:
        title (str): The title of the book.
        author (str): The author of the book.
        isbn (str): The ISBN of the book.
        pages (int): The number of pages of the book. Default
    """
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

    # --END CODE FROM CSI-260-01 LIBRARY PROJECT--

    def __repr__(self):
        return "Book({}{}{}{}{}{}{})".format(self.title, self.author, self.isbn, self.pages, self.genre, self.year_published, self._in_lists)

    def __gt__(self, other):
        return self._rating > other._rating

    def __lt__(self, other):
        return self._rating < other._rating

    def __eq__(self, other):
        return self.rating == other._rating

    def to_short_string(self):
        if "books_read" in self._in_lists:
            return f'{self.title} by {self.author} - (ISBN: {self.isbn}) | READ: {self.date_read} | RATING: {self._rating}'
        if "want_to_read" in self._in_lists:
            return f'{self.title} by {self.author} - (ISBN: {self.isbn})'

    def profile_string(self):
        print(f"____________{self.title}________________")
        print(f'{self.title} by {self.author}, {self.pages} pages')
        print(f'Genre: {self.genre}')
        print(f'Published: {self.year_published}, ISBN: {self.isbn}')
        lists = self.in_lists
        rating = self._rating
        print(f'In lists: {lists}')
        print(f'Rating: {rating}/10')
        print("___________________________________________")

    @property
    def rating(self):
        return self._rating

    @rating.setter
    def rating(self, value):
        self._rating = float(value)

    @property
    def date_read(self):
        return self._date_read

    @date_read.setter
    def date_read(self, value):
        self._date_read = value

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
