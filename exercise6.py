from typing import List


class Book:
    
    def __init__(self, name, author, no_of_pages):
        self.name = name
        self.author = author
        self.num_of_pages = no_of_pages

    def display_info(self):
        print(
            f"""
Name: {self.name}
Author: {self.author}
Number of pages: {self.num_of_pages}
"""
        )


class Library:

    def __init__(self) -> None:
        self.no_of_books = 0
        self.books = []

    def add_book(self, book):
        self.no_of_books += 1
        self.books.append(book)

    def remove_book(self, book):
        self.no_of_books -= 1 
        idx = self.books.index(book)
        self.books.pop(idx)

    def print_no_books(self):
        print("Total books:", self.no_of_books)
    
    def show_all_books(self):
        for book in self.books:
            book.display_info()


# To show that your program doesn't persist the books after the program is stopped
# uncomment the below ones and run them
# book1.display_info()
# book2.display_info()
# book3.display_info()


book1 = Book('Wolf Hall', 'Hilary Mantel', 752)
book2 = Book('Never Let Me Go', 'Kazuo Ishiguro', 210)
book3 = Book('The Amber Spyglass', 'Philip Pullman', 89)

lib = Library()

lib.add_book(book1)
lib.add_book(book2)

lib.remove_book(book1)

lib.add_book(book3)
lib.print_no_books()
lib.show_all_books()