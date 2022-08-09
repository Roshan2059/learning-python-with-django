# day8

# function with no argument and return type:
# def cal():
#   l = int(input("Enter l = "))
#   b = int(input("Enter b= "))
#   a = l * b
#   return a
# print(cal)

# def cal():
#   l = int(input("Enter l = "))
#   b = int(input("Enter b= "))
#   a = l * b
#   return a
# area = cal()
# print(area)

# def cal():
#   l = int(input("Enter l = "))
#   b = int(input("Enter b= "))
#   a = l * b
#   return a
# area = cal()
# print(area)
# h = int(input("Enter h = "))
# v = area * h
# print("The volume is = ",v)

# function with argument and return type:
# def cal(l,b):
#   a = l * b
#   return a

# l = int(input("Enter l = "))
# b = int(input("Enter b= "))
# area = cal(l,b)
# print("The required area is : ",area)

# def cal(l, b, h):
#     a = l * b
#     v = a * h
#     return a, v

# l = int(input("Enter l = "))
# b = int(input("Enter b= "))
# h = int(input("Enter h = "))
# c = cal(l, b, h)
# print(c)

# def cal(l, b, h):
#     a = l * b
#     v = a * h
#     return a, v

# l = int(input("Enter l = "))
# b = int(input("Enter b= "))
# h = int(input("Enter h = "))
# a, v = cal(l, b, h)
# print("The area is: ", a)
# print("The volume is: ", v)

# a = 10, 20
# print(a)

# x,y = a
# print(x)
# print(y)

# def add(a, b):
#     return a + b
# def sub(a, b):
#     return a - b
# def mul(a, b):
#     return a * b
# def div(a, b):
#     return a / b

# def cal():
#     a = int(input("value of a:\n"))
#     b = int(input("value of b:\n"))
#     o = input("Enter operator:\n")
#     if o == '+':
#         print(add(a, b))
#     elif o == '-':
#         print(sub(a, b))
#     elif o == '*':
#         print(mul(a, b))
#     elif o == '/':
#         print(div(a, b))
#     else:
#         print("Enter a valid operator")

# cal()

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

def cal():
    a = int(input("value of a:\n"))
    b = int(input("value of b:\n"))
    o = input("Enter operator:\n")
    if o == '+':
        print(add(a, b))
    elif o == '-':
        print(sub(a, b))
    elif o == '*':
        print(mul(a, b))
    elif o == '/':
        print(div(a, b))
    else:
        print("Enter a valid operator")
    x = input("Enter y for more calculation")
    if x == "y":
        cal()

cal()