import pandas as pd

# assignment url - https://github.com/zekelabs/pandas-assignment/blob/master/02_Filtering_%26_Sorting/Chipotle/Exercises.ipynb

# Import the dataset from this address
chipo = pd.read_table('https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv')

# See the first 10 entries
print(chipo.head(5))

# number of columns in the dataset
print(chipo.columns)

# Assign it to a variable called chipo
print(chipo.info())

# number of observations in the dataset
print(chipo.count() + 1)

# name of all the columns
print(list(chipo.columns.values))

# most ordered item
# chipo['item_name'].nlargest(1)

# What is the price of each item
print(chipo[['item_name', 'item_price']])

# Sort by the name of the item
print(chipo.sort_values(by='item_price'))

# What was the quantity of the most expensive item ordered
print(chipo.sort_values(by='item_price', ascending=False).head(1)['item_price'])

# Veggie Salad Bowl order count
print(chipo[chipo['item_name'] == 'Veggie Salad Bowl']['item_name'].count())

# Canned Soda order more then 1
print(chipo[(chipo['item_name'] == 'Canned Soda') & (chipo['quantity'] > 1)][''].count())
item_name
