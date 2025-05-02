import pandas as pd

from communication import *
from datetime import datetime
import pickle_bookshelf as pb

class Bookshelf:
    def __init__(self, date_created):
        self.date_created = date_created
        self.books_read = []
        self.want_to_read = []
        self.favorites = []
        self._username = None
        self.comms = None
        self.stats = None

    def profile(self):
        print(f'{self.username}\'s profile')
        print(f'Profile created: {self.date_created}')
        print(f'Books read: {len(self.books_read)}')
        print(f'Want to read: {len(self.want_to_read)}')

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        self._username = username

    def add_book(self, title):
        result = self.comms.search_books_by_title(title)
        if not result:
            "Book not found"
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

                # Source: https://stackoverflow.com/questions/70634943/python-datetime-check-if-user-input-date-matches-format
                while True:
                    check = input("Please enter the date you read this book in the format YYYY-MM-DD: ")
                    try:
                        date_read = datetime.strptime(check, '%Y-%m-%d').date()
                        result.date_read = date_read
                        break
                    except ValueError:
                        print("Invalid input. Please enter a date in the format YYYY-MM-DD: ")
                        continue

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
                break

            if choice == '2':
                self.want_to_read.append(result)
                result.in_lists.append("want_to_read")
                print ("")
                print(f"{result.title} has been added to your want-to-read books.")
                break

            if choice == '3':
                self.favorites.append(result)
                result.in_lists.append("favorites")
                print("")
                print(f"{result.title} has been added to your favorite books.")
            else:
                break

    def remove_book(self, book_list, results):
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
            return []
        return result


    def export_data(self, from_list, title, author, isbn, my_rating, original_publication_year, date_read, date_added,
                    shelves, bookshelves, done_books):
        # BOOKS READ
        for item in from_list:
            if item not in done_books:
                if from_list == self.books_read:
                    shelves.append("read")
                    date_read.append(item.date_read)
                    date_added.append(item.date_read)
                    rating = round(item.my_rating / 2)
                    my_rating.append(rating)
                    if "favorites" in item.in_lists:
                        bookshelves.append("favorites")
                    else:
                        bookshelves.append("")
                elif from_list == self.want_to_read:
                    shelves.append("to-read")
                title.append(item.title)
                author.append(item.author)
                isbn.append(item.isbn)
                original_publication_year.append(item.year_published)
                done_books.append(item)
            else:
                shelves.append("")
                continue


    def interface(self):
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
                title = input("Search Keyword (author, title, ")
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
                                        print("2. Exit")
                                        change_rating = input("Enter your choice: ")
                                        if change_rating == "1":
                                            rating = input("Enter your new rating: ")
                                            item.rating = rating
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
                # Some columns are intentionally left blank, goodreads doesn't require all the columns to be populated
                title, author, isbn, my_rating, average_rating, publisher, binding, year_published, \
                    original_publication_year, date_read, date_added, shelves, bookshelves, my_review, done_books = \
                    [], [], [], [], [], [], [], [], [], [], [], [], [], [], []

                self.export_data(self.books_read, title, author, isbn, my_rating, original_publication_year, date_read, date_added,shelves, bookshelves, done_books)
                self.export_data(self.want_to_read,title, author, isbn, my_rating, original_publication_year, date_read, date_added,shelves, bookshelves, done_books)

                #Create Dataframe
                # SOURCES: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html
                data = {'Title': title, 'Author': author, 'ISBN': isbn, 'My Rating': my_rating, 'Average Rating': average_rating,
                        'Publisher': publisher, 'binding': binding, 'Year Published':year_published, 'Original Publication Year':
                        original_publication_year, 'Date Read': date_read, 'Date Added': date_added, 'Shelves': shelves,
                        'Bookshelves': bookshelves, 'My Review': my_review}
                df = pd.DataFrame(data)

                #Export to Excel
                #SOURCES: My final CSI160 Project / https://stackoverflow.com/questions/55170300/how-to-save-a-pandas-dataframe-to-an-excel-file
                df.to_excel("bookshelf.xlsx", index=False)

            if choice == '7':
                print("Saving...")
                pb.save_bookshelf(self)
                print("Exiting...")
                break




