'''Create a python program capable of greeting you with good morning, good afternoon, and good evening,
Your program should use time module to get the current hour.'''

import time
timestamp = time.strftime("%I:%M:%S")
print(timestamp)

timestamp = int(time.strftime("%I"))
print("Hour:",timestamp)
timestamp = int(time.strftime("%M"))
print("Minute:",timestamp)
timestamp = int(time.strftime("%S"))
print("Second:",timestamp)

name = input("Enter your name: ")
if(timestamp > 0 or timestamp < 12 ):
    print( "Good Morning", name)
elif(timestamp >= 12 or timestamp <=6):
    print("Good afternoon", name)
else:
    print("Good evening", name)    

