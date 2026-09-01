class Library:

    def __init__(self, books):
        self.books = books

    def show_books(self):
        print("Available books:")
        for book in self.books:
            print(book)

    def borrow_book(self, book):
        if book in self.books:
            print("You borrowed:", book)
            self.books.remove(book)

class Student:

    def request_book(self, book):
        return book

books = ["Python", "C Programming", "Java", "Data science"]

library = Library(books)
student = Student()

library.show_books()

book = input("\nEnter the name of the book you want to borrow: ")

student.request_book(book)
library.borrow_book(book)

print("\nBooks remaining in the library:")
library.show_books()