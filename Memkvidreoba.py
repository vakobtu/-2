#1
"""class Book:
    def __init__(self, title, author, numPages, publishdate):
        self._title = title
        self._author = author
        self._numPages = numPages
        self._publishdate = publishdate
    
    
myBook = Book

myBook._title = "Coding"
myBook._author = "Code Koshmaridze"
myBook._numPages = "128"
myBook._publishdate = "2021"



print("The title of the book is ", myBook._title, "\nIts author is", myBook._author, "\nIt contains ", myBook._numPages,"\nPublishdate", myBook._publishdate)

"""
#3
class Animal():
    def __init__(self, name, age):
        self._name = name
        self._age = age
    
    def speak(self):
        print("Wof", self._name, "Wooooffff", self._age, "Uff Woof Waf")
    
class Dog(Animal):
    def __init__(self, name, age):
        self._name = name
        self._age = age
        self.type = " Jack Russel Terrier"
Lucky = Dog ("Dog", 4)
Lucky.speak()

#4 ეს მემგონი არასწორია
class CallMixin():
    def call_someone(self,call):
        print(f"Sending Call to {self.phone}")
    
class Person:
    def __init__(self, fname, lname, phone):
        self.fname = fname
        self.lname = lname
        self.phone = phone

    def info(self):
        return f"Phone - {self.phone}, fName - {self.fname}, - lName {self.lname}"
    
if __name__ == '__main__':

    print(c.info())
    c.call_someone()
