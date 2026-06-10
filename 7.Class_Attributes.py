



class vehicle:
	tax=4   # this is the class attribute
	def __init__(self, brand, Name, colour, HP, weels, price):
		self.brand=brand
		self.Name=Name
		self.colour=colour
		self.HP=HP
		self.weels=weels
		self.price=price
		self.totalPrice = None

	def include_tax(self):
		self.totalPrice=((vehicle.tax/100)*self.price)+self.price
		return self.totalPrice



adv=vehicle("Mahindra","TharRox", "Red", 100, 4, 2000000)
SUV=vehicle("TATA", "Safari", "white", 1200, 4, 3000000)

cars=(adv,SUV)
for car in cars:
	car.include_tax()
	print(f"{car.brand},{car.Name},{car.colour},{car.HP},{car.weels},{car.price},{car.totalPrice}")

for attributrs, values in vars(adv).items():
	print(f"{attributrs},{values}")