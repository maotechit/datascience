import numpy as np

np_survey_responses0 = np.array(42)
np_miscelanea = np.array([1,"mao",True,2.5])
np_survey_responses1 = np.array(["good","excellente","bad","good","bad","excellente","good","good","bad"])
#np_survey_responses2 = np.array([["good","excellente","bad"],["good","bad","excellente"],["good","good","bad"]])
np_survey_responses3 = np.array([{"good":["excellente","bad"]},{"good":["bad","excellente"]},{"good":["good","bad"]}])
#print(type(np_survey_responses0))
#print(np_survey_responses0.ndim)
#print(np_survey_responses0.shape)
#print(type(np_survey_responses3))

A_range = np.arange(10)


np_survey_responses2 = np.array([["good","excellente","bad"],["good","bad","excellente"],["good","good","bad"]])
np_A = np_survey_responses2[:,0]


A_normal = np.round(np.random.normal(0.0,1,10))
A_identidad = np.eye(3)
A_diagonal = np.diag([0,1,2])


A = np.array([[1,2,3],[4,5,6]])
A1 = np.sum(A)
print(A1)
print(type(A1))
print(A1.ndim)
print(A1.shape)
print(A1.dtype)
print(np.mean(A[:,0]))
