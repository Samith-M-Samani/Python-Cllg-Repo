class Book:
    def __init__(self, book_id, title, author, price, copies_available):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.price = price
        self.copies_available = copies_available
    
    def display_book(self):
        print("=" * 20)
        print("Book ID:", self.book_id)
        print("Title:", self.title)
        print("Author:", self.author)
        print("Price:", self.price)
        print("Copies Available:", self.copies_available)
        print("=" * 20)
    
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
books=[]
n=int(input("How many books you want to enter?"))
for i in range (n):
    print("Enter title,author,quantity and price of book",i+1)
    book_id=input()
    title=input()
    author=input()
    qty=int(input())
    price=float(input())
    books.append(Book(title,author,qty,price,book_id))
for book in books:
    book.display_book()
#book.get_data()