# Set
# -No indexing
# -No duplicate data
# -Unordered
# -Mutable

s = {1,2,3,4}
print(type(s))

s = {"Apple","Ball","Cat","Dog"}
print(s)

s = {1,1,2,3,4,5,6,7,5,6}
s

s = {"Apple","Ball","Cat","Dog"}
print(s[0])

s = {"Apple","Ball","Cat","Dog"}
for i in s:
    print(i)

s = {1}
type(s)

s = set()
n = int(input("Enter n = "))
for i in range(n):
    x = input("Enter x = ")
    s.add(x)
s

a = {'Apple', 'Ball', 'Cat'}
b = {'Fish'}
a.update(b)
print(a)

l =[1,1,2,3,4,5,6,7,5,6]
list(set(l))

ms = {'Ram','Gates','Jack','Jhon','Nabin','Sarita'}
apple = {'Jack','Jobs','Nabin','Ram','Sandesh','Mukesh'}

ms.intersection(apple)

ms.union(apple)

ms = {'Ram','Gates','Jack','Jhon','Nabin','Sarita'}
apple = {'Jack','Jobs','Nabin','Ram','Sandesh','Mukesh'}
ms - apple

ms.difference(apple)

ms = {'Ram','Gates','Jack','Jhon','Nabin','Sarita'}
apple = {'Jack','Jobs','Nabin','Ram','Sandesh','Mukesh'}
apple.difference(ms)

U = {'Gates','Jack','Jhon','Jobs','Mukesh','Nabin','Ram','Sandesh','Sarita','Hari','Sunita'}

ms = {'Ram','Gates','Jack','Jhon','Nabin','Sarita'}
apple = {'Jack','Jobs','Nabin','Ram','Sandesh','Mukesh'}

un = ms.union(apple)
U-un

a = {['Ram','Gates','Jack'],['Jhon','Nabin','Sarita']}
print(a)

a = {('Ram','Gates','Jack'),('Jhon','Nabin','Sarita')}
print(a)

a = {('Ram','Gates','Jack'),('Jhon','Nabin','Sarita')}
print(a)

ms = {'Ram','Gates','Jack','Jhon','Nabin','Sarita'}
apple = {'Jack','Jobs','Nabin','Ram','Sandesh','Mukesh'}
google = {'Ram'}
ms.intersection(google,apple)

ms = {'Ram','Gates','Jack','Jhon','Nabin','Sarita'}
apple = {'Jack','Jobs','Nabin','Ram','Sandesh','Mukesh'}
google = {'Ram'}
ms.union(apple,google)