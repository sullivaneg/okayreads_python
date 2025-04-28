import numpy as np
import matplotlib.pyplot as plt
from book import Book
from bookshelf import Bookshelf
from collections import defaultdict
from datetime import datetime

class Stats:
    def __init__(self, bookshelf):
        self.bookshelf = bookshelf

    def read_by_year(self):
        books_per_year = defaultdict(int)

        for book in self.bookshelf.books_read:
            year = book.date_read.year
            books_per_year[year] += 1

        # Prepare for matplotlib
        years = sorted(books_per_year.keys())
        books = [books_per_year[year] for year in years]

        # Matplotlib
        # SOURCE: https://matplotlib.org/stable/plot_types/basic/plot.html#sphx-glr-plot-types-basic-plot-py
        plt.style.use('_mpl-gallery')

        # make data
        x = years
        y = books

        # plot
        fig, ax = plt.subplots()

        ax.plot(x, y, linewidth=2.0)

        ax.set(xlim=(0, 200), xticks=np.arange(1, 200),
               ylim=(0, 200), yticks=np.arange(1, 200))

        plt.show()

    def read_by_month(self, year):
        books_per_month = defaultdict(int)

        for book in self.bookshelf.books_read:
            book_year = book.date_read.year
            if book_year == year:
                month = book.date_read.month
                books_per_month[month] += 1

        # Prepare for matplotlib
        months = sorted(pages_per_month.keys())
        pages = [pages_per_month[year] for month in months]

        # Matplotlib
        # SOURCE: https://matplotlib.org/stable/plot_types/basic/plot.html#sphx-glr-plot-types-basic-plot-py
        plt.style.use('_mpl-gallery')

        # make data
        x = months
        y = pages

        # plot
        fig, ax = plt.subplots()

        ax.plot(x, y, linewidth=2.0)

        ax.set(xlim=(0, 200), xticks=np.arange(1, 200),
               ylim=(0, 200), yticks=np.arange(1, 200))

        plt.show()

    def all_books(self):
        for book in self.bookshelf.books_read:
            print(book.to_short_string())

    def total_pages(self, read_list):
        pages = 0
        for item in read_list:
            pages += item.pages
        return pages

    def top_ten(self):
        #SOURCE: W3 Schools Python Sorted() Function https://www.w3schools.com/python/ref_func_sorted.asp
        top_ten = sorted(self.bookshelf.books_read, reverse=True)[:10]
        index = 1
        for book in top_ten:
            print(f"{i}. {book.to_short_string()}")

    def pages_by_year(self):
        pages_per_year = defaultdict(int)

        for book in self.bookshelf.books_read:
            year = book.date_read.year
            pages_per_year[year] += book.pages

        #Prepare for matplotlib
        years = sorted(pages_per_year.keys())
        pages = [pages_per_year[year] for year in years]

        #Matplotlib
        #SOURCE: https://matplotlib.org/stable/plot_types/basic/plot.html#sphx-glr-plot-types-basic-plot-py
        plt.style.use('_mpl-gallery')

        # make data
        x = years
        y = pages

        # plot
        fig, ax = plt.subplots()

        ax.plot(x, y, linewidth=2.0)


        ax.set(xlim=(0, 200), xticks=np.arange(1, 200),
               ylim=(0, 200), yticks=np.arange(1, 200))

        plt.show()


    def pages_by_month(self, year):
        pages_per_month = defaultdict(int)

        for book in self.bookshelf.books_read:
            if book.date_read.year == year:
                month = book.date_read.month
                pages_per_month[month] += book.pages

        # Prepare for matplotlib
        months = sorted(pages_per_month.keys())
        pages = [pages_per_month[year] for month in months]

        # Matplotlib
        # SOURCE: https://matplotlib.org/stable/plot_types/basic/plot.html#sphx-glr-plot-types-basic-plot-py
        plt.style.use('_mpl-gallery')

        # make data
        x = months
        y = pages

        # plot
        fig, ax = plt.subplots()

        ax.plot(x, y, linewidth=2.0)

        ax.set(xlim=(0, 200), xticks=np.arange(1, 200),
               ylim=(0, 200), yticks=np.arange(1, 200))

        plt.show()

    def all_books(self):
        for book in self.bookshelf.books_read:
            print(book.to_short_string())

    def total_pages(self, read_list):
        pages = 0
        for item in read_list:
            pages += item.pages
        return pages

    def interface(self):
        while True:
            break_outer = False
            print(f"{self.bookshelf.username}'s Statistics")
            print("__________________________________________")
            total_pages = self.total_pages(self.bookshelf.books_read)
            total_books = len(self.bookshelf.books_read)
            print(f"Books Read Read: {total_books}")
            print(f"Total Pages Read: {total_pages}")
            print("")
            print("___________________________________________")
            print("1. Display all books read ")
            print("2. Display your top 10 books read")
            print("3. See Books Read by Year")
            print("4. See Books Read by Month")
            print("5. See Pages Read by Year")
            print("6. See Pages Read by Month")
            print("7. Exit")
            choice = input("Enter your choice: ")
            while True:
                if choice == "1":
                    print("ALL BOOKS READ")
                    print("___________________________________")
                    self.all_books()
                    break
                if choice == "2":
                    print("Your Top 10 Books Read")
                    print("_____________________________________")
                    self.top_ten()
                    break
                if choice == "3":
                    print("Books Read by Year")
                    print("_____________________________________")
                    self.read_by_year()
                    break
                if choice == "4":
                    print("Books Read by Month")
                    print("_____________________________________")
                    self.read_by_month()
                    break
                if choice == "5":
                    print("Pages Read by Year")
                    print("_____________________________________")
                    self.pages_by_year()
                    break
                if choice == "6":
                    print("Pages Read by Month")
                    print("_____________________________________")
                    self.read_by_month()
                    break
                if choice == "7":
                    break_outer = True
                    break

            if break_outer:
                break



