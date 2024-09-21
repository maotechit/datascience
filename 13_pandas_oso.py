import numpy as np
import pandas as pd

#path = 'csv\Online_Retail.csv'
#data_frame = pd.read_excel(path,encoding='latin1')
#data_frame = pd.read_json(path,encoding='latin1')
#sales_data = pd.read_csv(path,encoding='latin1')
#print(sales_data.head())                    
data_array = np.array([[1,2,3],[4,5,6],[7,8,9]])
data_frame = pd.DataFrame(data_array, columns=['Fila A','Fila B','Fila C'])
#print(data_frame)

#Creaccion de un DataFrame a partir de una lista
data_lista = [[1,'Mauricio',49],[2,"Tomas",9]]
data_lista1 = [1,'Mauricio',49]
data_lista2 = [2,"Tomas",9]
columns=['id','name','age']
data_frame = pd.DataFrame([data_lista1,data_lista2], columns=columns)
data_frame = pd.DataFrame(data_lista, columns=['id','name','age'])

print("esto ses:")
data_lista3 = [
    1,
    2,
    5
    
]
data_lista4 = [
    'Mauricio',
    "Tomas",
    ""
    
]
data_framex = pd.DataFrame(
    list(zip(data_lista3,data_lista4)), 
    columns=['id','name']
)

print(data_framex)

#Creacion de un Dataframe a partir de un diccionario.
data_diccionario =[{'Id':1,'Name':"Mauricio", 'Age':49},{'Id':2,'Name':"Tomas", 'Age':9}]
data_frame_diccionario =pd.DataFrame(data_diccionario)
#print(data_frame_diccionario)

#Creacion de un Dateframe a partir de un diccioanrio con listas
data_dicc_list ={'Id':[1,2,3],"Name":["Mauricio","Tomas","Marina"],'Age':[49,9,67]}
data_frame_dicc_lis = pd.DataFrame(data_dicc_list)
#print(data_frame_dicc_lis)
#print(type(data_frame_dicc_lis))

#Creacion de un Dateframe a partir de una SERIE

data_serie = {'Id': pd.Series([1,2,3]), 'Name':pd.Series(["Mauricio","Tomas","Marina"])}
data_frame_serie = pd.DataFrame(data_serie)
#print(data_frame_serie)

