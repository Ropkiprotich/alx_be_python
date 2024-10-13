class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
class EBook(Book):

    def __init__(self, title, author,page_size:int):
        super().__init__(title, author)
        self.page_size = page_size

class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count =page_count

class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        if isinstance(book, Book):  
            self._books.append(book)
        else:
            print("Only objects of type Book can be added.")

    def list_books(self):
        for book in self._books:
            if isinstance(book, EBook):
                    print(f"Title: {book.title}, Author: {book.author}, Page Size: {book.page_size} KB")
            elif isinstance(book, PrintBook):
                    print(f"Title: {book.title}, Author: {book.author}, Pages: {book.page_count}")
            else:
                 print(f"Title: {book.title}, Author: {book.author}")