import pandas as pd
import numpy as np
import plotly.graph_objs as go
import plotly.colors
from collections import OrderedDict
import requests

#country_default = OrderedDict([('Canada', 'CAN'), ('United States', 'USA'), ('France', 'FRA'), ('India', 'IND'), ('Italy', 'ITA'),
#  ('Germany', 'DEU'), ('United Kingdom', 'GBR'), ('China', 'CHN'), ('Japan', 'JPN'), ('South Korea', 'KOR')])

country_default = ['CAN', 'USA', 'FRA', 'IND', 'ITA', 'DEU', 'GBR', 'CHN', 'JPN', 'KOR']

urls_world = []
data_frames = []

date_min = '2019-12-31'

# url for covid-19 data
for i in range(0, 20000, 250):
    url_world = 'https://api.namara.io/v0/data_sets/e820187b-708c-4394-a251-8fe61b919624/data/en-0?geometry_format=wkt&api_key=e2eb2c33b96a020626208c72182d57a50b1aa6ae19503a0cd12b9f4e07712724&organization_id=5eaf15fe48fab800111e1edc&project_id=5eaf164668d37d000f249dba&limit=250&offset={}'.format(i)

    try:
        r = requests.get(url_world)
    except:
        print('could not load data')

    #for j in range(len(r.json())):
        #data = r.json()[j]
        #data_frames.append(data)
    data = r.json()
    data_frames.extend(data)

#if not bool(countries):
countries = country_default

df = pd.DataFrame(data_frames)

# first chart cases versus date
graph_one = []

# filtering plots the countries in decreasing order by their values
#df = df[(df['date'].year == '2016') | (df['date'].year == '1990')]
df.sort_values('date', ascending=True, inplace=True)

x_val = df[df['location'] == 'Canada'].date.tolist()
y_val =  df[df['location'] == 'Canada'].total_cases.tolist()
fig = go.Figure(data=go.Scatter(
            x = x_val,
            y = y_val,
            mode = 'lines',
            name = 'Canada'))

fig.show()
