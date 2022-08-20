# Dictionary
# -Indexed
# -Ordered
# -Multiple data
# -Mutable

# d = {<key>:<value>,<key>:<value>,key>:<value>}

a = {'a':'Apple','b':'Ball','c':'Cat'}
print(a)

print(a['c'])
print(len(a))

a = {'a':'Apple','b':'Ball','c':'Cat'}
b = {'d':'dog'}
c = a+b
print(c)

a = {'a':'Apple','b':'Ball','c':'Cat'}
print(a*2)

a = {'a':'Apple','b':'Ball','c':'Cat'}
for i in a:
    print(i)

a = {'a':'Apple','b':'Ball','c':'Cat'}
for i in a.values():
    print(i)

a = {'a':'Apple','b':'Ball','c':'Cat'}
for i in a.items():
    print(i)

a = {'a':'Apple','b':'Ball','c':'Cat'}
b = []
for i in a.items():
    b.append(i)
    
b

dict(b)

a = dict()
print(a)

d = {'a': 'Apple', 'b': 'Ball', 'c': 'Cat'}
d['a'] = 'Ant'
d

d = {1: 'Apple', 0: 'Ball', 100: 'Cat'}
d

d = {'a': 'Apple', 'b': 'Ball', 'c': 'Cat'}
d['f'] = 'Fish'
d

d = {}
d['a'] = 'Apple'
d['b'] = 'Ball'
d['c'] = 'Cat'
d

d = {}
n = int(input("Enter n = "))
for i in range(n):
    name = input("Enter name = ")
    phone  = int(input("Enter phone = "))
    d[name] = phone
    
print(d)

d = {'Ram': 9878778765, 'Shyam': 9808667643}
d['Ram'] = 98086678665
d

d = {'Ram': 9878778765, 'Shyam': 9808667643}
del d['Ram']
print(d)

d = {'Ram': 9878778765, 'Shyam': 9808667643}
x = d.pop('Ram')
print(d)
print(x)

d = {['Ram']: 9878778765, ['Shyam']: 9808667643}
d

d = {('Ram',): 9878778765, ('Shyam',): 9808667643}
d

#List inside dictionary
d = {'Ram':[980866765,980778765],'Shyam':[9867556543,9808556543]}
d

info = {'Name':['Ram','Shyam'],'Age':[89,76],'Address':['Kathmandu','Lalitpur']}
info['Name']

info = {'Name':['Ram','Shyam'],'Age':[89,76],'Address':['Kathmandu','Lalitpur']}
info['Name'][0]

info = {'Name':[],'Age':[],'Address':[]}
n = int(input("Enter n = "))
for i in range(n):
    name = input("Enter name = ")
    age = int(input("Enter age = "))
    add = input("Enter add = ")
    info['Name'].append(name)
    info['Age'].append(age)
    info['Address'].append(add)
    
print(info)