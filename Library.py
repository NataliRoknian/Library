from Book import *
from Shelf import *
from Reader import *


class Library:

    def __init__(self):
        self.shelves = []
        for i in range(3):
            self.shelves.append(Shelf())
        self.readers =[]


    # check if there is a place for new book in one of the shelves - if yes return treu else false
    def is_there_place_for_new_book(self):
        is_shelves_are_full = list(map((lambda x : x.is_shelf_full), self.shelves))
        return(not(is_shelves_are_full[0] and is_shelves_are_full[1] and is_shelves_are_full[2]))


    # add new book to the first Shelf with a free space 
    def add_new_book(self, new_book):
        if(self.is_there_place_for_new_book()):
            shelves_with_free_space = list(filter((lambda x : x.is_shelf_full == False), self.shelves))
            first_shelf_available = shelves_with_free_space[0]
            first_shelf_available.add_book(new_book)


    # delete book from the library 
    def delete_book(self, book_title):
        for shelf in self.shelves :
            for book in range(len(shelf.books)):
                if (shelf.books[book].title == book_title):
                    shelf.books.pop(book)


    # change 2 books locations
    def change_locations(self, book1, book2):
        
        def find_book_location(book_title):
            for shelf in range(len(self.shelves)):
                for book in range(len(self.shelves[shelf].books)):
                    if(self.shelves[shelf].books[book].title == book_title):
                        return [shelf,book]

        book1_location = find_book_location(book1)
        book2_location = find_book_location(book2)
        temp = self.shelves[book1_location[0]].books[book1_location[1]]
        self.shelves[book1_location[0]].books[book1_location[1]] = self.shelves[book2_location[0]].books[book2_location[1]]
        self.shelves[book2_location[0]].books[book2_location[1]] = temp



    # replace between 2 books in the same shelf
    def change_locations_in_same_shelf(self, shelf, book1, book2):
        self.shelves[shelf].replace_books(book1, book2) 



    # order all books in each shelf by their num of pages
    def order_books(self) :
        for shelf in self.shelves :
            shelf.order_books()


    # add new user to readers list
    def register_reader(self, reader_name, reader_id) :
        new_reader = Reader()
        new_reader.name = reader_name
        new_reader.id = reader_id
        self.readers.append(new_reader)


    # remove reader from readers list
    def remove_reader(self, reader_name) :
        self.readers = list(filter(lambda x : x.name != reader_name, self.readers))


    # add book to the reader’s books list
    def reader_read_book(self, book_title , reader_name) :
        for reader in self.readers :
            if (reader.name == reader_name) :
                reader.read_book(book_title)
                break


    # return all books of author
    def search_by_author(self, author_name) :
        author_books = []
        for shelf in self.shelves :
            for book in shelf.books :
                if (book.author == author_name) :
                    author_books.append(book.title)
        return author_books


    # convert to json
    def convert_to_json(self) :
        return {
            "shelves" : list(map(lambda shelf : shelf.convert_to_json() , self.shelves)),
            "readers" : list(map(lambda reader : reader.convert_to_json() , self.readers))
        }