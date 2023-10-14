class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def lend_book(self, title):
        for book in self.books:
            if book.title == title and book.is_available:
                book.is_available = False
                return book
        return None

    def return_book(self, title):
        for book in self.books:
            if book.title == title and not book.is_available:
                book.is_available = True
                return book
        return None

    def display_books(self):
        print("\nLibrary Catalog:")
        for book in self.books:
            status = "Available" if book.is_available else "Not Available"
            print(f"Title: {book.title}, Author: {book.author}, Status: {status}")

if __name__ == '__main__':
    library = Library()

    # Adding books to the library
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
    book2 = Book("To Kill a Mockingbird", "Harper Lee")
    book3 = Book("Pride and Prejudice", "Jane Austen")

    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)

    while True:
        print("\nLibrary Management System")
        print("1. Display Books")
        print("2. Borrow Book")
        print("3. Return Book")
        print("4. Quit")
        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            library.display_books()
        elif choice == '2':
            title = input("Enter book title to borrow: ")
            book = library.lend_book(title)
            if book:
                print(f"You have borrowed '{book.title}'.")
            else:
                print("Book not available.")
        elif choice == '3':
            title = input("Enter book title to return: ")
            book = library.return_book(title)
            if book:
                print(f"'{book.title}' has been returned to the library.")
            else:
                print("Book not found or not borrowed.")
        elif choice == '4':
            print("Goodbye!")
            break
