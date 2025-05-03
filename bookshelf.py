"""File for the main interface of the code as well as most functions that affect the bookshelf

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

import pandas as pd
from datetime import datetime
import pickle_bookshelf as pb

class Bookshelf:
    """
    This class represents the bookshelf object which holds the book objects and does actions to them. Also functions as
    the main interface.

    Attributes:
        date_created (datetime): keeps track of when the bookshelf was created.

        books_read (list): list of the books read by the user.
        want_to_read(list): list of the books the user wants to read.
        favorites(list): list of user's favorite books.
        self._username (str): the username of the user. Default: None
        self.comms: the instance of the communication class the bookshelf class instance uses. Default: None
        self.stats: the instance of the statistics class the bookshelf class instance uses. Default: None

    Methods:
        profile(self): prints out the profile of the user.
        add_book(self, title): adds a book to the bookshelf by adding it to one of the lists.
        remove_book(self, title): removes a book from the bookshelf by removing it from the list it's in.
        search_bookshelf(string): internal search of the bookshelf books.
        export data(from_list, title, author, isbn, my_rating, average_rating, publisher, binding, year_published,
                    original_publication_year, date_read, date_added, shelves, bookshelves, my_review, done_books):
                    returns completed lists for the create_df method.
        create_df(): creates a pandas dataframe from the bookshelf's lists.
        interface(): The main interface of the program, allows the user to navigate through different pages of options.

    Getters/Setters:
        username: sets/gets the username of the user. Default: None

    """
    def __init__(self, date_created):
        self.date_created = date_created
        self.books_read = []
        self.want_to_read = []
        self.favorites = []
        self._username = None
        self.comms = None
        self.stats = None

    def profile(self):
        """
        Returns User's profile information.
        :return: str
        """
        print(f'{self.username}\'s profile')
        print(f'Profile created: {self.date_created}')
        print(f'Books read: {len(self.books_read)}')
        print(f'Want to read: {len(self.want_to_read)}')

    @property
    def username(self):
        """
        Returns the username of the user.
        :return: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """
        Sets the username of the user.
        :param username:
        """
        self._username = username

    def add_book(self, title):
        """
        Adds a book to the bookshelf by adding it to one of the lists.
        :param title:
        :return: nothing
        """
        result = self.search_bookshelf(title)
        if result:
            for book in result:
                choice = input(f"From your bookshelf: {book.to_short_string()} | Is this your book? Y or N: ")
                if choice.lower() == 'y':
                    result = book
                    break
                if choice.lower() == 'n' and len(result) == 1:
                    result = False
                    break
                if choice.lower() == 'n':
                    result.remove(book)
                    continue

        if not result:
            result = self.comms.search_books_by_title(title)

        if not result or result is None:
            print("___________________NO RESULT FOUND______________")
            print(" ")
            print("Book not found. Please adjust spelling or try a different title.")
            print(" ")
            print("__________________________________________________")

            return

        while True:
            print("ADD BOOK TO WHICH LIST:")
            print("")
            print("1. Books I've Read")
            print("2. Want to Read")
            print("3. Favorites")
            print("4. Exit")
            print("")
            choice = input("Enter your choice: ")

            # Add book to read books and add date read and rating
            if choice == '1':
                while True:
                    check = input("How would you rate this book out of 10? (Decimals are allowed): ")
                    try:
                        rating = float(check)
                        result.rating = rating
                        break
                    except ValueError:
                        print("Invalid input. Please enter a number. ")
                        continue

                # Original Code from: Stack Overflow
                # URL: https://stackoverflow.com/questions/70634943/python-datetime-check-if-user-input-date-matches-format
                # Author: arshovon
                # Date: January 8, 2022
                while True:
                    check = input("Please enter the date you read this book in the format YYYY-MM-DD: ")
                    try:
                        date_read = datetime.strptime(check, '%Y-%m-%d').date()
                        result.date_read = date_read
                        break
                    except ValueError:
                        print("Invalid input. Please enter a date in the format YYYY-MM-DD: ")
                        continue
                # END STACK OVERFLOW

                while True:
                    check = input("How many pages did your book have?: ")
                    try:
                        pages = int(check)
                        result.pages = pages
                        break
                    except ValueError:
                        print("Invalid input. Please enter a number. ")
                        continue

                self.books_read.append(result)
                result.in_lists.append("books_read")
                print("")
                print(f"{result.title} has been added to your read books.")
                print("")
                break

            if choice == '2':
                self.want_to_read.append(result)
                result.in_lists.append("want_to_read")
                print ("")
                print(f"{result.title} has been added to your want-to-read books.")
                print("")
                break

            if choice == '3':
                self.favorites.append(result)
                result.in_lists.append("favorites")
                print("")
                print(f"{result.title} has been added to your favorite books.")
                print("")
            else:
                break

    def remove_book(self, book_list, results):
        """
        Removes a book from one of the lists.
        :param book_list: which list the user would like to remove a book from.
        :param results: The results of the search, user will choose whether they want to remove the book or not.
        :return: nothing or an empty list of there are no search results.
        """
        if results:
            break_outer = False
            for item in results:
                if item not in book_list:
                    continue
                print(item)
                while True:
                    choice = input("Do you want to remove it? (y/n): ").lower()
                    if choice == "y":
                        book_list.remove(item)
                        print(f"{item.title} has been removed from your bookshelf.")
                        break_outer = True
                        break
                    elif choice == "n":
                        break
                    else:
                        print("Invalid input. Please enter y/n. ")
                        continue
                if break_outer:
                    break
        else:
            return []

    def search_bookshelf(self, string):
        """searches by name the books that are already on user's bookshelf"""
        result = []
        for entry in self.books_read:
            if entry.match(string):
                result.append(entry)
        for entry in self.want_to_read:
            if entry.match(string) and entry not in result:
                result.append(entry)
        for entry in self.favorites:
            if entry.match(string) and entry not in result:
                result.append(entry)
        if not result:
            return False
        return result


    def export_data(self, from_list, title, author, isbn, my_rating, average_rating, publisher, binding, year_published,
                    original_publication_year, date_read, date_added, shelves, bookshelves, my_review, done_books):
        """
        Takes in empty lists adds book instance information to the lists. Some columns are intentionally left empty. The
        lists match the default form to upload books to Goodreads so all columns are needed but not all need to be filled.
        :param from_list: which list to loop through.
        :param title: Empty List -> :returns list of titles.
        :param author: Empty List -> :returns list of authors.
        :param isbn: Empty List -> :returns list of ISBNs.
        :param my_rating: Empty List -> :returns list of book ratings.
        :param average_rating: Empty list.
        :param publisher: Empty list.
        :param binding: Empty list.
        :param year_published: Empty List.
        :param original_publication_year: Empty List -> :returns List of the publication years of the book objects.
        :param date_read: Empty List -> :returns list of dates the books were read.
        :param date_added: Empty List -> :returns list of the same dates as date_read.
        :param shelves: Empty List -> :returns either 'read' or 'to-read'
        :param bookshelves: Empty List -> :returns either 'favorites' or Empty
        :param my_review: Empty List.
        :param done_books: list of books that have contributed to the column lists so far.
        :return: Filled lists to become columns in the dataframe.
        """
        # BOOKS READ
        for item in from_list:
            if item not in done_books:
                if from_list == self.books_read:
                    shelves.append("read")
                    date_read.append(item.date_read)
                    date_added.append(item.date_read)
                    rating = round(item.rating / 2)
                    my_rating.append(rating)
                    if "favorites" in item.in_lists:
                        bookshelves.append("favorites")
                    else:
                        bookshelves.append("")
                elif from_list == self.want_to_read:
                    shelves.append("to-read")
                    date_read.append("")
                    date_added.append("")
                    my_rating.append("")
                    bookshelves.append("")
                title.append(item.title)
                author.append(item.author)
                isbn.append(item.isbn)
                original_publication_year.append(item.year_published)
                done_books.append(item)
                average_rating.append("")
                publisher.append("")
                binding.append("")
                year_published.append("")
                my_review.append("")
            else:
                continue
        return (title, author, isbn, my_rating, average_rating, publisher, binding, year_published, original_publication_year,
                date_read, date_added, shelves, bookshelves, my_review, done_books)

    def create_df(self):
        # Some columns are intentionally left blank, goodreads doesn't require all the columns to be populated
        title, author, isbn, my_rating, average_rating, publisher, binding, year_published, \
            original_publication_year, date_read, date_added, shelves, bookshelves, my_review, done_books = \
            [], [], [], [], [], [], [], [], [], [], [], [], [], [], []

        self.export_data(self.books_read, title, author, isbn, my_rating, average_rating, publisher, binding,
                         year_published, original_publication_year, date_read, date_added, shelves, bookshelves,
                         my_review, done_books)
        self.export_data(self.want_to_read, title, author, isbn, my_rating, average_rating,
                         publisher, binding, year_published, original_publication_year,
                         date_read, date_added, shelves, bookshelves, my_review, done_books)

        # Create Dataframe
        # SOURCES: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html
        data = {'Title': title, 'Author': author, 'ISBN': isbn, 'My Rating': my_rating,
                'Average Rating': average_rating,
                'Publisher': publisher, 'binding': binding, 'Year Published': year_published,
                'Original Publication Year':
                    original_publication_year, 'Date Read': date_read, 'Date Added': date_added, 'Shelves': shelves,
                'Bookshelves': bookshelves, 'My Review': my_review}
        df = pd.DataFrame(data)
        return df

    def interface(self):
        """
        Main interface of the program. Presents the users with menus. Takes care of error handling.
        """
        if self.username is None:
            username = input("What would you like to be called?")
            self.username = username

        while True:
            print("_________________okayreads_________________")
            print('')
            print(f'WELCOME TO OKAYREADS {self.username}')
            print("")
            print("___________________________________________")
            print("1. Add Book")
            print("2. Remove Book")
            print("3. Your Bookshelf")
            print("4. Statistics")
            print("5. Change Username")
            print("6. Export your Bookshelf as an Excel file")
            print("7. Save and Exit")
            choice = input("Enter your choice: ")

            # CHOICE 1: ADD BOOK
            if choice == '1':
                title = input("Search Title of your book: ")
                self.add_book(title)

            #CHOICE 2: REMOVE BOOK
            if choice == '2':
                while True:
                    break_outer = False
                    print("REMOVE BOOK")
                    print("____________________")
                    print("1. Books Read")
                    print("2. Want to Read")
                    print("3. Favorites")
                    print("4. Exit")
                    choice = input("Choose an option: ")
                    try:
                        choice = int(choice)
                    except ValueError:
                        print("Invalid input. Please enter a number. ")
                        continue

                    to_remove = input("Which title would you like to remove: ")
                    results = self.search_bookshelf(to_remove)

                    #CHOICE 2.1: REMOVE BOOK FROM BOOKS READ
                    if choice == 1:
                        result = self.remove_book(self.books_read, results)
                        if result == "No Results Found":
                            print("No Results Found")
                            break
                    #CHOICE 2.2: REMOVE BOOK FROM WANT TO READ
                    if choice == 2:
                        result= self.remove_book(self.want_to_read, results)
                        if result == "No Results Found":
                            print("No Results Found")
                            break
                    #CHOICE 2.3: REMOVE BOOK FROM FAVORITES
                    if choice == 3:
                        result = self.remove_book(self.favorites, results)
                        if result == "No Results Found":
                            print("No Results Found")
                            break

                    #CHOICE 2.4 EXIT
                    if choice == 4:
                        break_outer = True
                        break

                if break_outer:
                    break
            #CHOICE 3: YOUR BOOKSHELF
            if choice == '3':
                while True:
                    print(f"WELCOME TO YOUR BOOKSHELF {self.username}")
                    print("__________________________________________")
                    print("1. Search for a book on your bookshelf")
                    print("2. Your read books")
                    print("3. Your want-to-read list")
                    print("4. Your favorite books")
                    print("5. Exit")
                    choice = input("Choose an option: ")
                    try:
                        choice = int(choice)
                    except ValueError:
                        print("Invalid input. Please enter a number. ")

                    #SEARCH YOUR BOOKSHELF - DISPLAYS BOOK INFO
                    if choice == 1:
                        search = input("Enter the book title: ")
                        result = self.search_bookshelf(search)
                        check = True
                        if result:
                            break_outer = False
                            for item in result:
                                print(item)
                                while True:
                                    choice = input("Is this your choice? (y/n): ").lower()
                                    if choice == "y":
                                        item.profile_string()
                                        print("__________________________________________")
                                        print("1. Change Rating")
                                        print("2. Add to Favorites")
                                        print("3. Exit")
                                        change_rating = input("Enter your choice: ")
                                        if change_rating == "1":
                                            rating = input("Enter your new rating: ")
                                            item.rating = rating
                                        if change_rating == "2":
                                            if "favorites" not in item.in_lists:
                                                item.in_lists.append("favorites")
                                            if "favorites" in item.in_lists:
                                                print(f"{item.title} is already in your favorite list")
                                        break_outer = True
                                        break
                                    elif choice == "n":
                                        break
                                    else:
                                        print("Invalid input. Please enter y/n. ")
                                        continue
                                if break_outer:
                                    break
                        else:
                            check = False
                            error = "No Results Found"

                        if not check:
                            print(error)
                            break



                    if choice == 2:
                        print("BOOKS READ")
                        print("____________________________________________")
                        for book in self.books_read:
                            print(book.to_short_string())

                    if choice == 3:
                        print("READING LIST")
                        print("____________________________________________")
                        for book in self.want_to_read:
                            print(book.to_short_string())

                    if choice == 4:
                        print("FAVORITES")
                        print("____________________________________________")
                        for book in self.favorites:
                            print(book.to_short_string())

                    else:
                        break

            # CHOICE 4: STATISTICS INTERFACE
            if choice == '4':
                self.stats.interface()

            # CHOICE 5: CHANGE USERNAME
            if choice == '5':
                username = input("Enter your new username: ")
                self.username = username

            # CHOICE 6: EXPORT DATA AS EXCEL FILE
            if choice == '6':
                df = self.create_df()
                print("Exporting to bookshelf.xlsx...")
                print(df)

                #Export to Excel
                # Original code from: Final CSI-160 Project Champlain College
                # Author: Emma Sullivan
                # Date: November 2024

                df.to_excel("bookshelf.xlsx", index=False)
                print("Exported to bookshelf.xlsx")

                # END FINAL 160 CODE

            if choice == '7':
                print("Saving...")
                pb.save_bookshelf(self)
                print("Exiting...")
                break




