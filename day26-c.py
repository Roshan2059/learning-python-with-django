# exception handling:
try:
    pass
except:
    pass
try:
    x = int(input('x = '))
except:
    print('Enter only int values')

try:
  a = int(input('Enter a = '))
  b = int(input('Enter b = '))
  c = a/b

except:
  print('Error!')

else:
  print(c)

# What if we want to perform the calculation again after the error
# Just put the function inb the except block
def cal():
    try:
        a = int(input('Enter a = '))
        b = int(input('Enter b = '))
        c = a / b

    except:
        print('Error!')
        cal()

    else:
        print(c)

try:
    a = int(input('Enter a = '))
    b = int(input('Enter b = '))
    c = a / b
    print(c)
except ZeroDivisionError:
    print('Error! value of b cannot be zero')
except ValueError:
    print('Error! values should be of integer form')

# raise statement:
raise ZeroDivisionError

try:
    a = int(input("Enter a = "))
    b = int(input("Enter b = "))
    if b ==0:
        raise ZeroDivisionError
    else:
        c = a/b

except ZeroDivisionError:
    print("Error! value of b can not be zero")

except ValueError:
    print("Error! value of a and b should be int")
    
#assert statement:
# a = 10
# assert a < 5

try:
    a = int(input('Enter x = '))
    assert a % 2 == 0
except:
    print('X is not even')