class Car:
    
    model = "Civic"
    
    def __init__(self, color, type):
        self.color = color
        self.type = type
        self.started = False
        self.stopped = False
        
    def start(self):
        print("Car started")
        self.started = True
        self.stopped = False
    
    def stop(self):
        print("Car stopped")
        self.started = False
        self.stopped = True
        
class Sedan(Car):
    def __init__(self, color, type, seats):
        super().__init__(color, type)
        self.seats = seats
        
class ElectricSedan(Sedan):
    def __init__(self, color, type, seats, range_km):
        super().__init__(color, type, seats)
        self.range_km = range_km
    
        
my_car1 = Car("blue", "sedan")
my_car2 = Car("red", "hatchback")
my_car3 = Sedan("red", "hatchback", 5)
my_car4 = ElectricSedan("red", "hatchback", 5, 500)
print(my_car1.color)
print(my_car1.model)

print(my_car2.color)
print(my_car2.model)

print(my_car3.color)
print(my_car3.model)
print(my_car3.seats)

print(my_car4.color)
print(my_car4.model)
print(my_car4.seats)
print(my_car4.range_km)

my_car4.start()