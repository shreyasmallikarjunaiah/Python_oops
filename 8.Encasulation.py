


# Public

class ATM:
	def __init__(self, Bank_Name, Holder_Name, ATM_Pin):
		self.Bank_Name = Bank_Name
		self.Holder_Name = Holder_Name
		self.ATM_Pin = ATM_Pin

shreys=ATM("SBI", "Shreyas",1234)

print(f"1  {shreys.Bank_Name}, {shreys.Holder_Name}, {shreys.ATM_Pin}")






# Protected

class ATM:
	def __init__(self, Bank_Name, Holder_Name, ATM_Pin):
		self.Bank_Name = Bank_Name
		self.Holder_Name = Holder_Name
		self._ATM_Pin = ATM_Pin

shreys=ATM("SBI", "Shreyas",1234)

print(f"2  {shreys.Bank_Name}, {shreys.Holder_Name}, {shreys._ATM_Pin}")  # for protected use "_" to access


# Public

'''to access the private attribute we have three methods'''

# 1. Name Mangling (The Backyard Hack)

class ATM:
	def __init__(self, Bank_Name, Holder_Name, ATM_Pin):
		self.Bank_Name = Bank_Name
		self.Holder_Name = Holder_Name
		self.__ATM_Pin = ATM_Pin

shreys=ATM("SBI", "Shreyas",1234)

print(f"3  {shreys.Bank_Name}, {shreys.Holder_Name}, {shreys._ATM__ATM_Pin}")  # accessed by using class name

# Getter method

class ATM:
	def __init__(self, Bank_Name, Holder_Name, ATM_Pin):
		self.Bank_Name = Bank_Name
		self.Holder_Name = Holder_Name
		self.__ATM_Pin = ATM_Pin

	def get_pin(self):
		return self.__ATM_Pin

shreys=ATM("SBI", "Shreyas",1234)

print(f"4  {shreys.Bank_Name}, {shreys.Holder_Name}, {shreys.get_pin()}")

# Setter Method

class ATM:
	def __init__(self, Bank_Name, Holder_Name, ATM_Pin):
		self.Bank_Name = Bank_Name
		self.Holder_Name = Holder_Name
		self.__ATM_Pin = ATM_Pin

	def get_pin(self):
		return self.__ATM_Pin

	def set_pin(self, new_pin):
		if self.Holder_Name == "Shreyas" and self.Bank_Name == "SBI":  #if the condition is not satisfacted the the old valuse will get
			self.__ATM_Pin = new_pin
		else:
			print("access denide")

shreys=ATM("SBI", "Shreyas",1234)
shreys.set_pin(1000)
print(f"5  {shreys.Bank_Name}, {shreys.Holder_Name}, {shreys.get_pin()}")


# property

class ATM:
	def __init__(self, Bank_Name, Holder_Name, ATM_Pin):
		self.Bank_Name = Bank_Name
		self.Holder_Name = Holder_Name
		self.__ATM_Pin = ATM_Pin

	def get_pin(self):
		return self.__ATM_Pin

	def set_pin(self, new_pin):
		if self.Holder_Name == "Shreyas" and self.Bank_Name == "SBI":
			self.__ATM_Pin = new_pin
		else:
			print("access denide")

	ATM_Pin=property(get_pin,set_pin)   #only add this line for property

shreys=ATM("SBI", "Shreyas",1234)
shreys.ATM_Pin +=1
print(f"6  {shreys.Bank_Name}, {shreys.Holder_Name}, {shreys.ATM_Pin}")


# @property

class ATM:
	def __init__(self, Bank_Name, Holder_Name, ATM_Pin):
		self.Bank_Name = Bank_Name
		self.Holder_Name = Holder_Name
		self.__ATM_Pin = ATM_Pin

	@property
	def ATM_Pin(self):
		return self.__ATM_Pin

	@ATM_Pin.setter
	def ATM_Pin(self, new_pin):
		if self.Holder_Name == "Shreyas" and self.Bank_Name == "SBI":
			self.__ATM_Pin = new_pin
		else:
			print("access denide")


shreys=ATM("SBI", "Shreyas",1234)
shreys.ATM_Pin +=3
print(f"7  {shreys.Bank_Name}, {shreys.Holder_Name}, {shreys.ATM_Pin}")



# property

'''for more attribute hidden'''


class BouncyBall:

	def __init__(self, price, size, brand):
		self.__price = price
		self.__size = size
		self.__brand = brand

	def get_price(self):
		return self.__price
	def get_size(self):
		return self.__size
	def get_brand(self):
		return self.__brand

	def set_price(self, new_price):
		self.__price = new_price

	def set_size(self,new_size):
		self.__size = new_size


	def set_brand(self,new_brand):
		self.__brand = new_brand

	price = property(get_price, set_price)
	size = property(get_size, set_size)
	brand = property(get_brand, set_brand)


shirt = BouncyBall(2000, 34, "U.S.Polo")
shirt.price = 200
shirt.size = 34
shirt.brand = "Polo"
print(f"{shirt.price},{shirt.size}, {shirt.brand}")


# @property

'''for more attribute hidden'''


class BouncyBall:

	def __init__(self, price, size, brand):
		self.__price = price
		self.__size = size
		self.__brand = brand

	@property
	def price(self):
		return self.__price
	@price.setter
	def price(self, new_price):
		self.__price = new_price

	@property
	def size(self):
		return self.__size
	@size.setter
	def size(self,new_size):
		self.__size = new_size

	@property
	def brand(self):
		return self.__brand
	@brand.setter
	def brand(self,new_brand):
		self.__brand = new_brand




shirt = BouncyBall(2000, 34, "U.S.Polo")
shirt.price = 200
shirt.size = 34
shirt.brand = "Polo"
print(f"{shirt.price},{shirt.size}, {shirt.brand}")