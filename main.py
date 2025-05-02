# Main module
from bookshelf import Bookshelf
from communication import Comms
from stats import Stats
from datetime import date
import pickle_bookshelf

#SOURCE: Abbi Gehlbeck wrote the pickle part for our library project, I repurposed it, anything with the pickle emoji \
# is a part that I'm citing to her

today = date.today()

bookshelf = pickle_bookshelf.load_bookshelf() # 🥒

if bookshelf is None: # 🥒
    bookshelf = Bookshelf(today)
    comms = Comms(bookshelf)
    bookshelf.comms =comms
    stats = Stats(bookshelf)
    bookshelf.stats = Stats(bookshelf)

bookshelf.interface()
