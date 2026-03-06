# Library Book Management System
# Class, Object and Array of Objects problem

class Book:
    def __init__(self, book_id, title, author, price, copies_available):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.price = price
        self.copies_available = copies_available
    
    def display_book(self):
        print("=" * 40)
        print("Book ID:", self.book_id)
        print("Title:", self.title)
        print("Author:", self.author)
        print("Price:", self.price)
        print("Copies Available:", self.copies_available)
        print("=" * 40)
    
    def issue_book(self, quantity):
        if quantity > self.copies_available:
            print("Not enough copies available")
            return False
        else:
            self.copies_available -= quantity
            print(f"Issued {quantity} copy(s) of '{self.title}'")
            return True
    
    def add_copies(self, quantity):
        self.copies_available += quantity
        print(f"Added {quantity} copy(s) to '{self.title}'")
    
    def book_value(self):
        return self.price * self.copies_available


# Main program
# Create library list to store book objects
library = []

# Create 3 book objects as specified
book1 = Book(101, "Python Programming", "Mark Lutz", 750, 5)
book2 = Book(102, "Data Structures and Algorithms", "Thomas H. Cormen", 1200, 3)
book3 = Book(103, "Machine Learning Basics", "Andrew Ng", 950, 4)

# Add books to library
library.append(book1)
library.append(book2)
library.append(book3)

# Display all books
print("\n" + "=" * 50)
print("DISPLAYING ALL BOOKS IN LIBRARY")
print("=" * 50)
for book in library:
    book.display_book()

# Issue copies of a book
print("\n" + "=" * 50)
print("ISSUE BOOK OPERATION")
print("=" * 50)
# Issue 2 copies of book 1
library[0].issue_book(2)
print(f"Available copies now: {library[0].copies_available}")

# Try to issue more than available
print("\nTrying to issue 10 copies (more than available):")
library[0].issue_book(10)

# Add copies to a book
print("\n" + "=" * 50)
print("ADD COPIES OPERATION")
print("=" * 50)
library[1].add_copies(5)
print(f"Available copies now: {library[1].copies_available}")

# Calculate total value of all books in the library
print("\n" + "=" * 50)
print("TOTAL VALUE OF ALL BOOKS")
print("=" * 50)
total_value = 0
for book in library:
    book_val = book.book_value()
    print(f"'{book.title}': {book.price} x {book.copies_available} = {book_val}")
    total_value += book_val

print("\n" + "=" * 50)
print(f"TOTAL LIBRARY VALUE: {total_value}")
print("=" * 50)

# Display final state of all books
print("\n" + "=" * 50)
print("FINAL STATE OF ALL BOOKS")
print("=" * 50)
for book in library:
    book.display_book()

