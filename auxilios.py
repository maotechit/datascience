import numpy as np
import pandas as pd
path ='csv\Online_Retail.csv'
df = pd.read_csv(path,encoding = 'latin1')
# Crear una Serie desde una lista
#serie = pd.Series(\[10, 20, 30, 40])
#tail(): Regresa las últimas 5 filas (por default) del DataFrame o de la Serie.
#sample(): Regresa aleatoriamente 5 filas (por default) del DataFrame o de la Serie.
#Tanto head(), tail() y sample() son de gran utilidad a la hora de darle un primer vistazo a los datos, y así podemos darnos una idea de que podemos hacer posteriormente en nuestros análisis.

#Les servirá para cuando quieran saber cuantas filas o registros de valores nulos o faltantes de 
# dos o más columnas #comparten y así sacar un porcentaje que les ayude a entender mejor cómo están 
# distribuidos esos datos nulos entre las columnas.

#retail_data = pd.read_csv(path,encoding='windows-1252')

# Ordena los datos por columna
#Description = retail_data.sort_values(by='Description', ascending=False)
#print(Description)

A = pd.DataFrame({'Num': [4, None, 9, None, 77]})
B = pd.DataFrame({'Num': [44, None, 6, 22, None]})

null_A = A[A.Num.isna() == True].index
null_B = B[B.Num.isna() == True].index
null_A.intersection(null_B)

##############################################################
data_null = df.isnull()

null_positions = data_null[data_null == True].stack().index.tolist()

print(f"Positions of null values:\n{null_positions}")

######
df['ProductInfo'] = df['StockCode'].astype(str) + " - " + df['Description']

print(df[['StockCode', 'Description', 'ProductInfo']].head())

# Calcular el top 3 de mejores países por ventas
top_countries = df.groupby('Country')['Quantity'].sum().nlargest(3)
top_countries

# Calcular el top 3 de peores países por ventas
worst_countries = df.groupby('Country')['Quantity'].sum().nsmallest(3)
worst_countries


#Un ejemplo interesante es el método np.linalg.lstsq, que permite encontrar la solución por mínimos cuadrados de un sistema de la forma Ax=y. Esto es importante para realizar una regresión lineal simple.

#El primer paso es tener dos vectores de datos a los cuales queremos realizarles una regresión lineal simple. Como queremos una ecuación vectorial de la forma y=mx+c, podemos pasarlo a una forma matricial con np.stack. Finalmente usamos np.linalg.lstsq , y conseguimos una regresión lineal simple!


x = np.array([0,1,2,3])
y = np.array([-1,0.2,0.9,2.1])
A = np.stack([x, np.ones(len(x))], axis=1)
print(A)
m, c = np.linalg.lstsq(A, y, rcond=None)[0]
print(m,c)
print(m*x+c)