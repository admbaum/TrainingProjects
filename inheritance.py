class Vehicle:  #  This is the base class
    def __init__(self, VIN, weight, manufacturer):  #  Class constructor method that expects VIN, weight, manufacturer
        self.vin_number = VIN
        self.weight = weight
        self.manufacturer = manufacturer

    def getweight(self):  #  Getter method to get weight
        return self.weight

    def getmanufacturer(self):
        return self.manufacturer

    def vehicletype(self):
        pass


class Car(Vehicle):  #  class that inherits from Vehicle
    def __init__(self, VIN, weight, manufacturer, seats):
        self.vin_number = VIN
        self.weight = weight
        self.manufacturer = manufacturer
        self.seats = seats

    def numberofseats(self):
        return self.seats

    def vehicletype(self):
        return 'Car'


class Truck(Vehicle):  #  Another class that inherits from Vehicle
    def __init__(self, VIN, weight, manufacturer, capacity):
        self.vin_number = VIN
        self.weight = weight
        self.manufacturer = manufacturer
        self.capacity = capacity

    def transportcapacity(self):
        return self.capacity

    def vehicletype(self):
        return 'Truck'


a = Car('ABC', 1000, 'BMW', 4)
b = Truck('ADD', 1000, 'MAN', 10000)
c = Car('DEF', 1200, 'Ford', 4)
d = Truck('asfd', 11000, 'Mercedes', 15000)

print(a.getweight(), b.getmanufacturer(), c.numberofseats(), d.transportcapacity())

