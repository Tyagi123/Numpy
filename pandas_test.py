# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
# print(np.arange(5,9))


import pandas as pd

print(pd.Series([1, 2, 3], index=list('abc')))
print(pd.Series([12, 22, 32]))

a = pd.Series({'a': 1, 'b': 2})
print(a)

a = pd.Series([11, 12, 13, 14, 15], list('abcde'))
print(a)
b = pd.Series([11, 12, 13, 14, 15], list('bcdef'))
print(b)
df = pd.DataFrame({'ser1': a, 'ser2': b})
print(df)

print(df['ser1'])

print(list(df['ser1']))

test = pd.DataFrame(np.random.randint(0, 6, (10, 10)), columns=list('abcdefjhij'))

print(test)

print(test['a'])

hr_data = pd.read_csv(
    'https://raw.githubusercontent.com/zekelabs/data-science-complete-tutorial/master/Data/HR_comma_sep.csv.txt')

# stats like null values and row numbers
print(hr_data.info())

print(hr_data.columns)

print(hr_data.head(5))

print(hr_data.tail(5))

print(hr_data['salary'])

# reterive top 5 elements for salary and sales
print(hr_data[['salary', 'sales']].head(5))

print(hr_data['salary'][::2])

print(hr_data.info())

# comparision for data  as per row : check hr_data mention twices
print(hr_data[hr_data['salary'] == 'low'])

print(hr_data[(hr_data['salary'] == 'low') & (hr_data['time_spend_company'] > 5)].head(5))

# ways to check people promoted in last 5 years
print(hr_data[hr_data['promotion_last_5years'] > 0])
print(hr_data['promotion_last_5years'].value_counts())

print(hr_data['time_spend_company'].value_counts())

# person got promotion in lastr five year and spend less than 6 hrs in company
print(hr_data[(hr_data['promotion_last_5years'] > 0) & (hr_data['time_spend_company'] < 6)].shape)

hr_data['newcol'] = hr_data['salary'].str.replace('low', 'l')
print(hr_data['newcol'])

# get peticuler row 
print(hr_data.iloc[3])

print(hr_data.iloc[0:2, 3:5])

print(hr_data.describe())

## drop Nan values
hr_data.dropna(inplace=True)

hr_data.reset_index(inplace=True)

print(hr_data.info())
