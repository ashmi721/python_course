'''override'''

# Base class
class Vehicle:
    def __init__(self, cost, engine_type):
        self.cost = cost
        self.engine_type = engine_type

    def show_Vehicle(self):
        print(f"the cost of the vehicle is: {self.cost}")
        print(f"the engine_type of the vehicle is: {self.engine_type}")
v1 = Vehicle(234000,"Petrol")

# Base class
class Car(Vehicle):
  def __init__(self,cost,engine_type,tyres):
    super().__init__(cost,engine_type) # overrid the base class
    self.tyres=tyres
    self.show_car_details()

  def show_car_details(self):
    print("Number of tyres in car is :",self.tyres)
    print("I am Car base class")

c1 = Car(1450000,"Electric",4)  
c1.show_Vehicle()   