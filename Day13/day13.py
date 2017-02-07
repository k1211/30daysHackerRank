# Given a Book class and a Solution class, write a MyBook class that does the following:
#
# - Inherits from Book
# - Has a parameterized constructor taking these 3 parameters:
#     - string title
#     - string author
#     - int price
# Implements the Book class' abstract display() method so it prints these 3 lines:
# Title: , a space, and then the current instance's title.
# Author: , a space, and then the current instance's author.
# Price: , a space, and then the current instance's price.

from abc import ABCMeta, abstractmethod
class Book:
    __metaclass__ = ABCMeta
    def __init__(self, title, author):
        self.title = title
        self.author = author
    @abstractmethod
    def display(): pass

class My_Book(Book):
    def __init__(self, title, author, price):
        Book.__init__(self,title,author)
        self.price = price

    def display(self):
        print "Title: {}\nAuthor: {}\nPrice: {}".format(self.title, self.author, self.price)

title = raw_input()
author = raw_input()
price = int(raw_input())
new_novel = My_Book(title,author,price)
new_novel.display()