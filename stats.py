"""File to keep track of user statistics, display graphs, and provide an interface

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

import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict
import pandas as pd
from datetime import datetime

class Stats:
    def __init__(self, bookshelf):
        self.bookshelf = bookshelf

    def create_stats_df(self):
        # Create a new DF from bookshelf
        df = self.bookshelf.create_df()

        # Filter to only read books
        df = df[df['Shelves'] == 'read']
        return df

    def read_by_year(self):
        df = self.create_stats_df()
        df['Date Read'] = pd.to_datetime(df['Date Read'])

        # Source: Perplexity AI
        # Notes: I was debugging and I took this entire line
        counts = df['Date Read'].dt.year.value_counts().sort_index()
        # --END AI--

        # Prepare for matplotlib
        years = counts.index.tolist()
        books = counts.values.tolist()

        # Matplotlib Graph
        plt.figure(figsize=(12, 10))
        plt.bar(years, books)
        plt.xticks(years, years)
        plt.xlabel("Year")
        plt.ylabel("Number of Books")
        plt.title("Books per year")
        plt.show()

    def read_by_month(self, year):
        df = self.create_stats_df()

        # Original Source: Stack Overflow
        # URL: https://stackoverflow.com/questions/46878156/pandas-filter-dataframe-rows-with-a-specific-year
        # Author: Vaishali
        # Date: October 23, 2017

        df['Date Read'] = pd.to_datetime(df['Date Read'])
        df_temp = df[df['Date Read'].dt.year == year]

        # --END STACK OVERFLOW--

        # Perplexity AI
        # I was debugging
        counts = df_temp['Date Read'].dt.month.value_counts().reindex(range(1, 13), fill_value=0)
        # -- END AI --


        #Prepping for matplotlib
        months = counts.index.tolist()
        num_books = counts.values.tolist()

        #Matplotlib Graph
        plt.figure(figsize = (12, 10))
        plt.bar(months, num_books)
        plt.xticks(months, months)
        plt.xlabel("Month")
        plt.ylabel("Number of Books")
        plt.title("Monthly Books for Year {}".format(year))
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
        # SOURCE: W3 Schools Python Sorted() Function
        # URL: https://www.w3schools.com/python/ref_func_sorted.asp
        top_ten = sorted(self.bookshelf.books_read, reverse=True)[:10]
        index = 1
        for book in top_ten:
            print(f"{index}. {book.to_short_string()}")
            index += 1

    def pages_by_year(self):
        pages_per_year = defaultdict(int)

        for book in self.bookshelf.books_read:
            year = book.date_read.year
            pages_per_year[year] += book.pages

        #Prepare for matplotlib
        years = sorted(pages_per_year.keys())
        pages = [pages_per_year[year] for year in years]

        # Matplotlib Graph
        plt.figure(figsize=(12, 10))
        plt.plot(years, pages, 'bo-')
        plt.xticks(years, years)
        plt.xlabel("Year")
        plt.ylabel("Number of Pages")
        plt.title("Number of Pages Read per Year")
        plt.show()

    def pages_by_month(self, year):
        pages_per_month = defaultdict(int)

        for book in self.bookshelf.books_read:
            if book.date_read.year == year:
                month = book.date_read.month
                pages_per_month[month] += book.pages

        # Prepping for matplotlib
        months = sorted(pages_per_month.keys())
        pages = [pages_per_month[month] for month in months]

        # Matplotlib Graph
        plt.figure(figsize=(12, 10))
        plt.plot(months, pages, 'bo-')
        plt.xticks(months, months)
        plt.xlabel("Month")
        plt.ylabel("Number of Pages")
        plt.title("Monthly Pages Read for Year {}".format(year))
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
            print(" ")
            print(f"__________________{self.bookshelf.username}'s Statistics_________________________")
            total_pages = self.total_pages(self.bookshelf.books_read)
            total_books = len(self.bookshelf.books_read)
            print(f"Books Read: {total_books}")
            print(f"Total Pages Read - All Time: {total_pages}")
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
                    flag = True
                    while flag:
                        year = (input("Enter the year you want to see: "))
                        try:
                            year = int(year)
                            flag = False
                            print("Books Read by Month")
                            print("_____________________________________")
                            self.read_by_month(year)
                            break
                        except ValueError:
                            continue

                    break
                if choice == "5":
                    print("Pages Read by Year")
                    print("_____________________________________")
                    self.pages_by_year()
                    break
                if choice == "6":
                    flag = True
                    while flag:
                        year = (input("Enter the year you want to see: "))
                        try:
                            year = int(year)
                            flag = False
                            print("Pages Read by Month")
                            print("_____________________________________")
                            self.pages_by_month(year)
                            break
                        except ValueError:
                            continue
                    break
                if choice == "7":
                    break_outer = True
                    break

            if break_outer:
                break



