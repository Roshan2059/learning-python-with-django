try:
    file = open('data.csv','x')
    file.close()
except:
    print("The file is already there ! ")

import pandas as pd
df = pd.read_csv('data.csv')
df

import pandas as pd
df = pd.read_csv('data.csv',nrows = 5,index_col = 'sn')
df

df['phone']

df[df['add'] == 'Bara']

data = df[df['age'] >50]
data

data.to_csv('new_data.csv')



data = df[(df['age'] >50) & (df['add']=='Patan')]
data

# DataFrame
import pandas as pd
data = {'Name':['Ram','Shyam','Hari'],
       'Age':[45,67,89],
       'Add':['Kathmandu','Bhaktapur','Lalitpur']}

df = pd.DataFrame(data)
df.to_csv('new_csv.csv')
df

import pandas as pd
df = pd.read_csv('data.csv',index_col = 'sn')
df

df.iloc[1:4]

import pandas as pd
df = pd.read_csv('data.csv',index_col = 'sn')
df.loc[2:5]

import pandas as pd
df = pd.read_csv('data.csv',index_col = 'name')
df.loc['Nabin':'Sabin']

