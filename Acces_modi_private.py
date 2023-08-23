# create a private variables
class Vehicle:

 def __init__(self,color):
  # create private attribute
  self.__color = color

  # to create a public method to access the private attribute
 def access_private(self):
   return self.__color

 # create a private method to reset color of privious color
 def __reset_color(self,color):
  self.__color = color

 # access private method inside the class to create a public method to access the reset private method
 def display_reset_color(self,color):
  self.__reset_color(color)
  print(f"color after reseting is: {self.__color}")


car = Vehicle("red")
# car.__color  (private atrribute can not be accesed)
private_var = car.access_private()
print(f"Access private variable: {private_var}")

car.display_reset_color("blue")
