# Main module
from bookshelf import Bookshelf
from communication import Comms
from stats import Stats
from datetime import date

today = date.today()
bookshelf = Bookshelf(today)
comms = Comms(bookshelf)
stats = Stats(bookshelf)
bookshelf.interface()
