# Communicates with the API and creates book classes
import json
import requests as rq
from collections import namedtuple
from book import Book

# Sources: Working with APIs in Python - Code in 10 Minutes by VideoLab on Youtube
# Working with JSON - https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Scripting/JSON
# Requests Documentation - https://requests.readthedocs.io/en/latest/user/quickstart/

class Comms:
    def __init__(self, bookshelf):
        self.bookshelf = bookshelf

    def make_book(self, title: str, author: str, isbn: int, pages: int, genre: str, year_published: int, in_lists: list):
        book = Book(title, author, isbn, pages, genre, year_published)
        return book

    def search_books_by_title(self, title):
        """
        Searches Open Library for a book title and returns the JSON response. Also displays search results.
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

        Results = namedtuple('Results', ['author', 'title', 'Year_Published', 'isbn', 'pages', 'genre'])

        run = True
        while run is True:
            for doc in response.json()['docs']:
                book = Results(
                    author=doc.get('author_name', ['unknown author'])[0], title = doc.get('title', 'unknown title'), \
                    Year_Published = doc.get('first_publish_year', 'Unknown'), isbn = doc.get('cover_i', 'Unknown ISBN'), \
                    pages = doc.get('number_of_pages', 0), genre = doc.get('subject', 'unknown genre'))
                check = input(f"Is {book.title} by {book.author} Published {book.Year_Published} ISBN: {book.isbn} your book? Y or N: ")
                title, author, isbn, pages, genre, year_published = book.title, book.author, book.isbn, book.pages, \
                    book.genre, book.Year_Published
                _in_lists = []
                if check.lower() == 'y':
                    instance = self.make_book(title, author, isbn, pages, genre, year_published, _in_lists)
                    print("")
                    return instance
                if check.lower() == 'exit':
                    print("Exiting...")
                    return
