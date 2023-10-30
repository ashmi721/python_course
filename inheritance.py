import math
# Base class
class Shape:
 def __init__(self,color,filled_status):
  self.color = color
  self.filled_status = filled_status

# derived class
class Rectangle(Shape):
  def __init__(self,color,filled_status,length,width):
    super().__init__(color,filled_status) # super is used to access the base class
    self.length = length
    self.width = width
  def calculate_area(self):
    return self.length * self.width

# derived class
class Circle(Shape):
  def __init__(self,color,filled_status,radius):
    super().__init__(color,filled_status)
    self.radius = radius
  def calculate_area(self):
    return math.pi * (self.radius **2)

obj1 = Rectangle("Black","true",2,3)
rect_area = obj1.calculate_area()

obj2 = Circle("Red","state",2)
circle_area= obj2.calculate_area()

print(f"Area of the rectangle: {rect_area}")
print(f"Area of the circle: {circle_area}")

print("-----------")

# Base class
class Vehicle:
    def __init__(self, cost, engine_type):
        self.cost = cost
        self.engine_type = engine_type

    def show_Vehicle(self):
        print(f"the cost of the vehicle is: {self.cost}")
        print(f"the engine_type of the vehicle is: {self.engine_type}")

v1 = Vehicle(234000,"Petrol")
v1.show_Vehicle()
# Child class
class Car(Vehicle):
    def __init__(self, cost, engine_type):
        super().__init__(cost, engine_type)  # Call the parent class constructor
        self.car_detail()

    def car_detail(self):
        print("I am a car")


c1 = Car(150000, "Electric")
c1.show_Vehicle()  # This line will print the vehicle details