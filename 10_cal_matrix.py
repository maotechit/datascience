import numpy as np

A = np.array([[1,2],[3,4]])
B = np.array([[5,6],[7,8]])


#determinanate e inversa
det_A = np.linalg.det(A)
inv_A = np.linalg.inv(A)


##suma
suma_AB = A + B

#multipliaccion
multi_AB = np.dot(A , B)

#Ecuaciones lineales Ax=b
b = np.array([9,11])
x = np.linalg.solve(A,b)
print("Hola")
print(x)