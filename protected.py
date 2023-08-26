# program to illustrate protected access modifier in a class
class Student:
#create a constructor
  def __init__(self,name,roll,branch):
 # declare a protected attribute
    self._name = name
    self._roll = roll
    self._branch = branch

# protected member function
  def _displayRollAndBranch(self):
# accessing protected data members
      print("Roll: ", self._roll)
      print("Branch: ", self._branch)

class School(Student):
  def __init__(self,name,roll,branch):
    Student.__init__(self,name,roll,branch)
# public member function
  def displayDetails(self):
# accessing protected data members of super class
     print("Name: ", self._name)


obj1 = Student("ashmita",2,"Information Technology")
obj2 = School("asus",2,"civil")
# accessing protected member functions of super class
obj1._displayRollAndBranch()
obj2.displayDetails()