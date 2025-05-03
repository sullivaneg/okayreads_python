"""Main Module for the okayreads project code

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

# Main module
from bookshelf import Bookshelf
from communication import Comms
from stats import Stats
from datetime import date
import pickle_bookshelf

# 🥒
# Original Code from: CSI-260-01 Library Project
# Group: Abigail Gehlbach, Charles Justus, Emma Sullivan, Sebastian Dominguez
# Author: Abigail Gehlbach
# Note: Specific lines in3 this module that used Abigail's code as source code are marked with the pickle(cucumber) emoji
"""
This module initializes the bookshelf class, the comms class, the stats class and starts the main interface.
"""
today = date.today()

bookshelf = pickle_bookshelf.load_bookshelf() # 🥒

if bookshelf is None: # 🥒
    bookshelf = Bookshelf(today)
    comms = Comms(bookshelf)
    bookshelf.comms =comms
    stats = Stats(bookshelf)
    bookshelf.stats = Stats(bookshelf)

bookshelf.interface()
