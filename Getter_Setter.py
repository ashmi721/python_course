class Vehicle:
  def __init__(self,name):
    self._name = name


  def display(self):
    print(f"Name of the Vehicle is {self._name}")

    @property
    def access_name(self):
      return self._name

    @access_name.setter
    def access_name(self):
      # self._name = name
      pass

obj = Vehicle("car")
obj.access_name = "Bike"
print(f"after setting Name of the vehicle is {obj.access_name}")
obj.display()