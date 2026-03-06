Class, object and array of object problem

Here is a moderate problem statement using Class, Object, and Array (list) of Objects in Python.
🔶 Problem: Library Book Management System
Design a program to manage books in a library using class, objects, and an array (list) of objects.
🔹 Class: Book
Create a class Book with the following instance variables:
• book_id
• title
• author
• price
• copies_available
🔹 Constructor
The constructor should initialize all the book details.
🔹 Instance Methods
Create the following methods:
1️⃣ display_book()
• Display complete book information.
2️⃣ issue_book(quantity)
• Reduce the number of available copies.
• If requested copies exceed available copies, print "Not enough copies available".
3️⃣ add_copies(quantity)
• Increase the number of copies available.
4️⃣ book_value()
• Return total value of the book in library
• Formula:
price × copies_available
🔹 Array (List) of Objects
In the main program:
• Create at least 3 book objects.
• Store them inside a list of objects called library.
• Perform the following operations:
• Display all books
• Issue copies of a book
• Add copies to a book
• Calculate total value of all books in the library

Book 1
• Book ID: 101
• Title: Python Programming
• Author: Mark Lutz
• Price: 750
• Copies Available: 5

Book 2
• Book ID: 102
• Title: Data Structures and Algorithms
• Author: Thomas H. Cormen
• Price: 1200
• Copies Available: 3
• 
Book 3
• Book ID: 103
• Title: Machine Learning Basics
• Author: Andrew Ng
• Price: 950
• Copies Available: 4