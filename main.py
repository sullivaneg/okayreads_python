# Main module
from bookshelf import Bookshelf
from communication import Comms
from stats import Stats
from datetime import date

today = date.today()
bookshelf = Bookshelf(today)
comms = Comms(bookshelf)
bookshelf.comms =comms
stats = Stats(bookshelf)
bookshelf.stats = Stats(bookshelf)
bookshelf.interface()
