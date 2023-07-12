# Q.1 Write a python function to multiply all the numbers in a list
def multiply(n):
  mul = 1
  for item in list1:
    mul*=item
  print(f"The multiply of all the number in a list {mul}")
list1 = [2,3,4,5]
multiply(list1)   



# Q.2 Write a python function to find factorial of a given non negativenumber
# def fact(n):
#   f = 1
#   for i in range(1,n+1):
#       f *=i
#   print(f"The factorial of {n} is: {f}")

# user_input = int(input("enter the positive number:"))  

# fact(user_input)

# Q.3 Write a python function to reverse a string
# def rev_str(string):
#     return string[::-1]
# rev = rev_str("Hello World!")
# print(rev)


# Q.4 Write a python function that accepts a string and calculate the number of upper case letters and lower case letters
# def calc_letter_case(string):
#    upper_letter = 0
#    lower_letter = 0
#    for char in string:
#     if char.isupper():
#       upper_letter+=1
#     elif char.islower():
#       lower_letter += 1
#    print(f"Number of upper_letter:{upper_letter}\nNumber of lower_letter:{lower_letter}")

# user_str = input("Enter the string:")
# calc_letter_case(user_str)

# Q.5 Write a python function that takes a list and returns a new list with unique elements of the first list
def unique_list():
  list1 = [1,1,2,3,5,6,7,3,"hello",6]
  new_list = list(set(list1))
  print(f"the new list is : {new_list}") 
unique_list()

# Q.6 Write a Python function that takes a number as a parameter and check the number is prime or not.
# def check_prime(number):
#   count = 0
#   for i in range(1,number+1):
#     if number%i==0:
#      count+=1
#   if count==2:
#      print(f"Number {number} is prime")
#   else:
#       print(f"Number {number} is not prime")

# user_input = int(input("Enter the positive number:")) 
# check_prime(user_input)    

# Q.7 Write a python function to print the even numbers from a given list
# def print_even(number):
#   even_num = [item for item in number if item%2==0]
#   print(f"List of even number {even_num}")
# input_list = [1,2,4,5,7,6,8]
# print_even(input_list)  