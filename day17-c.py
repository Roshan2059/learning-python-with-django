# day17

try:
  b = open('data.txt','x')
  b.close()
except:
  print('File already exists')

b =  open('data.txt','r')
x = b.read()
print(x)
b.close()

y = x.split('\n')
print(y)

a = open('data1.txt','x')
a.close()

with open('data1.txt','w') as b:
  b.write('I am Roshan')

# It is same as b = open('data1.txt','w') but if we write the with syntax then we should not have t0 write close function

b = open('data2.txt','w')
b.write('Hello world! Its Roshan')
b.close()

bill = ''
n = int(input('Enter n = '))
for i in range(n):
  name = input('Enter name = ')
  price = int(input('Enter price = '))
  quantity = int(input('Enter quantity = '))
  total = price * quantity
  data = f"{name} {price} {quantity} {total}\n"
  bill = bill+data
print(bill)

b = open('bill.txt','w')
b.write(bill)
b.close()

bill = ''
n = int(input('Enter n = '))
for i in range(n):
  name = input('Enter name = ')
  price = int(input('Enter price = '))
  quantity = int(input('Enter quantity = '))
  total = price * quantity
  data = f"{name},{price},{quantity},{total}\n"
  bill = bill+data
print(bill)

b = open('bill.csv','w')
b.write(bill)
b.close()