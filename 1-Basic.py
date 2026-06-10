# Class is a bLueprint
# __init__    =is a special method used to define the initial state of an object
# Elements inside the __init__ method is called Parameters
# self.brand,self.ram,self.storage,self.colour these are the Attributes of an Object right side of
# these attributes are the valuse of the attributes .
# attributes are the indipendent for the different object
class Laptop:
    def __init__(self,brand,ram,storage,colour):
        self.brand=brand
        self.ram=ram
        self.storage=storage
        self.colour=colour

# object creation
# here option_1 is the object (Instance)
Option_1=Laptop("6gb","500gb","black","t")
print(Option_1.brand, Option_1.ram, Option_1.storage, Option_1.colour)