# wap to print circumference of circle to call the instance method
class Circle:
  pi = 3.14
  def __init__(self,radius):
    self.radius = radius
  def get_circumference(self):
    print(f"this is the circumference of circle {2 * self.pi * self.radius}")
obj = Circle(4)
obj.get_circumference()


# wap to print circumference of circle to call the class method
# class Circle:
#   pi = 3.14
#   def __init__(self,radius):
#     self.radius = radius

#   def get_circumference(self):
#    circumference = 2 * Circle.pi * self.radius
#    return circumference
#   # def set_radius(self,radius):
#   #   self.radius = radius
# obj = Circle(4)
# area = obj.get_circumference()

# print(area)