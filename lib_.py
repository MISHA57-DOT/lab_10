
class Book:
    def __init__(self, book_id, title, author, quantity):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.quantity = quantity
    def display(self):
        print("Book ID:", self.book_id)
        print("Book Title:", self.title)
        print("Author:", self.author)
        print("Available Quantity:", self.quantity)
class Library:
    def __init__(self):
        self.books = []
        self.issued_books = []
    def add_book(self):
        print("\n--- Add New Book ---")

        book_id = input("Enter Book ID: ")

        for book in self.books:
            if book.book_id == book_id:
                print("Book ID already exists!")
                return

        title = input("Enter Book Title: ")
        author = input("Enter Author Name: ")
        quantity = int(input("Enter Quantity: "))

        if quantity > 0:
            new_book = Book(book_id, title, author, quantity)
            self.books.append(new_book)
            print("Book added successfully!")
        else:
            print("Quantity must be greater than zero!")
    def view_books(self):
        print("\n--- All Books ---")

        if len(self.books) == 0:
            print("No books available!")
            return

        for book in self.books:
            print("-------------------")
            book.display()
    def search_book(self):
        print("\n--- Search Book ---")

        search = input("Enter Book ID or Title: ")
        found = False

        for book in self.books:
            if book.book_id == search or book.title == search:
                book.display()
                found = True

        if found == False:
            print("Book not found!")
    def issue_book(self):
        print("\n--- Issue Book ---")

        book_id = input("Enter Book ID: ")
        student_name = input("Enter Student Name: ")

        for book in self.books:
            if book.book_id == book_id:

                if book.quantity > 0:
                    book.quantity = book.quantity - 1

                    record = {
                        "book_id": book.book_id,
                        "title": book.title,
                        "student": student_name
                    }

                    self.issued_books.append(record)

                    print("Book issued successfully!")
                    return

                else:
                    print("Book is not available!")
                    return

        print("Book not found!")

    def return_book(self):
        print("\n--- Return Book ---")

        book_id = input("Enter Book ID: ")
        student_name = input("Enter Student Name: ")

        for record in self.issued_books:

            if (record["book_id"] == book_id and
                    record["student"] == student_name):

                for book in self.books:
                    if book.book_id == book_id:
                        book.quantity = book.quantity + 1
                        break

                self.issued_books.remove(record)

                print("Book returned successfully!")
                return

        print("Matching issued record not found!")
    def delete_book(self):
        print("\n--- Delete Book ---")

        book_id = input("Enter Book ID: ")

        for record in self.issued_books:
            if record["book_id"] == book_id:
                print("Cannot delete! Book is currently issued.")
                return

        for book in self.books:
            if book.book_id == book_id:
                self.books.remove(book)
                print("Book deleted successfully!")
                return

        print("Book not found!")
    def view_issued_books(self):
        print("\n--- Issued Books ---")

        if len(self.issued_books) == 0:
            print("No books are currently issued!")
            return

        for record in self.issued_books:
            print("-------------------")
            print("Book ID:", record["book_id"])
            print("Book Title:", record["title"])
            print("Student Name:", record["student"])
    def menu(self):
        while True:
            print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
            print("1. Add Book")
            print("2. View All Books")
            print("3. Search Book")
            print("4. Issue Book")
            print("5. Return Book")
            print("6. Delete Book")
            print("7. View Issued Books")
            print("8. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_book()

            elif choice == "2":
                self.view_books()

            elif choice == "3":
                self.search_book()

            elif choice == "4":
                self.issue_book()

            elif choice == "5":
                self.return_book()

            elif choice == "6":
                self.delete_book()

            elif choice == "7":
                self.view_issued_books()

            elif choice == "8":
                print("Thank you for using Library Management System!")
                break

            else:
                print("Invalid choice! Please select 1 to 8.")
library = Library()
library.menu()
