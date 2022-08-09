# write a program to create a calculator using function

# def calc(a,b,o):
#     if o == "+":
#         result = a + b
#         print(result)
#     elif o == "-":
#         result = a - b
#         print(result)
#     elif o == "*":
#         result = a * b
#         print(result)
#     elif o == "result":
#         result = a / b
#         print(result)
#     elif o == "":
#         print("Please enter an operator")
#     else:
#         print("Invalid operator")

# a = int(input("Enter first number : "))
# b = int(input("Enter second number : "))
# c = input("Enter operator(+, -, *, /) : ")
# calc(a,b,c)

# billing system using function with grand total:

# Requirement analysis and specification:
#     billing system where number of item, price of item and quantity of item is given by user and grand total amount is calculated and displayed as output.

# Design:
#     total = price * quantity
#     gtotal = gtotal + total
# no. of product, price and quantity enter garna lagaune

# Coding:

def bill(n):
    total = 0
    gtotal = 0
    for i in range(n):
      name = input("Enter name of item : ")
      price = int(input("Enter price of product : "))
      quantity = int(input("Enter quantity of product : "))
      total = (price * quantity)
      gtotal = gtotal + total
    print("Grand total is: ", gtotal)

n = int(input("Enter number of items : "))
bill(n)