import pandas as pd

path = 'csv\Online_Retail.csv'
#DataFrame
retail_data = pd.read_csv(path,encoding='latin1')

#Me muestra los nombres de las columnas
columns_names = retail_data.columns
#Me muestra el numero de filas y columnas
num_rows,num_columns = retail_data.shape
#Me muestra todos los datos de la columna elejida.
retail_dataA = retail_data[['Quantity']]
#print(retail_dataA)
#print(retail_data.Quantity)
summary = retail_data.describe()



for label,row in retail_data.iterrows():
            #print(label)
            #print(row)
            #print("Hola soy yo"+str(2))
            print(label,":",row['Quantity'])






