# list1=[1,2,9,3,4,5]
# a=[]
# for i in list1:
#     if a<i:
#         a=i
# print(a)
# from symtable import Class
#
# class Human:
#     def __init__(self,name,age,height,weight):
#         self.name=name
#         self.age=age
#         self.height=height
#         self.weight=weight
#
# shreyas=Human("shreyi",20,5.9,57)
#
# print(shreyas.name)
# print(shreyas.age)
# print(shreyas.height)
# print(shreyas.weight)
#
# shreyas.name="hello"
# print(shreyas.name)
#
# class Circle:
#     def __init__(self, radius, color, border):
#         self.radius = radius
#         self.color = color
#         self.border = border
#
# my_circle = Circle(5, "Red", "Thick")
# there_circle = Circle(7, "blue", "Thin")
# # 1. Group the objects inside a list
# circle_list = [my_circle, there_circle]
#
# # 2. Iterate through the list
# for circle in circle_list:
#     print(f"This circle has a radius of {circle.radius} and is {circle.color}.")
from time import sleep

# Outputs:
# This circle has a radius of 5 and is Red.
# This circle has a radius of 7 and is blue.







# class Car:
# 	def __init__(self, colour, wheel, gear,milage):
# 		self.colour=colour
# 		self.wheel=wheel
# 		self.gear=gear
# 		self.milage=milage
#
# benz=Car("red",4,6,12)
# print(benz.colour)
#
# for attributes,values in vars(benz).items():
#     print (f"{attributes}={values}")





#
# class ATM:
# 	def __init__(self, Bank_Name, Holder_Name, ATM_Pin):
# 		self.Bank_Name = Bank_Name
# 		self.Holder_Name = Holder_Name
# 		self.__ATM_Pin = ATM_Pin
#
# 	def get_pin(self):
# 		return self.__ATM_Pin
#
# 	def set_pin(self,new_pin):
# 		self.__ATM_Pin=new_pin
#
# 	ATM_Pin=property(get_pin,set_pin)
#
# shreys=ATM("SBI", "Shreyas",1234)
# shreys.set_pin(5432)
#
# print(f"1  {shreys.Bank_Name}, {shreys.Holder_Name}, {shreys.ATM_Pin}")

# class BouncyBall:
#
# 	def __init__(self, price, size, brand):
# 		self.__price = price
# 		self.__size = size
# 		self.__brand = brand
#
# 	def get_price(self):
# 		return self.__price
# 	def get_size(self):
# 		return self.__size
# 	def get_brand(self):
# 		return self.__brand
#
# 	def set_price(self, new_price):
# 		self.__price = new_price
#
# 	def set_size(self,new_size):
# 		self.__size = new_size
#
#
# 	def set_brand(self,new_brand):
# 		self.__brand = new_brand
#
# 	price = property(get_price, set_price)
# 	size = property(get_size, set_size)
# 	brand = property(get_brand, set_brand)
#
#
# shirt = BouncyBall(2000, 34, "U.S.Polo")
# shirt.price = 200
# shirt.size = 34
# shirt.brand = "Polo"
# print(f"{shirt.price},{shirt.size}, {shirt.brand}")



# class BouncyBall:
#
# 	def __init__(self, price, size, brand):
# 		self.__price = price
# 		self.__size = size
# 		self.__brand = brand
#
# 	@property
# 	def price(self):
# 		return self.__price
# 	@price.setter
# 	def price(self, new_price):
# 		self.__price = new_price
#
# 	@property
# 	def size(self):
# 		return self.__size
# 	@size.setter
# 	def size(self,new_size):
# 		self.__size = new_size
#
# 	@property
# 	def brand(self):
# 		return self.__brand
# 	@brand.setter
# 	def brand(self,new_brand):
# 		self.__brand = new_brand
#
#
#
#
# shirt = BouncyBall(2000, 34, "U.S.Polo")
# shirt.price = 200
# shirt.size = 34
# shirt.brand = "Polo"
# print(f"{shirt.price},{shirt.size}, {shirt.brand}")


a="rrr"
b="rrr"
print(id(a))
print(id(b))

c=[1,2,3,4,5]
d=[1,2,3,4,5]
d=c
print(id(c))
print(id(d))

print(a==b)
print(a is b)

print(c==d)
print(c is d)
print(a is b)

a=[1,2,3,4,5]
b=[1,2,3,4,5]
c=a

print(a == b)
print(a == c)

my_list=[1,2,3,4,5]

def list1(seq):
    print(f" in side the function{id(seq)}")

list1(my_list)
print(f" out side the function{id(my_list)}")


# class Ball:
#     def __init__(self, radius):
#         self.radius = radius
#     def area(self, b, change=10):
#         self.radius = self.radius + change
#         self.radius = self.radius + b
#
#     def perimeter(self):
#         self.area(b, change)
#
#
# a=Ball(5)
# print(a.radius)
# a.area(5,3)
# print(a.radius)
# a.perimeter()
# print(a.area())
#



a=[1,2,3,4]
b=a[:]


print(id(a))
print(id(b))


class Ball:
    def __init__(self, radius):
        self.radius = radius
        self.radius -= radius
    def area(self, change=10):

         self.radius = self.radius + change


class bat(Ball):
    def game(self):
        # self.radius -=1
        return self.radius
        # return 0

my=Ball(5)

print(my.radius)
my.area()
print(my.radius)

you=bat(5)
print(you.radius)