
import pandas as pd
import numpy as np
path = './csv/Online_Retail.csv'
df = pd.read_csv(path,encoding = 'latin1')
                  
#1-Crear un array: Crea un array de 10 elementos con valores del 0 al 9
'''np_array_10 = np.arange(10)'''
#2-Operaciones matemáticas: Crea un array de 10 elementos con valores aleatorios y calcula su media y desviación estándar.
'''np_array_10 = np.random.randint(10,size=10)
print("media",np.mean(np_array_10))
print("std",np.std(np_array_10))'''
#3-Indexación y segmentación: Crea un array de 20 elementos y selecciona los elementos del 5 al 15.
'''np_array_20 = np.arange(20)
print(np_array_20)
print(np_array_20[5:16])'''

#Ejercicios de Pandas

#1a-Crear un DataFrame: Crea un DataFrame con tres columnas: ‘A’, ‘B’, y ‘C’, y 5 filas con valores aleatorios.
row_random_1 = np.random.randint(1,14,size=3)
row_random_2= np.random.randint(1,41,size=3)
row_random_3 = np.random.randint(1,55,size=3)
row_random_4 = np.random.randint(1,69,size=3)
row_random_5 = np.random.randint(1,84,size=3)
val_5rows = pd.DataFrame([row_random_1, row_random_2, row_random_3,row_random_4,row_random_5],columns=['A','B','C'])
#1b-Filtrar datos: Filtra el DataFrame para mostrar solo las filas donde los valores de la columna ‘A’ sean mayores que 0.5.
'''print(val_5rows)'''
'''print(val_5rows[val_5rows['A'] > 10])'''
#1c-Operaciones con columnas: Añade una nueva columna ‘D’ que sea la suma de las columnas ‘A’ y ‘B’
val_5rows['D'] =val_5rows['A'] + val_5rows['B'] 
print(val_5rows)
