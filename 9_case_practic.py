import numpy as np
import pandas as pd

months = np.array(['January', 'Febuary', 'Mar', 'Apr', 'May','Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
product_A = np.array([150,200,250,300,220,210,180,190,230,240,280,300])
product_B = np.array([180,210,230,250,270,260,240,250,270,290,310,330])
product_C = np.array([200,220,240,260,280,300,320,340,360,380,400,420])


matriz = np.stack((product_A, product_B, product_C))
df =pd.DataFrame(matriz,index=['product_A','product_B','product_C'],columns=months)
print()
print()
print(df)



A = np.array([[1,2],[3,4]])
B = np.array([[5,6],[7,8]])

#suma
suma_AB = A + B

#multipliaccion
multi_AB = np.dot(A , B)


