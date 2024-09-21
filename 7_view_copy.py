import numpy as np

np_survey_responses = np.array(["good","excellente","bad","good","bad","excellente","good","good","bad"])

#1
responses,count = np.unique(np_survey_responses,return_counts=True)

A = id(np_survey_responses)
A = responses.base
A = id(responses)
#print(responses,count)
print(A)


#2 "VIEW and "COPY"
array_x = np.array([2,3,56,67,78,90,8565])
#array_x = np.arange(10)
copy_x = array_x[[2,3]]
view_x = array_x[1:3]
print("copy:",copy_x)
print("view:",view_x)
array_x[1:3] = [100,222]
print("copy_past:",copy_x)
print("view_past:",view_x)

print("shiring memory with the copy?",np.shares_memory(array_x,copy_x))
print("shiring memory with the view?",np.shares_memory(array_x,view_x))

print("Conclusion: cuando se altera el array original las vistas cambian pero las copias no")

