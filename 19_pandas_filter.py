import numpy as np
import pandas as pd
path ='csv\Online_Retail.csv'
#Leer el dataset de ventas de un archivo de CSV.
df = pd.read_csv(path,encoding = 'latin1')
print(df)
#Muestreme la filtracion de datos de ventas del 2011
df['InvoiceDate'] =pd.to_datetime(df['InvoiceDate'])
#print(df.sort_values(by="InvoiceDate"))
df_may2099= df[df['InvoiceDate'].dt.year >2010]

df['Month'] = df['InvoiceDate'].dt.month
df['Year'] = df['InvoiceDate'].dt.year
df_month_year = df.sort_values(by=["Month","Year"])
print(df)
print(df_month_year)
print(df_may2099)

df = pd.read_csv(path,encoding = 'latin1')
############################################
#print(df.head(2))
#print(df.info())
#print(df.head(1))
#print(df.shape)
#print(df.columns)
#print(df.describe())

# 1-Convertir la columna 'InvoiceDate' a tipo datetime.
#df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
#print(df['InvoiceDate'].head(2))

# 2-Eliminar filas con valores faltantes en la columnas críticas (['Description] y ['CustomerID] y ['InvoiceDate'])
#null_df = df[df.InvoiceDate.isna()==True].index
#null_df = df[df['InvoiceDate'].notna()].index
#null_df = df[df.CustomerID.isna()==True].index
#null_df = df[df['CustomerID'].notna()].index
#print(null_df)
#df.dropna(subset=['CustomerID', 'InvoiceDate'],inplace=True)
#print(df)

#3-Crear una nueva columna 'TotalPrice'

df['TotalPrice'] = df['Quantity'] * df['UnitPrice']
#print(df.head())

#Filtrar las venta en el United Kingdom 
uk_sales = df[df['Country']== 'United Kingdom']
#print(uk_sales)
a=df.groupby('Country')['Quantity'].agg(['sum'])
#print(a)
#print(uk_sales)

#Cantidades de la ventas mayores a 10
high_quantity_sales = df[df['Quantity'] > 7000]
print(high_quantity_sales)
print(type(high_quantity_sales))