data = [3, 56, 67, 45, 34, 6, 7, 8]
l = [i for i in data if i % 2 == 0]
print(l)

data = ['Apple', 'ball', 'cat', 'Dog']
l = [i for i in data if i[0].isupper()]
print(l)

data = {i: i**2 for i in range(1, 10)}
print(data)

data = ['AppLE', 'BAll', 'caT', 'alskd']
d = {i: i.lower() for i in data}
list(d.values())

import datetime

x = datetime.datetime.now()
z = int(input("Enter number"))
y = datetime.datetime.now()
print(y - x)

x = datetime.datetime.now()
print(x.strftime("%c"))

import os

os.listdir()
os.mkdir('NewFolder')

import pandas as pd
data = {'Name':['Ram','Shyam','Hari'],
       'Age':[45,67,89],
       'Add':['Kathmandu','Bhaktapur','Lalitpur']}

df = pd.DataFrame(data)
df.to_json('new_csv.json')
df