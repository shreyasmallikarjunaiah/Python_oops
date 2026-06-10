
class Circle:
	def __init__(self,radius):
		self.radius = radius

	def diameter(self):
		# return self.radius*2
		print(self.radius*2)

one=Circle(5)
one.diameter()



class Backpack:
	def __init__(self):
		self._items=[]

	@property
	def items(self):
		return self._items

	def Add_item(self,item):
		if isinstance(item,str):
			self._items.append(item)
		else:
			print("Item is not a string")

	def remove_item(self, item):
		if item in self._items:
			self._items.remove(item)
		else:
			print("Item is not in the list")
	def has_item(self,item):
		return item in self._items



my_backpack=Backpack()
print(my_backpack._items)

my_backpack.Add_item("apple")
print(my_backpack._items)

my_backpack.Add_item("banana")
print(my_backpack._items)
my_backpack.Add_item("orange")
print(my_backpack._items)
my_backpack.Add_item("grape")
print(my_backpack._items)
my_backpack.Add_item("mango")
print(my_backpack._items)

my_backpack.remove_item("orange")
print(my_backpack._items)


has_mango=my_backpack.has_item("mango")
print(has_mango)




# class Backpack:
# 	def __init__(self):
# 		self._items=[]
#
# 	def add_item(self,item):
# 		self._items.append(item)
# 	def show_elements(self,condition=False):
# 		if condition:
# 			print(sorted(self._items))
# 		else:
# 			print(self._items)
#
# my_backpack=Backpack()
# print(my_backpack._items)
# my_backpack.add_item("apple")
# my_backpack.add_item("banana")
# my_backpack.add_item("orange")
# my_backpack.add_item("grape")
# my_backpack.add_item("mango")
#
# print("with sort")
# my_backpack.show_elements(condition=True)
# print("without sort")
# my_backpack.show_elements()


class Backpack:
	def __init__(self):
		self._items=[]
	def multipl(self,items):
		for item in items:
			self.add_item(item)
	def add_item(self,item):
		self._items.append(item)
	def show_elements(self,condition=False):
		if condition:
			print(sorted(self._items))
		else:
			print(self._items)


my_backpack=Backpack()
print(my_backpack._items)
my_backpack.multipl(["apple","banana","grape","mango"])
print(my_backpack._items)


# Method chaining

class Pizza:

	def __init__(self):
		self.toppings = []

	def add_topping(self, topping):
		self.toppings.append(topping.lower())
		return self

	def show_toppings(self):
		print("This Pizza has:")
		for topping in self.toppings:
			print(topping.capitalize())

pizza=Pizza()
pizza.add_topping("cheese").add_topping("magareta").add_topping("onion").show_toppings()
