# day7

# def <function_name>():
#   <operation>

# function_name()

# def hello():
#   print("Hello world")
# hello()

# def cal():
#     p = int(input("Enter p = "))
#     t = int(input("Enter t = "))
#     r = int(input("Enter r = "))
#     i = p * t * r / 100
#     print(int(i))

# cal()

# Two types of functions:
# pre-defined function
# user-defined function

# function without argument and non return type
# function with argument and return type
# function without argument and return type
# function with argument and non return type

# All the above written functions are function without argument and non return type

# function with argument and no return type
# def area(l,b):
#   a = l*b
#   print("The area is: ",a)
# area(10,2)

# def info(name,age,add):
#   data = "Hello world my name is "+ name + " I am " + age + 
#   " years old " + " and I currently live in " + add

# name = input("Enter name:")
# age = input("Enter age:")
# add = input("Enter address:")

# info(name,age,add)

# def area(x,y):
#   a = x*y
#   print(a)
# def volume(x,y,z):
#   v = x*y*z
#   print(v)

# area(10,20)
# volume(10,20,30)

# write a program to create a calculator using function

def calc(a,b,o):
  if o == "+":
    print(a+b)
  elif o == "-":
    print(a-b) 
  elif o == "*":
    print(a+b) 
  elif o == "/":
    print(a+b)
  elif o == " " & o != "+,-,*,/":
    print("Enter a valid operator")
  else o == " "

a = int(input("Enter the first number:"))
b = int(input("Enter the second number:"))
c = input("Enter the operator:")