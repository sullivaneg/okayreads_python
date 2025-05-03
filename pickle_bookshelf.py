"""Pickle File to populate and store data in

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

import pickle
import os.path

# Original code from: CSI-260-01 Library Project
# Group: Abigail Gehlbach, Charles Justus, Emma Sullivan, Sebastian Dominguez
# Author: Abigail Gehlbach
"""
This module is for managing pickle. Pickle is a tool to serialize information to your disk. It keeps track of the current
books saved to the bookshelf when the user saves in the main interface.
"""
def save_bookshelf(bookshelf):
    """
    Saves bookshelf to disk.
    :param bookshelf:
    """
    pickle.dump(bookshelf, open("save.p", "wb"))

def load_bookshelf():
    """
    Loads a saved bookshelf from disk.
    :return:
    """
    if os.path.exists("./save.p"):
        print("opened file")
        try:
            with open("save.p", "rb") as f:
                cat = pickle.load(f)
            if cat:
                return cat
            else:
                return None
        except(FileNotFoundError, EOFError) as err:
            print(err)
    else:
        return None