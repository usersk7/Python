class Car:
    def __init__(self):
        print("Car class")

    def wheel(self):
        print("Car have 4 wheel")
    
    def engie(self):
        print("Power is 200hp")

class Truck:
    def __init__(self):
        print("Truck class")

    def wheel(self):
        print("Truck have 6 wheel")
    
    def engie(self):
        print("Power is 500hp")

# common interface
def vehical(vh):
    vh.wheel()
    vh.engie()

#instantiate objects
carobj = Car()
vehical(carobj)

truckobj = Truck()
vehical(truckobj)