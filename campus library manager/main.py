# main.py
from models import Book, Member, Magazine, DVD 

book = Book("Python 101", 1, "A. Rao")
# TODO: create one Magazine and one DVD
magazine = Magazine("Science Monthly", 2, "July 2024")
dvd = DVD("Inception", 3, 148)

alice = Member("Alice", 101)
bob = Member("Bob", 102, max_items=1)

# 1. Borrowing with error handling
try:
    alice.borrow(book)
    print("Alice borrowed:", book.describe())
    bob.borrow(book)  # should fail: already borrowed
except ValueError as e:
    print("Could not borrow:", e)


# 2. trigger the borrow-limit error and the not-borrowed error, catching each
try:
    bob.borrow(magazine)
    print("Bob borrowed:", magazine.describe())
    bob.borrow(dvd)  # should fail: limit reached
except ValueError as e:
    print("Could not borrow:", e)

try:
    bob.return_item(book)  # should fail: not borrowed by Bob
except ValueError as e:
    print("Could not return:", e)


# 3. Polymorphism: one loop, no type checks
items = [book, magazine, dvd]  # add the magazine and the DVD
for item in items:
    print(item.describe(), "-> late fee for 3 days: Rs", item.late_fee(3))

# 4. Class attribute shared by all objects
print("Total items created:", Book.total_items)


# 5. Try item.__available from outside the class and note the AttributeError; then read availability properly with is_available().
# print(book.__available)  # will result in AttributeError

print(f"{book}-availability: {book.is_available()}") # should print False, since Alice borrowed it