# 25. Question: What are Python's magic (dunder) methods, and how are they used? Provide an example.

"""
Magic or dunder (double underscore) methods in Python are special methods that have double underscores at the beginning 
and end of their names. They allow developers to emulate built-in behavior or implement operator overloading."""

class Book:
    def __init__(self, pages):
        self.pages = pages
    
    def __add__(self, other):
        return Book(self.pages + other.pages)

book1 = Book(100)
book2 = Book(150)
book3 = book1 + book2
print(book3.pages)
