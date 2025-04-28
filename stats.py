import numpy as np
import matplotlib.pyplot as plt
from book import Book

class Stats:
    def __init__(self, bookshelf):
        self.bookshelf = bookshelf

    def read_by_year(self):
        pass

    def read_by_month(self, year):
        pass

    def top_ten(self):
        #SOURCE: W3 Schools Python Sorted() Function https://www.w3schools.com/python/ref_func_sorted.asp
        top_ten = sorted(self.bookshelf.books_read, reverse=True)[:10]
        index = 1
        for book in top_ten:
            print(f"{i}. {book.to_short_string()})

    def top_genres(self):
        pass

    def pages_by_year(self):
        pass

    def pages_by_month(self, year):
        pass

    def all_books(self):
        pass

    def interface(self):
        pass