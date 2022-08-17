# append() insert() extend()

a = []
a.append('Apple')
a.append('Ball')
a.append('Cat')
print(a)

a = []
n = int(input("Enter n = "))
for i in range(n):
    x = input("Enter x = ")
    a.append(x)
    
print(a)

a = ['Apple', 'Ball', 'Cat']
a.insert(1,'Ant')
print(a)

a = ['Apple', 'Ball', 'Cat']
b = ['Dog','Fish']
a.extend(b)
print(a)

# Update
a = ['Apple', 'Ball', 'Cat', 'Dog', 'Fish']
a[0] = 'Ant'
a

# del remove() pop()

a = ['Apple', 'Ball', 'Cat', 'Dog', 'Fish']
del a[0]
print(a)

a = ['Apple', 'Ball', 'Cat', 'Dog', 'Fish']
del a[0:4]
a

a = ['Apple', 'Ball', 'Cat', 'Dog', 'Fish']
a.remove('Apple')
a

a = ['Apple', 'Ball', 'Cat', 'Dog', 'Fish','Apple']
a.remove('Apple')
a

a = ['Apple', 'Ball', 'Cat', 'Dog', 'Fish','Apple']
c = a.count('Apple')
for i in range(c):
    a.remove('Apple')
print(a)

a = ['Apple', 'Ball', 'Cat', 'Dog', 'Fish']

a.index('Apple')

a = ['Apple', 'Ball', 'Cat', 'Dog', 'Fish','Apple']

for i in range(len(a)):
    if a[i] == 'Apple':
        print(i)

a = ['Apple', 'Ball', 'Cat', 'Dog', 'Fish','Apple']
a.pop()
a

a = ['Apple', 'Ball', 'Cat', 'Dog', 'Fish','Apple']
b = a.pop(3)
print(b)

a = "Apple 3 200 600\nBanana 2 100 200"
print(a)

x = a.split('\n')
x

# List inside list
a = [[1,2,3],
     [4,5,6],
     [6,7,8]]
print(a)
print(type(a))
print(len(a))

info = [['Ram',34,'Kathmandu'],
        ['Shyam',67,'Lalitpur'],
        ['Hari',67,'Bhaktapur']]


data = []
a = "Apple 3 200 600\nBanana 2 100 200"
x = a.split('\n')
print(x)
x[1].split()

data = []
a = "Apple 3 200 600\nBanana 2 100 200"
x = a.split('\n')
for i in x:
    y = i.split()
    data.append(y)
    
print(data)