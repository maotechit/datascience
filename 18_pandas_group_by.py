import numpy as np
import pandas as pd

path ='csv\Online_Retail.csv'
df = pd.read_csv(path,encoding = 'latin1')

'''
#print(df.head(0))
country_count = df['Country'].value_counts()
#print(country_count)

country_group = df.groupby('Country')['Quantity'].sum()
country_rank = country_group.sort_values(ascending=False)
#print(country_group)
country_stats = df.groupby('Country')['Quantity'].agg(['mean','sum'])
country_stock_group = df.groupby('Country')['Quantity']
country_stock_group = df.groupby(['Country','StockCode'])['Quantity'].sum()
#print(country_rank.iloc[:3])
#print(type(country_stock_group))
#print(country_stock_group)

def total_revenue(group):
    return (group['Quantity'] * group['UnitPrice']).sum()


revenue_per_country = df.groupby('Country').apply(total_revenue)
#revenue_per_country = df.groupby('Country', group_keys=False).apply(total_revenue)
#1grouped = df.groupby('Country')
#1revenue_per_country = grouped.apply(lambda x: total_revenue(x)).reset_index(drop=True)

#print(revenue_per_country)

top_3_best_sales  = revenue_per_country.sort_values(ascending=False)
top_3_worst_sales = revenue_per_country.sort_values(ascending=True)

#print("Top 3 best sales:",top_3_best_sales)
#print("Top 3 worst sales:",top_3_worst_sales)

'''
'''
print(df['Quantity'])
print(type(df['Quantity']))
print(df[['Quantity']])
print(type(df[['Quantity']]))
'''