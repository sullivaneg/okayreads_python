# Main module
from bookshelf import Bookshelf
from stats import Stats
from datetime import date

today = date.today()
bookshelf = Bookshelf(today)
stats = Stats(bookshelf)
bookshelf.interface()