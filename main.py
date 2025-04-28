# Main module
from bookshelf import Bookshelf
from stats import Stats
from datetime import date

name = input("What would you like to be called? ")
today = date.today()
bookshelf = Bookshelf(name, today)
stats = Stats(bookshelf)

bookshelf.interface()