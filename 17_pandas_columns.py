import numpy as np
import pandas as pd

path ='csv\Online_Retail.csv'
df = pd.read_csv(path,encoding = 'latin1')

# starting here
#print(df.head(0))
df['TotalPrice'] = df['Quantity'] * df['UnitPrice']

df['val_mayor_18'] = df['TotalPrice'] > 18
#print(df['val_mayor_18'].head(3))
#print(df['val_mayor_18'].info())
#print(df.info())

df["DiscountPrice"]=df['UnitPrice'].apply(lambda x: x*0.9)
#print(df.head(3))

def categorize_price(price):
    if price > 50:
        return 'High'
    elif price < 20:
        return 'Medium'
    else:
        return 'Low'

df["PriceCategory"] = df['UnitPrice'].apply(categorize_price)
#print(df.head(3))
B= np.array([0.9])
print(type(B))
C = df['UnitPrice'] * B
print(type(C))
print(C)





#array_between_18_19 = np.logical_and(df['val_mayor_18']>18,df['val_mayor_18']<19)
#print(type(array_between_18_19))
#print([array_between_18_19])
#print(type[array_between_18_19])



