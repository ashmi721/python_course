class Vehicle:
  is_electric = False # class attribute

# create object
obj = Vehicle()

# access attibute using class name'
print(Vehicle.is_electric)

# modify class attributes
Vehicle.is_electric = True


# create a class name  people with atleast 1 instance attribute
class people:
  a = 10 # class attribute
  @classmethod
  def display(value): # create a class method
    print(f"this is the class method {value.a}")

# instance attribute
  def __init__(self,name,age):
    self.name = name
    self.age = age

# instance method
  def display_instance_method(self):
     print(f"this is the instance method where as age is  {self.age}")

# create a objects
obj1 = people("ashmita",17)
# object call the class method
obj1.display()
# object call the instance method
obj1.display_instance_method()
# call the instance attribute
obj1.name


''' create an class with 2 parameter '''
class Student:
  def detail(self,name,address):
    self.name = name
    self.address=address
  def show_detail(self):
    print (f"Name : {self.name}, Address : {self.address}")

s1 = Student()
s1.detail("ashmita","Dang")  
s1.show_detail()

print(" ---- ")

''' create class using constructor '''
class Employee:
  def __init__(self,name,age,salary,gender):
    self.name = name
    self.age = age
    self.salary = salary
    self.gender = gender

  def show_detail(self):
    print(f"Name of the employee is : {self.name}") 
    print(f"Age of the employee is : {self.age}") 
    print("salary of the employee is ",self.salary) 
    print("Gender of the employee is ",self.gender)

e1 = Employee("Jhon",32,40000,"Male")
e1.show_detail() 