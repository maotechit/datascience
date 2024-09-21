import numpy as np
import pandas as pd
#Rows: 541909 Columns: 8
path ='csv\Online_Retail.csv'
#Leer el dataset de ventas de un archivo de CSV.
df = pd.read_csv(path,encoding='latin1')
'''
#Pivot: Resumir,reorganizar,Identificar patrones o comparar subgrupo de datos.

pivot_table = pd.pivot_table(df,values = 'Quantity',index='Country')
#print(df['Quantity'] )

#print(pivot_table)
paises = df[df['Country'] == 'Australia']
print(paises['Quantity'].sum() )
print('Suma',df.groupby('Country')['Quantity'])
#Apilar y Desapilar
'''
dicc = {
    'A':['food','bar','baz'],
    'B':[1,2,3],
    'C':[4,5,6]
    }


df = pd.DataFrame(dicc)
df_stacked = df.stack()
#print(df_stack)


df_unstacked = df_stacked.unstack()
print(df_unstacked)