import numpy as np

np_matriz = np.array([[1,10,3],[4,45,6],[7,8,9]])
transposed_np_matriz = np_matriz.T
print()
print(np_matriz)
print()
print(transposed_np_matriz)

########################################

np_array = np.arange(1,13)
reshape_array = np_array.reshape(3,4)
#print(np_array)
#print(reshape_array)

###########################################
reverse_array = np_array[::-1]
#print(reverse_array)

########################################

# FLATENNED HORIZONTAL 

flatenned_array = np_matriz.flatten()
#print(flatenned_array)

# FLATENNED VERTICAL

flatenned_array = np_matriz.flatten().reshape(-1,1)
#print(flatenned_array)
