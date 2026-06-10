class Vehicle:
	def __init__(self, engine, breaks, milage):
		self.engine = engine
		self.breaks = breaks
		self.milage = milage
		self.milage += milage


class Car(Vehicle):
	def __init__(self, staring, doors, engine, breaks, milage):
		Vehicle.__init__(self,engine, breaks,milage)
		self.staring=staring
		self.doors=doors


vehicle=Car("normal",4,"petrol", "air", 12)
print(vehicle.engine)
print(vehicle.breaks)
print(vehicle.milage)
print(vehicle.staring)
print(vehicle.doors)

# Use super().


class Vehicle:
	def __init__(self, engine, breaks, milage):
		self.engine = engine
		self.breaks = breaks
		self.milage = milage



class Car(Vehicle):
	def __init__(self, staring, doors, engine, breaks, milage):
		super().__init__(engine, breaks,milage)
		self.staring=staring
		self.doors=doors



vehicle=Car("normal",4,"petrol", "air", 12)
print(vehicle.engine)
print(vehicle.breaks)
print(vehicle.milage)
print(vehicle.staring)
print(vehicle.doors)

print("//////////////////////////////////")

class Vehicle:
	def __init__(self, engine, breaks, milage):
		self.engine = engine
		self.breaks = breaks
		self.milage = milage
		self.milage += milage


class Car(Vehicle):
	def __init__(self, staring, doors, engine, breaks, milage):
		super().__init__(engine, breaks,milage)
		self.staring=staring
		self.doors=doors
		self.milage-=milage
class Bike(Car):
	def __init__(self,staring,doors, engine, breaks, milage, cc=20):
		super().__init__(staring,doors,engine, breaks, milage)
		self.cc=cc

class Truck(Vehicle):
	def __init__(self, engine, breaks, milage, tyres):
		super().__init__(engine, breaks, milage)
		self.tyres=tyres




vehicle=Car("normal",4,"petrol", "air", 12)
print(vehicle.engine)
print(vehicle.breaks)
print(vehicle.milage)
print(vehicle.staring)
print(vehicle.doors)

print("//////////////////////////////////")

my_bike=Bike("self","none","petrol", "Disc", 60,)
print(my_bike.milage)
print("//////////////////////////////////")
my_truk=Truck("self","Air",60, 10)
print(my_truk.milage)


