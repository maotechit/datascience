import numpy as np

precies = np.array([100,200,300])
discount = np.array([0.9])


total_price = precies * discount
#print(total_price)

A = np.array([0,100,23,55,56,1])
#print(np.any(A >0))
#print(np.all(A >100))


B = np.split(A,3)
print(B)