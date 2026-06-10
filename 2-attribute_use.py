class Dog:
    def __init__(self,name,age,height):
        self.name=name
        self.age=age
        self.height=height


# using the attribute inside the class

        print(self.name)


my_dog=Dog("Piya",4,"5ft")


# using the attribute outside the class

print(my_dog.name)