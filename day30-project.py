from bs4 import BeautifulSoup
import requests
url = BeautifulSoup('https://www.worldometers.info/coronavirus/', 'html.parser')
soup = requests.get(url)
soup

soup = soup.text


# !pip install lxml

code = BeautifulSoup(soup, "lxml")


code = code.table

data = []
tags = code.find_all('tr')
for tag in tags:
  x = tag.text
  data.append(x)

data

datas = []
for i in data:
  datas.append(i.split('\n')[1:-1])



cleaned_data = [i for i in datas if i[0] != '']


import csv
file = open('covid_data.csv','w')
x = csv.writer(file)
for i in cleaned_data:
  x.writerow(i)

file.close()

import pandas as pd
df = pd.read_csv('/content/covid_data.csv')
df

df = df.iloc[0:10]
x = list(df['Country,Other'])
y = list(df['TotalCases'])
y_death = list(df['TotalDeaths'])
new_y = []
for i in y:
  z = int(i.replace(',','')) 
  new_y.append(z)

new_y_death = []
for j in y_death:
  z = int(j.replace(',','')) 
  new_y_death.append(z)

import plotly.graph_objects as go
x_axis=x
y_axis = y
fig = go.Figure([go.Bar(x=x_axis, y=new_y)])
fig.show()

import plotly.graph_objects as go

fig = go.Figure(data=[go.Pie(labels=x, values=new_y)])
fig.show()

import plotly.graph_objects as go

fig = go.Figure(data=[
    go.Bar(name='Total Active cases', x=x, y=new_y),
    go.Bar(name='Total Death', x=x, y=new_y_death)
])
# Change the bar mode
fig.update_layout(barmode='group')
fig.show()