# Q. Write a python program to create abstract class with method start(). Create another 2 class Car and Truck inherited from Abstract Class with the implementation of abstract method.
# Create a Abstract Base Class named "Vehicle"

from abc import ABC, abstractmethod

class Vehicle(ABC):

  @abstractmethod
  def start(self):
    pass

class Car(Vehicle):
  def start(self):
    print("Car is started")

class Truck(Vehicle):
  def start(self):
    print("Truck is started")

obj1 = Car()
obj2 = Truck()    


obj1.start()
obj2.start()