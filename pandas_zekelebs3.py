import pandas as pd

hr_data_itr = pd.read_csv(
    'https://raw.githubusercontent.com/zekelabs/data-science-complete-tutorial/master/Data/HR_comma_sep.csv.txt')

abc = hr_data_itr[(hr_data_itr['time_spend_company'] < 6) & (hr_data_itr['promotion_last_5years'] == 1)]
print(abc)

data = hr_data_itr.groupby(['salary']).mean()
print(data['satisfaction_level'])

print(hr_data_itr.isnull().values.any())

hr_cat = hr_data_itr.select_dtypes('object')
print(hr_cat)

print(hr_data_itr[hr_data_itr['left'] == 1].groupby(['satisfaction_level', 'last_evaluation']).mean().iloc[:, :0])

print(hr_data_itr[hr_data_itr['left'] == 0].groupby(['satisfaction_level', 'last_evaluation']).mean().iloc[:, :0])

print(hr_data_itr.hist())

hr_data_itr['next_promotion'] = 0
print(hr_data_itr)

hr_data_itr['next_promotion'] = (hr_data_itr['satisfaction_level'] < 0.5) & (hr_data_itr['left'] == 0) & (
            hr_data_itr['salary'] == 0)
print(hr_data_itr)
