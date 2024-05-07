# -*- coding: utf-8 -*-
"""
Created on Tue May  7 18:18:53 2024

@author: 90539
"""

import pandas as pd

dataset = pd.read_csv("country_vaccination_stats.csv")

#column_argentina = dataset[dataset['country'] == 'Argentina']

#print(column_argentina['daily_vaccinations'].min())
#arge_min = column_argentina['daily_vaccinations'].min()
#column_argentina['daily_vaccinations'].fillna(arge_min, inplace=True)
countries = dataset['country'].unique()

for country in countries:
    country_row = dataset[dataset['country'] == country]
    dailymin_vaccinations = country_row['daily_vaccinations'].min()
    country_row['daily_vaccinations'].fillna(dailymin_vaccinations, inplace=True)
    dataset.loc[dataset['country'] == country, 'daily_vaccinations'] = country_row['daily_vaccinations']

print(dataset)

   
    
    