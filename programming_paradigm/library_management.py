# Book class definition
class Book:
    def __init__(self, title, author):
        # Public attributes
        self.title = title
        self.author = author
        # Private attribute to track if the book is checked out
        self._is_checked_out = False

    # Method to check out the book
    def check_out(self):
        self._is_checked_out = True

    # Method to return the book
    def return_book(self):
        self._is_checked_out = False

    # Method to check if the book is checked out
    def is_checked_out(self):
        return self._is_checked_out


# Library class definition
class Library:
    def __init__(self):
        # Private list to store books
        self._books = []

    # Method to add a book to the library
    def add_book(self, book):
        self._books.append(book)

    # Method to check out a book by title
    def check_out_book(self, title):
        for book in self._books:
            if book.title == title and not book.is_checked_out():
                book.check_out()
                print(f"Book '{title}' has been checked out.")
                return
        print(f"Book '{title}' is either not available or already checked out.")

    # Method to return a book by title
    def return_book(self, title):
        for book in self._books:
            if book.title == title and book.is_checked_out():
                book.return_book()
                print(f"Book '{title}' has been returned.")
                return
        print(f"Book '{title}' is not checked out or doesn't exist.")

    # Method to list all available books (modified to include title and author)
    def list_available_books(self):
        available_books = [book for book in self._books if not book.is_checked_out()]
        if available_books:
            print("Available books:")
            for book in available_books:
                print(f"{book.title} by {book.author}")
        else:
            print("No books are available.")


# Main function
def main():
    # Setup a small library
    library = Library()
    library.add_book(Book("Brave New World", "Aldous Huxley"))
    library.add_book(Book("1984", "George Orwell"))

    # Initial list of available books
    print("Available books after setup:")
    library.list_available_books()

    # Simulate checking out a book
    library.check_out_book("1984")
    print("\nAvailable books after checking out '1984':")
    library.list_available_books()

    # Simulate returning a book
    library.return_book("1984")
    print("\nAvailable books after returning '1984':")
    library.list_available_books()


# Call the main function when the script is executed
if __name__ == "__main__":
    main()
