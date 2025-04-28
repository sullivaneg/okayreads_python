from stats import *
from communication import *
import datetime

class Bookshelf:
    def __init__(self, username, date_created):
        self.username = username
        self.date_created = date_created
        self.books_read = []
        self.want_to_read = []
        self.favorites = []

    def profile(self):
        print(f'{self.username}\'s profile')
        print(f'Profile created: {self.date_created}')
        print(f'Books read: {len(self.books_read)}')
        print(f'Want to read: {len(self.want_to_read)}')

    def add_book(self, title):
        result = Comms.search_books_by_title(title)
        while True:
            if Comms.search_books_by_title(title):
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
                            print("Invalid input. Please enter a number.")
                            continue

                    # Source: https://stackoverflow.com/questions/70634943/python-datetime-check-if-user-input-date-matches-format
                    while True:
                        check = input("Please enter the date you read this book in the format YYYY-MM-DD: ")
                        try:
                            date_read = datetime.strptime(check, '%Y-%m-%d').date()
                            result.date_read = date_read
                            break
                        except ValueError:
                            print("Invalid input. Please enter a date in the format YYYY-MM-DD:.")
                            continue
                    self.books_read.append(result)
                    print(f"{result.title} has been added to your read books.")
                    break

                if choice == '2':
                    self.want_to_read.append(result)
                    print(f"{result.title} has been added to your want-to-read books.")
                    break

                if choice == '3':
                    self.favorites.append(result)
                    print(f"{result.title} has been added to your favorite books.")
                else:
                    break

    def remove_book(self, title):
        pass

    def search_bookshelf(self, string):
        pass

    def export_data(self):
        pass

    def interface(self):
        print("_________________okayreads_________________")
        print('')
        print(f'WELCOME TO YOUR BOOKSHELF {self.username}')
        print("")
        print("WHAT WOULD YOU LIKE TO DO?")
        print("___________________________________________")
        print("1. Add Book")
        print("2. Remove Book")

