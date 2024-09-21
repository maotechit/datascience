import pandas as pd

path = 'csv\Online_Retail.csv'
#Dataframe
#df =pd.read_csv(path,index_col=0,encoding ="latin1")
df =pd.read_csv(path,encoding ="latin1")

#Ubicar la serie 1 y columna 2 
#print("El df",df)
#print(df.loc[0])
lis_prueba = df["Quantity"]
#print(type(lis_prueba))
#print(df.loc[:,'Country'])
#print(df.loc[0:4])
#print(df)
#print(df.head())
'''for lab,row in df.iterrows():
    print(lab)
    print(row)
    break'''
'''
for x in enumerate(lis_prueba):
    # la respuesta se dan tuplas
    print(x)
    break
for x in lis_prueba.items():
    print(x)
    break
'''

#print(df.isna())
#print(df.isna().sum())
#print(df.dropna())

print(df.iloc[0])
print(df.iloc[[0]])