"""File for the Communication class that communicates with the API and creates book classes

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

import json
import requests as rq
from collections import namedtuple
from book import Book

# CODE LOOSELY SOURCED FROM:
# Working with APIs in Python - Code in 10 Minutes by VideoLab on Youtube
# Working with JSON - https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Scripting/JSON
# Requests Documentation - https://requests.readthedocs.io/en/latest/user/quickstart/

class Comms:
    """
    This class handles the communication with the OpenLibrary API, parses JSON results and creates book classes.

    Attributes:
        bookshelfn(Bookshelf): The bookshelf object that holds information about the books

    Methods:
        make_book(title, author, isbn, pages, year_published, in_lists): Makes a book instance.
        search_books_by_title(title): Searches books by title in the API.
    """
    def __init__(self, bookshelf):
        self.bookshelf = bookshelf

    def make_book(self, title: str, author: str, isbn: int, pages: int, year_published: int, in_lists: list):
        """
        Makes a book instance.
        :param title: str: The title of the book
        :param author: str: The author of the book
        :param isbn: int: The ISBN of the book
        :param pages: int: The number of pages of the book. (Set by User)
        :param year_published: int: The year the book was published.
        :return: Instance of the book class.
        """
        book = Book(title, author, isbn, pages, year_published)
        return book

    def search_books_by_title(self, title):
        """
        Takes user input and searches the OpenLibrary Search API. Results from the API are returned as a JSON file and
        are parsed into a namedtuple. The user is asked if this book is their choice, if yes the tuple is used to
        pass parameters into the make_book function. If no, the next tuple is created.
        :param title: str: The title of the book
        :return: Book class instance
        """
        print("Searching Open Library for a book title...")
        print("To exit search results type 'Exit'")
        base_url = "https://openlibrary.org/search.json"
        params = {'title': title}

        try:
            response = rq.get(base_url, params=params)
            response.raise_for_status() # Raise an exception for HTTP errors
        except rq.exceptions.RequestException as e:
            print(f"Network error occurred: {e}")
            return None

        docs = response.json().get('docs', [])
        if not docs:
            return None

        Results = namedtuple('Results', ['author', 'title', 'Year_Published', 'isbn', 'pages'])

        run = True
        while run is True:
            for doc in response.json()['docs']:
                book = Results(
                    author=doc.get('author_name', ['unknown author'])[0], title = doc.get('title', 'unknown title'), \
                    Year_Published = doc.get('first_publish_year', 'Unknown'), isbn = doc.get('cover_i', 'Unknown ISBN'), \
                    pages = doc.get('number_of_pages', 0))
                check = input(f"Is {book.title} by {book.author} Published {book.Year_Published} ISBN: {book.isbn} your book? Y or N: ")
                title, author, isbn, pages, year_published = book.title, book.author, book.isbn, book.pages, \
                book.Year_Published
                _in_lists = []
                if check.lower() == 'y':
                    instance = self.make_book(title, author, isbn, pages, year_published, _in_lists)
                    print("")
                    return instance
                if check.lower() == 'exit':
                    print("Exiting...")
                    return
