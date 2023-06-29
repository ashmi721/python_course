#1. wap to create a biling system (product,price,aulity,total,all_total)
def clc_billing_system():
  name = input("Enter your name: ")
  print(f"Welcome Mr\Mrs {name}")

  all_total = 0
  try:
   product_num = int(input("Enter the number of product:"))
   for i in range( product_num):
      product = input("Enter the product name: ")
      price = int(input("Enter the price: "))
      quantity = int(input("Enter the quantity:"))
      total = price * quantity
      print(f"You buy the {quantity} {product}RS.{price} is {total}")
      
      all_total +=total
   print(f"Your total bill is :{all_total}")   
  except ValueError:
      print("Error:invalid literal for int() with base 10: 'a' !Please enter the number")
clc_billing_system()