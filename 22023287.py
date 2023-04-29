# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 01:31:13 2023

@author: BINEESHA BABY
"""

import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt


# Load COVID-19 data from a CSV file
covid_data = pd.read_csv("D:/C/WHO_COVID_19.csv")

# Define a function to filter the data for a specific country and create a line plot using Plotly Express
def plotly_lineplot(country):
    # Filter the data to select the specified country
    country_data = covid_data[covid_data['Country'] == country]

    # Convert the Date_reported column to a datetime format
    country_data['Date_reported'] = pd.to_datetime(country_data['Date_reported'])

    # Create a line plot of new cases and new deaths over time using Plotly Express
    fig = px.line(country_data, x='Date_reported', y=['New_cases', 'New_deaths'], title=f'COVID-19 in {country}')

    # Return the Plotly figure
    return fig

# Define a function to filter the data for a specific country and create a line plot using Matplotlib
def matplotlib_lineplot(country):
    # Filter the data to select the specified country
    country_data = covid_data[covid_data['Country'] == country]

    # Convert the Date_reported column to a datetime format
    country_data['Date_reported'] = pd.to_datetime(country_data['Date_reported'])

    # Create a line plot of new cases and new deaths over time using Matplotlib
    fig, ax = plt.subplots()
    ax.plot(country_data['Date_reported'], country_data['New_cases'], label='New Cases')
    ax.plot(country_data['Date_reported'], country_data['New_deaths'], label='New Deaths')
    ax.set_xlabel('Date')
    ax.set_ylabel('Number of Cases')
    ax.set_title(f'COVID-19 in {country}')
    ax.legend()

    # Return the Matplotlib figure
    return fig




us_data = covid_data[covid_data['Country'] == 'United States of America']
april_data = covid_data[covid_data['Date_reported'].str.startswith('2021-04')]

country_data = covid_data.groupby('Country')['New_cases'].sum()
date_data = covid_data.groupby('Date_reported')['New_cases', 'New_deaths'].sum()

# Bar chart of total cases by country
country_data.sort_values().plot(kind='barh', figsize=(10, 20))
plt.xlabel('Total cases')
plt.ylabel('Country')
plt.title('COVID-19 cases by country')

# Line chart of new cases and deaths by date
date_data.plot(kind='line', figsize=(10, 5))
plt.xlabel('Date')
plt.ylabel('Count')
plt.title('COVID-19 cases and deaths by date')

