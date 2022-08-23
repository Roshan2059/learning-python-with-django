# dictionary inside list
a = [{'Name':'Ram','Age':34,'Add':'Kathmandu'},
    {'Name':'Shyam','Age':56,'Add':'Bhaktapur'},
    {'Name':'Hari','Age':89,'Add':'Lalitpur'}]

print(a[0])

b = {'Name':'Hari','Age':89,'Add':'Lalitpur'}
a.append(b)
print(a)

info = []
n = int(input("Enter n = "))
for i in range(n):
    name = input("Enter name = ")
    age = int(input("Enter age = "))
    add = input("Enter add = ")
    data = {'Name':name,'Age':age,'Add':add}
    info.append(data)
    
print(info)

a = [{'Name': 'Ram', 'Age': 45, 'Add': 'Kathmandu'}, 
     {'Name': 'Shyma', 'Age': 89, 'Add': 'Kathmandu'}, 
     {'Name': 'Nabin', 'Age': 23, 'Add': 'Lalitpur'}]
a[0] = {'Name': 'Rama', 'Age': 25, 'Add': 'Bara'}
a

a = [{'Name': 'Ram', 'Age': 45, 'Add': 'Kathmandu'}, 
     {'Name': 'Shyma', 'Age': 89, 'Add': 'Kathmandu'}, 
     {'Name': 'Nabin', 'Age': 23, 'Add': 'Lalitpur'}]
a[0]['Name'] = 'Rama'
a

# dict inside dict
d = {1:{'Name':'Ram','Per':80,'Pos':2},
    2:{'Name':'Shyam','Per':60,'Pos':20},
    3:{'Name':'Nabin','Per':78,'Pos':5}
    }
print(d)

d = {}
# d[<key>] = {<key>:<velue>}
d[1] = {'Name': 'Ram', 'Per': 80, 'Pos': 2}
d[2] = {'Name': 'Shyam', 'Per': 60, 'Pos': 20}
d

d = {'sn':[],'name':[],'category':[]}

# WAP to create dict inside dict
d = {}
n = int(input("Enter n = "))
for i in range(1,n+1):
    name = input("Enter name = ")
    per = int(input("Enter per = "))
    pos = int(input("Enter pos = "))
    d[i] = {'Name':name,'Per':per,'Pos':pos}
    
print(d)

d = {'sn':[1,2],
     'name':['Coke','Momo'],
     'quantity':[3,3],
     'price':[200,150],
     'total':[600,450]}




{1: {'Name': 'Ram', 'quantity': 78, 'price': 2,'total':600},
 2: {'Name': 'Hari', 'quantity': 78, 'price': 2,'total':600}}
