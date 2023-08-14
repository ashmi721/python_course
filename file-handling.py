
"""
<h2> Exception Handling in python </h2>
File handling is important because the data is stored permanently in non-volatile memory

"""

#1. Zero division error exception handling

a = int(input("enter number 1: "))
b = int(input("enter number 2: "))
# try:
#   divisible = a/b
# except Exception as e:
#   print("Exception occured:",e)

# print("Hello world")

# write a program to handle the specify exception
try:
  divisible = a/b
except ZeroDivisionError:
  print("Error: num is not divisible by 0 ")

# 2. TypeError
a = 2
b = "2"
try:
 z = a + b
except Exception as e:
  print("Exception occured:",e)

# write a program to handle the specify exception
try:
 z = a + b
except TypeError:
 print("Error: cannot add an int and a str")

# 3. IndexError
try:
    even_numbers = [2,4,6,8]
    print(even_numbers[5])

except ZeroDivisionError:
    print("Denominator cannot be 0.")

except IndexError:
    print("Index Out of Bound.")

# 4. ValueError
try:
  n = int(input("Enter the num:"))
  for item in range(1,11):
    mul = n * item
except ZeroDivisionError:
    print("Denominator cannot be 0.")

except IndexError:
    print("Index Out of Bound.")

except Exception as e:
    print(e)
else:
   print(mul)

# NameError
try:
   a = int(input("enter the num1:"))
   b = int(input("enter the num2:"))

   division = a / b

except ZeroDivisionError:
    print("Denominator cannot be 0.")

except ValueError:
  print("can not be typecast str to int ")

except Exception as e:
  print(e)
else:
  print(division)

try:
  a = int(input("enter the num1:"))
  b = int(input("enter the num2:"))

  division = a / b
except ZeroDivisionError:
    print("Denominator cannot be 0.")

except ValueError:
  print("can not be typecast str to int ")

except Exception as e:
  print(e)

# Python program to handle simple runtime error
#Python 3

a = [1, 2, 3]
try:
	print ("Second element = %d" %(a[1]))

	# Throws error since there are only 3 elements in array
	print ("Fourth element = %d" %(a[2]))

except:
	print ("An error occurred")

"""<h3> Finaly keyword in python </h3>
The finally block will always be executed, no matter if the try block raises an error or not:
"""

# used finaly block

try:
   a = int(input("enter the num1:"))
   result = 10/a
   print("Result:",result)
except ValueError:
  print("Invalid input! please enter the valid number:")

except ZeroDivisionError:
    print("Denominator cannot be 0.")

finally:
  print("program executed complited")

# Raised keyword
def calc_square_root(number):
  if number < 0:
    raise ValueError("canot calculate square root of the negative number")
  else:
    return number ** 0.5

a = int(input("enter the num1:"))
result = calc_square_root(a)
print(result)

try:
 result = calc_square_root(a)
except ValueError as e:
   print("ValueError:",e)



# user_input = input("enter the age:")

# To Write the file in 
# f = open("data.txt",'w')
# f.write(user_input)
# f.close()

#To append the data
# with open("data.txt",'a') as f:
#  f.write(" Hello mrs. AShmita ")

# To Read the file
# f = open("data.txt",'r')
# print(f.read())
# f.close()

# To read the only 5 word
# f = open("data.txt",'r')
# print(f.read(5))
# f.close()

# To read the file in lines
# with open("data.txt",'r') as f:
#  print(f.readlines())


# To split the file data in the 
# with open("data.txt", "r") as file:
#     data = file.readlines()
#     for line in data:
#         word = line.split()
#         print (word)

 
# 1. The seek() funtion allows you to move the current position within a file to a specific point.
# with open("data.txt",'r') as f:
# # move to the 2th byte in the file    
#   f.seek(2)

  # To find the current position 
#   print(f.tell()) 
#   # to read the next 8byte
#   data = f.read(8)
#   print(data) 

  # When you open the file in write mode than you can use truncate() to specify the size of the file data
with open('data.txt','a') as f:
  f.write("I am a python developer")
  f.truncate(10)
  
with open('data.txt','r') as f:
 print(f.read())
  
import os
os.remove("demo.txt")
os.path.exists('demo.txt')
