class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(book, "added successfully.")

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print(book, "removed successfully.")
        else:
            print("Book not found.")

    def display_books(self):
        if len(self.books) == 0:
            print("No books available.")
        else:
            print("Available books:")
            for book in self.books:
                print("-", book)

    def issue_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print(book, "issued successfully.")
        else:
            print("Book not found.")

    def return_book(self, book):
        self.add_book(book)


# Creating libray object
library = Library()

# Adding books
library.add_book("Python Programming")
library.add_book("Data Science")
library.add_book("Operating System")

# Display books
library.display_books()

# Issue a book
library.issue_book("Python Programming")

# Display books again
library.display_books()

# Return the book
library.return_book("Python Programming")

# Display books again
library.display_books()

# Remove a book
library.remove_book("Operating System")

# Final list
library.display_books()