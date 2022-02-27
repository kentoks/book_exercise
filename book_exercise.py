class Book:
    def __init__(self, title, author, dewey, isbn):
        self.title = title
        self.author = author
        self.dewey = dewey
        self.isbn = isbn
        self.available = True
        self.borrower = False # none means false as well
        book_list.append(self) # holds book objects as created - main routine

    def book_details(self):
        print(self.title)
        print(self.author)
        print(self.dewey)
        print(self.isbn)
        print(self.isbn)
        print(self.available)
        print(self.borrower)
        print("__________________________________")

# print list of books
def print_info():
    for book in book_list:
        book.book_details()

class User:
    def __init__(self, name, address):
        self.name = name # string
        self.address = address # string
        self.fees = 0.0 # float
        self.borrowed_books = []
        user_list.append(self)

    def user_details(self):
        print("Name: ", self.name)
        print("Address: ", self.address)
        print("Fees: $ ", self.fees)
        print("----------------------------------")

def print_user():
    for user in user_list:
        user.user_details()

# Add a new library user
def add_user():
    name = input("Enter the new user's name: ").title()
    address = input("Enter the new user's address: ")
    User(name, address)
    print(name, address, "has been added to your list")

# Add a new book
def add_book():
    title = input("Enter the new book's title: ").title()
    author = input("Enter the new book's author: ").title()
    dewey = input("Enter the new book's dewey code: ").title()
    isbn = input("Enter the new book's ISBN: ").title()
    Book(title, author, dewey, isbn)
    print(f"{title} has been added to the book list")

# Find a user
def find_user():
    user_to_find = input("Enter the user's name: ").title()
    for user in user_list:
        if user.name == user_to_find:
            print(f"Hi, {user_to_find}")
            return user
    print("Sorry, no user was found")
    return None

# Find a book
def find_book():
    book_to_find = input("Enter the name of the book: ").title()
    for book in book_list:
        if book.title == book_to_find:
            print(f"The book '{book_to_find}' is in the catalogue")
            return book
    print("Sorry, no book was found with that name")
    return None

# Lending
def lend_book():
    user = find_user()
    print()
    if user: # only if user was found
        book = find_book() # make sure that the book exists
        if book.available: # to see if book is available
            confirm = input("Type 'Y' if you want to borrow this "
                            "book: ").upper() # user confirms

            if confirm == "Y":
                print(f"Book title: '{book.title}' is now out on "
                      f"loan to {user.name}") # feedback to user
                book.available = False # set 'available attribute
                book.borrower = user.name # record borrower name
                user.borrowed_books.append(book.title)
        else:
            print(f"Sorry, '{book.title}' is already out on loan")


def returning_book():
    user = find_user()
    print()
    if user:
        book = find_book()
        if not book.available:
            confirm = input("Type 'Y' if you want to "
                            "return this book").upper()
            if confirm == "Y":
                print(f"Book title: '{book.title} is now returned "
                      f"to the library")
                book.available = True
                book.borrower = user.name
                user.borrowed_books.remove(book.title)
        else:
            print(f"Sorry, '{book.title}' is on loan to someone else")

# Main routine
book_list = []
user_list = []

# Create book objects
Book("Lord of the Rings", "J.R.R Tolkien", "TOL", "9780261103252")
Book("The Hunger Games", "Suzanne Collins", "COL", "9780261103252")
Book("A Tale of Two Cities", "Charles Dicksens", "DIC", "9781853262647")
Book("Harry Potter", "J.K Rowling", "ROW", "9780439321624")

# Create User objects
User("John", "12 Example road")
User("Susan", "1011 Binary road")
User("Paul", "25 Appletree Dr")
User("Mary", "8 Moon Cres")

lend_book()
print("_________________________")
returning_book()
# print_user()
# add_user()
# find_user()
# find_user()
# print_info()
# add_book()
# find_book()

# User menu
new_action = True
while new_action:
    print("1. Lend a book")
    print("2. Return a book")
    print("3. Add a user")
    print("4. Add a book")
    print("5. Exit")

    choice = input("\nWhat would you like to do? - enter a number: ")
    if choice == "1":
        lend_book()
    elif choice == "2":
        returning_book()
    elif choice == "3":
        add_user()
    elif choice == "4":
        add_book()
    elif choice == "5":
        confirm = input("Type 'Y' if you want to exit the system - or any other"
                        " key to go back to the menu: ").upper()
        if confirm =="Y":
            print("Goodbye")
            new_action = False
    else:
        print("\n__________ That was not a valid choice, please try again __________\n")



