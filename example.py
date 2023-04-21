from setup import command_bus

class Car():
    def __init__(self, make, model):
        self.make = make
        self.model = model

class Bike():
    def __init__(self, gears):
        self.gears = gears

print(command_bus.handle(Bike(21))) # Bike
print(command_bus.handle(Car('Renault', 'Megane')))


