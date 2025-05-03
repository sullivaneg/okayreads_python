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
        pages (int): The number of pages of the book. User input.
        year_published (str): The year the book was first published.
        _in_lists(list): A list of all the book lists the book is in. Private to the class, set by the setter.

    Methods:
        match(filter_text): Checks if the filter text matches a book object.
        __str__(): Returns the string representation of the book object.
        __repr__(): Returns the string representation of what the book object looks like.
        __gt__(), __lt__(), __eq__(), __ne__(): Represents greater than, less than, equal and not equal respectively.
        to_short_string(): Returns a short string representation of the book object.
        profile_string(): Long form version of the book object for an internal search result.

    Getters/Setters:
        rating, date_read, in_lists
    """
    def __init__(self, title: str, author: str, isbn: int, pages: int, year_published: int = None, _in_lists: list = None):
        """
        Initialize the book object.
        """
        self.title = title
        self.author = author
        self.isbn = isbn
        self.pages = pages
        self.year_published = year_published if year_published is not None else 'Unknown year published'
        self._in_lists = _in_lists if _in_lists is not None else []
        self._rating =None

    def match(self, filter_text: str):
        """
        Checks if the filter text matches a book object.
        :param filter_text: User input of book title in the interface.
        :return: Bool
        """
        return filter_text.lower() in self.title.lower() or filter_text.lower() == self.isbn  or \
             filter_text.lower() in self.author.lower() or filter_text == self.pages

    def __str__(self):
        """
        Returns the string representation of the book object.
        """
        return f'{self.title} by {self.author}, {self.pages} pages, published in {self.year_published}(ISBN: {self.isbn})'

    # --END CODE FROM CSI-260-01 LIBRARY PROJECT--

    def __repr__(self):
        """
        Returns the string representation of the book object for debugging.
        """
        return "Book({}{}{}{}{}{})".format(self.title, self.author, self.isbn, self.pages, self.year_published, self._in_lists)

    def __gt__(self, other):
        """
        Defines greater than based on book rating.
        :param other: Other Book object
        :return: Bool
        """
        return self._rating > other._rating

    def __lt__(self, other):
        """
        Defines less than based on book rating.
        :param other: Other Book object
        :return: Bool
        """
        return self._rating < other._rating

    def __eq__(self, other):
        """
        Defines equal based on book rating.
        :param other: Other Book object
        :return: Bool
        """
        return self.rating == other._rating

    def __ne__(self, other):
        """
        Defines not equal based on book rating.
        :param other: Other Book object
        :return: Bool
        """
        return self.rating != other._rating

    def to_short_string(self):
        """
        Returns a short string representation of the book object.
        :return: str
        """
        if "books_read" in self._in_lists:
            return f'{self.title} by {self.author} - (ISBN: {self.isbn}) | READ: {self.date_read} | RATING: {self._rating}'
        if "want_to_read" in self._in_lists:
            return f'{self.title} by {self.author} - (ISBN: {self.isbn})'

    def profile_string(self):
        """
        Returns a long string representation of the book object for search result/book profile purposes.
        :return: str
        """
        print(f"____________{self.title}________________")
        print(f'{self.title} by {self.author}, {self.pages} pages')
        print(f'Published: {self.year_published}, ISBN: {self.isbn}')
        lists = self.in_lists
        rating = self._rating
        print(f'In lists: {lists}')
        print(f'Rating: {rating}/10')
        print("___________________________________________")

    @property
    def rating(self):
        """
        Returns the rating of the book object.
        :return: float
        """
        return self._rating

    @rating.setter
    def rating(self, value):
        """
        Sets the rating of the book object.
        :param value: str
        """
        self._rating = float(value)

    @property
    def date_read(self):
        """
        Returns the date read of the book object.
        :return: str
        """
        return self._date_read

    @date_read.setter
    def date_read(self, value):
        """
        Sets the date read of the book object.
        :param value: str
        """
        self._date_read = value

    @property
    def in_lists(self):
        """
        Returns the list of book lists the book is in.
        :return: list
        """
        return self._in_lists

    @in_lists.setter
    def in_lists(self, value, value2 = None, value3 = None):
        """
        Sets the list of book lists the book is in.
        :param value: str name of a list
        :param value2: optional second name of a list
        :param value3: optional third name of a list
        :return:
        """
        self._in_lists.append(value)
        if value2 is not None:
            self._in_lists.append(value2)
        if value3 is not None:
            self._in_lists.append(value3)
