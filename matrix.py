import numpy as np
matrix1=[[1,2,3],[4,5,6],[7,8,9]]
matrix2=[[1,2,3],[4,5,6],[7,8,9]]
arr1=np.array(matrix1)
arr2=np.array(matrix2)
#print(arr2)
#print(arr1)
#print(arr1/arr2)
a=np.zeros((2,5))
#print(a)
rng=np.arange(18)
#print(rng)
b=rng.reshape(3,6)
#print(b)
c=b.ravel()
print(c)
print(arr1.sum(axis=0))
print(arr1.T)