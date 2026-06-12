class Vehicle:
    def __init__(self, milage, tyre, door):
        self.milage = milage
        self.tyre = tyre
        self.door = door

    def cal_milage(self):
        return self.milage * self.tyre


class Employee:
    def __init__(self, name, vehicle):
        self.name = name
        self.vehicle = vehicle   # Aggregation


me = Vehicle(12, 4, 4)

you = Employee("Shreyas", me)

print(you.name)
print(you.vehicle.milage)
print(you.vehicle.cal_milage())