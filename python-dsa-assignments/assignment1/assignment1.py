"""
📌 Assignment 1: Object-Oriented Programming in Python
Date: 2025-08-20

This assignment focuses on creating Python classes to practice object-oriented programming
concepts like constructors, methods, and data handling.

I am following the DSA course by **[Saurabh Shukla / Youtube Channel : MySirg]**, and this repository documents my learning journey with practice problems and assignments. 
These practise questions are a part of the assigments under "Dsa in Python" course.  
"""

# 1️ Person Class
class Person:
    def __init__(self, name=None, age=None):
        self.name = name
        self.age = age

    def show(self):
        print("Name:", self.name)
        print("Age:", self.age)


# Example usage:
if __name__ == "__main__":
    print("---- Person ----")
    person1 = Person("Deepak", 23)
    person1.show()

    print("-" * 40)

    # 2️ Circle Class
    class Circle:
        PI = 3.14

        def __init__(self, radius=None):
            self.radius = radius

        def set_radius(self, radius):
            self.radius = radius

        def get_radius(self):
            print("Radius:", self.radius)

        def get_area(self):
            area = Circle.PI * (self.radius ** 2)
            print("Area:", area)

        def get_circumference(self):
            circumference = 2 * Circle.PI * self.radius
            print("Circumference:", circumference)

    print("---- Circle ----")
    circle1 = Circle()
    circle1.set_radius(3)
    circle1.get_radius()
    circle1.get_area()
    circle1.get_circumference()

    print("-" * 40)

    # 3️ Rectangle Class
    class Rectangle:
        def __init__(self, length=None, breadth=None):
            self.length = length
            self.breadth = breadth

        def set_dimensions(self, length, breadth):
            self.length = length
            self.breadth = breadth

        def get_dimensions(self):
            print("Length:", self.length)
            print("Breadth:", self.breadth)

        def get_area(self):
            # Area = length * breadth
            area = self.length * self.breadth
            print("Area:", area)

    print("---- Rectangle ----")
    rectangle1 = Rectangle()
    rectangle1.set_dimensions(20, 10)
    rectangle1.get_dimensions()
    rectangle1.get_area()

    print("-" * 40)

    # 4️ Book Class
    class Book:
        def __init__(self, bookid=None, title=None, price=None):
            self.bookid = bookid
            self.title = title
            self.price = price

        def show(self):
            print("Book ID:", self.bookid)
            print("Title:", self.title)
            print("Price:", self.price)

    print("---- Book ----")
    book1 = Book(1, "Diary of a Young Girl", 100)
    book1.show()

    print("-" * 40)

    # 5️ Team Class
    class Team:
        def __init__(self):
            # Avoid mutable default arguments by initializing inside __init__
            self.members = []

        def add_member(self, name):
            self.members.append(name)

        def show_members(self):
            print("Team Members List:")
            for member in self.members:
                print(member)

    print("---- Team ----")
    team1 = Team()
    team1.add_member("Avi")
    team1.add_member("Mavi")
    team1.add_member("Avisha")
    team1.show_members()
