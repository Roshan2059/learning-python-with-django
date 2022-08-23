# day13

#tuple:
# indexed
# ordered
# duplicated value
# immutable
# no append() insert() pop()
# no del remove because this is an immutable data type
# no update()
# no clear()
# no copy()
# no fromkeys()
# no index()
# no count()
# no sort()
# no reverse()
# no extend()
# a = ("apple",)
# print(a)

# tuple inside tuple:
# a = ((1,2,3),(4,5,6),(7,8,9))
# print(a)

# # converting tuple into list inside list
# a = (("ram",23,"kathmandu"),("ram",23,"kathmandu"),("ram",23,"pokhara"),("ram",23,"birgung"),("ram",23,"kathmandu"))
# l = []
# for i in a:
#   x = list(i)
#   l.append(x)
# print(l)

# # Tuple
# -Indexed
# -Ordered
# -Multiple and duplicate values
# -Imutable

a = (1,2,3,4)
print(type(a))
print(a)

a = (1, 2, 3, 4)
print(a[0])
print(a[0:3])

a = (1,2,3,4,5,)
b = (6,7,8,9)
c = a+b
print(c)

# no append() insert() extend()
# no update
# no del pop() remove
#no sort()

a = ('Apple',)
print(a)
print(type(a))

a = (1, 2, 3, 4, 5, 6, 7, 8, 9,)
b = list(a)
b

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
b = tuple(a)
b

b = "Apple"
list(b)

a = ()
b = "Apple"
c = a+(b,)
c

t = tuple()
n = int(input("Enter n = "))
for i in range(n):
    x = int(input("Enter x = "))
    t = t+(x,)
    
print(t)

a = (1, 2, 3, 4, 5, 6, 7, 8, 9,)
a = list(a)
a

del a[0]

tuple(a)

#Tuple inside tuple
a = ((1,2,3),(4,5,6),(7,8,9))
a



t = tuple()
n = int(input("Enter n = "))
for i in range(n):
    name = input("Enter name = ")
    age = int(input("Enter age = "))
    add = input("Enter add = ")
    
    t = t+((name,age,add),)
    
print(t)

a = (('Ram', 34, 'Kathmandu'), ('Shyam', 78, 'Kathmandu'))
l = []
for i in a:
    x = list(i)
    l.append(x)
    
print(l)

a = [['Ram', 34, 'Kathmandu'], 
     ['Shyam', 78, 'Kathmandu']]
t = ()
for i in a:
    x = tuple(i)
    t = t+(x,)
    
t

# WAP to create matrix using tuple inside tuple

m = ()
r = int(input("Enter row = "))
c = int(input("Enter column = "))
for i in range(r):
    y = ()
    for j in range(c):
        x = int(input("Enter x = "))
        y = y+(x,)
    m = m +(y,)
print(m)

a = ((234, 456, 34), (567, 345, 56), (456, 678, 24))
for i in a:
    print(i)