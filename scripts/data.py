import pandas as pd
import numpy as np
import plotly.graph_objs as go
import plotly.colors
import requests

#country_default = OrderedDict([('Canada', 'CAN'), ('United States', 'USA'), ('France', 'FRA'), ('India', 'IND'), ('Italy', 'ITA'),
#  ('Germany', 'DEU'), ('United Kingdom', 'GBR'), ('China', 'CHN'), ('Japan', 'JPN'), ('South Korea', 'KOR')])

country_default = ['Canada', 'United States', 'France', 'India', 'Italy', 'Germany', 'United Kingdom', 'China', 'Japan', 'South Korea']

def return_figures(countries = country_default):
    """Creates four plotly visualizations using
        # Coronavirus Disease (COVID-19) – Statistics and Research API
        # Source: https://ourworldindata.org/coronavirus
        # https://api.namara.io/v0/data_sets/{DATA_SET_ID}/data/{VERSION}?api_key={YOUR_API_KEY}&query_parameters={VALUE}
        Args:
            country_default (list): list of countries for filtering the data
        Returns:
            list (dict): list containing the four plotly visualizations
    """

    urls_world = []
    data_frames = []

    date_min = '2019-12-31'

    # api url for covid-19 data
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

    if not bool(countries):
        countries = country_default

    df = pd.DataFrame(data_frames)

    # sort the data frames based on date
    df.sort_values('date', ascending=True, inplace=True)

    # first chart total covid-19 cases versus date
    graph_one = []

    for country in countries:
        x_val = df[df['location'] == country].date.tolist()
        y_val =  df[df['location'] == country].total_cases.tolist()
        graph_one.append(
          go.Scatter(
          x = x_val,
          y = y_val,
          mode = 'lines',
          name = country
          )
        )

    layout_one = dict(title = 'COVID-19 Total Cases Trends from 2019-12-31',
                xaxis = dict(title = 'Date',
                  autotick=False, tick0=date_min, dtick=10*86400000),
                yaxis = dict(title = 'Total Cases'),
                )

    # second chart plots new cases from 2019-12-31
    graph_two = []

    for country in countries:
        x_val = df[df['location'] == country].date.tolist()
        y_val =  df[df['location'] == country].new_cases.tolist()
        graph_two.append(
          go.Scatter(
          x = x_val,
          y = y_val,
          mode = 'lines',
          name = country
          )
        )

    layout_two = dict(title = 'COVID-19 New Cases Trends from 2019-12-31',
                xaxis = dict(title = 'Date',
                  autotick=False, tick0=date_min, dtick=10*86400000),
                yaxis = dict(title = 'New Cases'),
                )

    # third chart plots total deaths from 2019-12-31
    graph_three = []

    for country in countries:
        x_val = df[df['location'] == country].date.tolist()
        y_val =  df[df['location'] == country].total_deaths.tolist()
        graph_three.append(
          go.Scatter(
          x = x_val,
          y = y_val,
          mode = 'lines',
          name = country
          )
        )

    layout_three = dict(title = 'COVID-19 Total Deaths Trends from 2019-12-31',
                xaxis = dict(title = 'Date',
                  autotick=False, tick0=date_min, dtick=10*86400000),
                yaxis = dict(title = 'Total Deaths'),
                )

    # fourth chart plots total tests from 2019-12-31
    graph_four = []

    for country in countries:
        x_val = df[df['location'] == country].date.tolist()
        y_val =  df[df['location'] == country].total_tests.tolist()
        graph_four.append(
          go.Scatter(
          x = x_val,
          y = y_val,
          mode = 'lines',
          name = country
          )
        )

    layout_four = dict(title = 'COVID-19 Total Tests Trends from 2019-12-31',
                xaxis = dict(title = 'Date',
                  autotick=False, tick0=date_min, dtick=10*86400000),
                yaxis = dict(title = 'Total Tests'),
                )

    # append all charts
    figures = []
    figures.append(dict(data=graph_one, layout=layout_one))
    figures.append(dict(data=graph_two, layout=layout_two))
    figures.append(dict(data=graph_three, layout=layout_three))
    figures.append(dict(data=graph_four, layout=layout_four))

    return figures
