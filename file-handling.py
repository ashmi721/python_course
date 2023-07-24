# File handling is important because the data is stored permanently in non-volatile memory
# user_input = input("enter the age:")
# 


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
