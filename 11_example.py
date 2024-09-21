import numpy as np

#Crea dos arrays de 1D con valores enteros y realiza las operaciones de suma, resta, multiplicación, y división entre ellos.
A1 = np.array([10,20,30,40])
A2 = np.array([1,2,3,4])

#Suma
suma = A1 + A2
#print("La suma de A1+A2",suma)
#resta
resta = A1 - A2
#print("La resta de A1+A2",resta)
#Multiplicacion
multi = A1 * A2
#print("La multiplicacion de A1*A2",multi)
#Divicion 
divi = A1 // A2
#print("La divicion de A1/A2",divi)

#Dado un array de datos, calcula la media, mediana, varianza, y desviación estándar.
#Media
#A3 = np.random.randint(1,100,size=9)
#A3 = np.array(1,100,size=9)
media_array =np.mean(A1)
#print("La media es: ",media_array)
#Mediana
mediana_array =np.median(A1)
#print("La mediana es: ",media_array)
#Varianza
varianza_array =np.var(A1)
#print("La varianza es: ",varianza_array)
#Desviacion Standar
std_array = np.std(A1)
#print("La desviacion standar es: ",std_array)

#exam_arrayA = np.random.randint(1,25,size=(2,2))
#exam_arrayB = np.random.randint(1,25,size=(2,2))

#Crea dos matrices de 2x2 y realiza las operaciones de suma, resta, multiplicación (producto matricial) y cálculo de la inversa de una de ellas.
exam_arrayA = np.array([[-5,3],[4,7]])
exam_arrayB = np.array([[9,0],[2,-5]])
#print("A",exam_arrayA)
print()
#print("B",exam_arrayB)
print()
#print("A-B",exam_arrayA-exam_arrayB)
print()
#print("A*B",exam_arrayA*exam_arrayB)
print()
multi_AB = np.dot(exam_arrayA, exam_arrayB)
#print("AxB",multi_AB)

#Algebra Lineal-Inversa

inversaA = np.linalg.inv(exam_arrayA)
#print("inversa A",inversaA)

#Resuelve el sistema de ecuaciones lineales dado por Ax=b, donde A es una matriz 2x2 y b es un vector de 2 elementos.
#Algebra Lineal-Ax=b
A = np.array([[2,3],[1,2]])
b = np.array([8,5])

x = np.linalg.solve(A,b)
#print("Solucion del sistema de ecuaciones",x)

#Genera un array de 1000 números aleatorios que sigan una distribución normal con media 0 y desviación estándar 1. Calcula la media y desviación estándar del array generado.
#Generar array de 1000 numeros aleatorios

datos_simulados = np.random.normal(0, 1, 1000)
media_simulada = np.mean(datos_simulados)
desviacion_simulada = np.std(datos_simulados)

aleato_array = np.random.randint(5,6,1000)
print(aleato_array)
print("media",np.median(aleato_array))
print("std",np.std(aleato_array))

