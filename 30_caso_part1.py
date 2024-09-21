import pandas as pd

path = 'csv\Online_Retail.csv'
#DataFrame
retail_data = pd.read_csv(path,encoding='latin1')

#Null: en Description 1454  y CustomerID 135080
'''print("isnull",retail_data.isnull().sum())'''
# 5268 duplicates
'''print(retail_data.duplicated().sum())'''

