# if <codition>:
# <operations>
# elif:
# <opreations>
# else:
# <operations>

# comparison operators
# < > <= >= == !=

a = 10
b = 20
print(a != b)

a = int(input("Enter the value of a:"))
if a>10:
  print("The value you entered is greater than ten")
else:
  print("The value you entered is less than 10")

a = int(input("Enter the value of a:"))
if a>0:
  print("The value is positive")
elif a<0:
    print("Value is negative ")
else:
  print("The value you entered is 0")

a = int(input("Enter a = "))
b = int(input("Enter b = "))
if a>b:
  print("a is greater than b")
elif b>a:
  print("b is greater than a ")
else:
  print("a and b are equal")

a = int(input("Enter a value:\n"))
if a % 2 == 0:
  print("The number is even")
else:
  print("The number is odd")

a = int(input("value of a:\n"))
b = int(input("value of b:\n"))
o = input("Enter operator:\n")
if o == '+':
  print(a + b)
elif o == '-':
  print(a -b)
elif o == '*':
  print(a * b)
elif o == '/':
  print(a / b)
else:
  print("Enter a valid operator")

# logical operators
# & --> and
# | --> or

a = int(input("value of a:\n"))
b = int(input("value of b:\n"))
o = input("Enter operator:\n")
if o == '+':
    print(a + b)
elif o == '-':
    print(a - b)
elif o == '*':
    print(a * b)
elif (o == '/') and (b != 0):
    print(a / b)
elif (o == '/') and (b == 0):
    print("Value of b cannot be 0")
else:
    print("Enter a valid operator")