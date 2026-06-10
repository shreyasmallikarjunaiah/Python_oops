"""
Course: Python OOP - Object Oriented Programming for Beginners
By: Estefania Cassingena Navone
"""

class Circle:

    def __init__(self, radius, color):
        self.radius=radius
        self.color = color


my_circle = Circle(6, "Yellow")

print(my_circle.radius)
print(my_circle.color)
print(hex(my_circle.radius))        #we can see the memory address
my_circle.radius = 15
my_circle.color = "Black"

print(hex(my_circle.radius))        #we can see the memory address, wether changed or same
print(my_circle.color)
print(my_circle.radius)
print(my_circle.color)


