import collections
from hashlib import new
from typing import Collection
from pymongo import MongoClient
import json
import os
import sys
import requests
from Book import *
from Shelf import *
from Reader import *
from Library import *


client = MongoClient(port=27017)
db = client["booksDB"]
books_collection = db["books"]


library = Library()
books = list(books_collection.find({}))
for shelf in range(len(library.shelves)):
    for book in range(2):
        new_book = Book()
        new_book.author = books[(2*shelf)+book]["author"]
        new_book.title = books[(2*shelf)+book]["title"]
        new_book.num_of_pages = books[(2*shelf)+book]["num_of_pages"]
        library.shelves[shelf].add_book(new_book)



# Login
print("LOG IN \n")
user_name = input("Enter username : \n")
user_email = input("Enter email : \n")
response = requests.get("https://jsonplaceholder.typicode.com/users")
users = response.json()
users_names = list(map(lambda x : x["username"] , users))
users_emails = list(map(lambda x : x["email"] , users))
if(user_name in users_names and user_email in users_emails):
    user_name_index = users_names.index(user_name)
    user_email_index = users_emails.index(user_email)
    success_login = user_name_index == user_email_index
else:
    success_login = False
    print("Login Failed...")


def menu() :
    print("MENU \n")
    print("For adding a book - Press 1 \n")
    print("For deleting a book - Press 2 \n")
    print("For changing books locations - Press 3 \n")    
    print("For registering a new reader - Press 4 \n")
    print("For removing a reader - Press 5 \n")
    print("For searching books by author - Press 6 \n")
    print("For reading a book by a reader - Press 7 \n")
    print("For ordering all books - Press 8 \n")
    print("For saving all data - Press 9 \n")
    print("For loading data - Press 10 \n")
    print("For exit - Press 11 \n")
    choice = int(input("Enter your choice: \n"))
    return(choice)




while (success_login):
    choice = menu()

    if (choice == 1): 
        print("---adding new book--- \n")
        new_book = Book()
        new_book.author = input("name of author: \n")
        new_book.title = input("title of book: \n")
        new_book.num_of_pages = int(input("number of pages: \n"))
        library.add_new_book(new_book)

    elif (choice == 2):
        print("---deleting a book--- \n")
        book_title = input("book title: \n")
        library.delete_book(book_title)

    elif (choice == 3):
        print("---changing books locations--- \n")
        book1 = input("first book title: \n")
        book2 = input("second book title: \n")
        library.change_locations(book1, book2)

    elif (choice == 4):
        print("---registering a new reader--- \n")
        reader_name = input("reader name: \n")
        reader_id = input("reader ID : \n")
        library.register_reader(reader_name, reader_id)

    elif (choice == 5):
        print("---removing a reader--- \n")
        reader_name = input("reader name: \n")
        library.remove_reader(reader_name)
    
    elif (choice == 6):
        print("---searching books by author--- \n")
        author_name = input("author name: \n")
        author_books = library.search_by_author(author_name)
        print("Books list written by " + author_name + ": \n")
        for book in author_books : 
            print(book + "\n")
    
    elif (choice == 7):
        print("---reading a book by a reader--- \n")
        reader_id = input("reader id: \n")
        book_title = input("book title: \n")
        for reader in library.readers:
            if (reader.id == reader_id):
                reader.read_book(book_title)
                break
        
    elif (choice == 8):
        print("---ordering all books in library by num of pages--- \n")
        library.order_books()

    elif (choice == 9):
        print("---saving all data--- \n")
        file_name = input("File name: \n")
        with open(os.path.join(sys.path[0], file_name + ".json"),'w') as file :
            data = library.convert_to_json()
            json.dump(data, file)

    elif (choice == 10):
        print("---loading data--- \n")
        file_name = input("File name: \n")
        with open(os.path.join(sys.path[0], file_name + ".json"),'r') as file :
            data = json.load(file)
            for shelf in range(len(data["shelves"])) :
                library.shelves[shelf].is_shelf_full = data["shelves"][shelf]["is_shelf_full"]
                for book in data["shelves"][shelf]["books"] :
                    new_book.author = book["author"]
                    new_book.title = book["title"]
                    new_book.num_of_pages = book["num_of_pages"]
                    library.shelves[shelf].books.append(new_book)
            for reader in data["readers"] :
                new_reader = Reader()
                new_reader.id = reader["id"]
                new_reader.name = reader["name"]
                new_reader.books = reader["books"]
                library.readers.append(new_reader)

    elif (choice == 11):
        exit()