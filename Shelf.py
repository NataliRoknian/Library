class Shelf:

    def __init__(self):
        self.books = []
        self.is_shelf_full = False 


    # add book
    def add_book(self, book):
        if(not self.is_shelf_full):
            self.books.append(book)
            if(len(self.books) == 5):
                self.is_shelf_full = True
        else:
            print("NO MORE SPACE IN SHELF")


    # replace books
    def replace_books(self, book1, book2):
        if (book1 > 5 or book2 > 5):
            print("one or more of the indexes are invalid - press only 1-5")
        else:
            shelf_length = len(self.books)
            if (book1 > shelf_length or book2 > shelf_length):
                print("There is only" + shelf_length + "books in this shelf")
            else:
                temp = self.books[book1]
                self.books[book1] = self.books[book2]
                self.books[book2] = temp


    # order book
    def order_books(self):
        self.books.sort(key= lambda x : x.num_of_pages)


    # convert to json
    def convert_to_json(self) :
        return {
            "books" : list(map(lambda book : book.convert_to_json() , self.books)),
            "is_shelf_full" : self.is_shelf_full
        }