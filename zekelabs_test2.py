import numpy as np
import pandas as pd

cols = ['age', 'workclass', 'fnlwgt', 'education', 'education-num', 'marital-status', 'occupation', 'relationship'
    , 'race', 'sex', 'capital-gain', 'capital-loss', 'hours-per-week', 'native-country', 'Salary']
adult_data = pd.read_csv(
    'https://raw.githubusercontent.com/zekelabs/data-science-complete-tutorial/master/Data/adult.data.txt', names=cols)

# Access by column name
print(adult_data['workclass'])
print(adult_data['native-country'])

# Replace ? values to nan for native country column
print(adult_data['native-country'].map(lambda x: np.nan if x.strip() == '?' else x))
print(adult_data['native-country'].values)

# set race column as index (there would not be any race column)
print(adult_data.set_index('race', inplace=True))
print(adult_data)

# reset column to default and race as column again
adult_data.reset_index(inplace=True)
print(adult_data)

# set age column as index (there would not be any age column)
adult_data.set_index('age', inplace=True)
print(adult_data)

# sort index if you wanna access any range element for index
adult_data.sort_index(inplace=True)
print(adult_data)

# index value count
print(adult_data.index.value_counts())
# get data for all age between 18 to 21
print(adult_data.loc[18:21])

# reset index
adult_data.reset_index(inplace=True)
print(adult_data)

adult_data.set_index('race', inplace=True)
print(adult_data)

print(adult_data.index.value_counts())

adult_data.sort_index(inplace=True)
print(adult_data)

# removing space in elements before making it as index and fecth data by index
adult_data.index = adult_data.index.map(lambda x: x.strip())
print(adult_data)

print(adult_data.loc['White'])

adult_data.reset_index(inplace=True)
print(adult_data)

# fetch data for perticuler data type
adult_data.select_dtypes('object')
print(adult_data.select_dtypes('object').info())

# group by race
g = adult_data.groupby('race')
for k, d in g:
    print('=================================================')
    print(k)
    print(d)

# means for all table and group by race
m = adult_data.groupby('race').mean()
print(m)

adult_data.hist()

print(adult_data[adult_data['native-country'].isnull()].head(5))

# fill nan by first elements
print(adult_data['native-country'].fillna(method='ffill', inplace=True))
