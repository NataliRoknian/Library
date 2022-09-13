from datetime import date

class Reader:

    def __init__(self):
        self.id = 0
        self.name = ""
        self.books = [{ "title" : "" , "date" : "" }]
    
    # read book
    def read_book(self, book_title):
        self.books.append({"title":book_title, "date":date.today()})

    
    # convert to json
    def convert_to_json(self) :
        return {
            "id" : self.id,
            "name" : self.name,
            "books" : self.books
        }