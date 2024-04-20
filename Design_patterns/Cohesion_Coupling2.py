class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available_copies = 10  # Initial number of copies

class Member:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.borrowed_books = []

class LibraryManagementSystem:
    def __init__(self):
        self.books = [
            Book("Book 1", "Author 1", "ISBN1"),
            Book("Book 2", "Author 2", "ISBN2"),
            Book("Book 3", "Author 3", "ISBN3"),
        ]
        self.members = []

    def add_member(self, name, email):
        member = Member(name, email)
        self.members.append(member)
        print(f"Member {name} added successfully")

    def borrow_book(self, member_name, book_title):
        member = self._find_member(member_name)
        book = self._find_book(book_title)

        if book is None:
            print(f"Book '{book_title}' not found")
            return

        if book.available_copies == 0:
            print(f"No copies of '{book_title}' available")
            return

        book.available_copies -= 1
        member.borrowed_books.append(book)
        print(f"Book '{book_title}' borrowed by {member_name}")

    def return_book(self, member_name, book_title):
        member = self._find_member(member_name)
        book = self._find_book(book_title)

        if book is None:
            print(f"Book '{book_title}' not found")
            return

        if book not in member.borrowed_books:
            print(f"{member_name} did not borrow '{book_title}'")
            return

        member.borrowed_books.remove(book)
        book.available_copies += 1
        print(f"Book '{book_title}' returned by {member_name}")

    def _find_member(self, name):
        for member in self.members:
            if member.name == name:
                return member
        return None

    def _find_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None

    def send_email_notification(self, member, message):
        print(f"Email sent to {member.email}: {message}")

# Usage
# library = LibraryManagementSystem()

# library.add_member("John Doe", "john@example.com")
# library.add_member("Jane Smith", "jane@example.com")

# library.borrow_book("John Doe", "Book 1")
# library.borrow_book("John Doe", "Book 2")
# library.borrow_book("Jane Smith", "Book 1")

# library.return_book("John Doe", "Book 1")

# library.send_email_notification(library.members[0], "Your book is due soon.")


##################################################################################################
from abc import ABC, abstractmethod

class Book:
    """
    This class is responsible for book related details and actions
    """
    INITIAL_NUMBER_OF_COPIES = 10

    def __init__(self, title: str, author: str, isbn: str):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available_copies = Book.INITIAL_NUMBER_OF_COPIES
        
    def update_available_copies(self, num: int):
        self.available_copies = self.available_copies + num

    def available_copies(self) -> int:
        return self.available_copies

class Member:
    """
    This class is responsible for member related details and actions
    """
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email
        self.borrowed_books = {}

    def add_book(self, book: Book):
        self.borrowed_books[book.title] = book

    def remove_book(self, book: Book):
        del self.borrowed_books[book.title]

    def is_book_borrowed(self, book: Book) -> bool:
        return book.title in self.borrowed_books

class LibraryManagementSystem:
    """
    This class is responsible for managing the library
    """
    def __init__(self):
        self.books = {
            'Ponniyin Selvan': Book("Ponniyin Selvan", "Kalki", "ISBN1"),
            'Neram Nirpadhillai': Book("Neram Nirpadhillai", "Thangavelu Marimuthu", "ISBN2"),
            'Atomic Habits': Book("Atomic Habits", "James Clear", "ISBN3"),
        }
        self.members = {}

    def add_member(self, member: Member):
        self.members[member.name] = member
        print(f"Member {member.name} added successfully")

    def borrow_book(self, member_name: str, book_title: str):
        try:
            member = self._find_member(member_name)
            book = self._find_book(book_title)

            if book is None:
                print(f"Book '{book_title}' not found")
                return

            if book.available_copies == 0:
                print(f"No copies of '{book_title}' available")
                return

            book.update_available_copies(-1)
            member.add_book(book)
            print(f"Book '{book_title}' borrowed by {member_name}")

        except Exception as e:
            print(f"Error: {e}")

    def return_book(self, member_name: str, book_title: str):
        try:
            member = self._find_member(member_name)
            book = self._find_book(book_title)

            if book is None:
                print(f"Book '{book_title}' not found")
                return

            if not member.is_book_borrowed(book):
                print(f"{member_name} did not borrow '{book_title}'")
                return

            member.remove_book(book)
            book.update_available_copies(1)
            print(f"Book '{book_title}' returned by {member_name}")

        except Exception as exp:
            print(f"Error: {exp}")

    def _find_member(self, name: str) -> Member|None:
        return self.members.get(name)

    def _find_book(self, title) -> Book|None:
        return self.books.get(title)

class NotificationService(ABC):
    @abstractmethod
    def send():
        pass

class EmailNotificationService(NotificationService):
    """
    This class is responsible for sending email notifications
    for sending an email member object and message necessary
    """
    def __init__(self, member: Member, message: str):
        self.member = member
        self.message = message

    def send(self):
        print(f"Email sent to {self.member.email}: {self.message}")

if __name__ == "__main__":
    member1 = Member("Mutharasu", "arasu@example.com")
    member2 = Member("Tamil", "tamil@example.com")

    library = LibraryManagementSystem()
    library.add_member(member1)
    library.add_member(member2)

    library.borrow_book("Mutharasu", "Ponniyin Selvan")
    library.borrow_book("Tamil", "Neram Nirpadhillai")
    library.borrow_book("Jane Smith", "invalid book")

    library.return_book("Mutharasu", "Ponniyin Selvan")

    email = EmailNotificationService(member1, "Your book is due soon.")
    email.send()
