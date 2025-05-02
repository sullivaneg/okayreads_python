import pickle
import os.path

# SOURCE: Abbi Gehlbeck wrote this part of our Library project and I repurposed it for pickle for this project
def save_bookshelf(bookshelf):
    pickle.dump(bookshelf, open("save.p", "wb"))

def load_bookshelf():
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