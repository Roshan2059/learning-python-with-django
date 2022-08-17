# WAP to create a billing system using list inside list
bill = []
n = int(input("Enter n = "))
for i in range(n):
    name = input("Enter name = ")
    price = int(input("Enter price = "))
    quantity = int(input("Enter quantity = "))
    total = price*quantity
    s = [name,price,quantity,total]
    bill.append(s)
    
print(bill)

a = [['Ram',34,'Kathmandu'],
     ['Shyam',31,'Bhaktapur'],
     ['Sabin',35,'Lalitpur']]
name = input('Enter name = ')
for i in a:
    if name in i:
        print(i)

a = [[1,2,3],
    [4,5,6],
    [7,8,9]]
a[1][2]

a = [['Ram',34,'Kathmandu'],
     ['Shyam',31,'Bhaktapur'],
     ['Sabin',35,'Lalitpur']]
name = input('Enter name = ')
# a = ['Ram',34,'Kathmandu']
for i in a:
    if name in i:
        print(i)

#  ['Sabin',35,'Lalitpur'] == "Ram"

#Update
a = [['Ram',34,'Kathmandu'],
     ['Shyam',31,'Bhaktapur'],
     ['Sabin',35,'Lalitpur']]
a[0] = ['Ramprasad', 54, 'Kathmandu']
a

a = [['Ram',34,'Kathmandu'],
     ['Shyam',31,'Bhaktapur'],
     ['Sabin',35,'Lalitpur']]
a[0][0] = 'Ramprasad'
a

a = [['Ram',34,'Kathmandu'],
     ['Shyam',31,'Bhaktapur'],
     ['Sabin',35,'Lalitpur'],
    ['Ram',34,'Kathmandu']]
name = input("Enter name = ")
for i in a:
    if name in i:
        a.remove(i)
        
print(a)

# m = [[1,2,3],[4,5,6]]        
# WAP to create a matrix
m = []
r = int(input("Enter row = "))
c = int(input("Enter column = "))
for i in range(r):
    y = []
    for j in range(c):
        x = int(input("Enter x = "))
        y.append(x)
    m.append(y)
print(m)