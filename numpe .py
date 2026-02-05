import numpy as np

d={'1':'A'}

a = np.array([[1,2,3],
              [4,d,6],
              [7,8,"Hello"]])#,dtype = np.int32)

print(a.dtype)
#print(a[1][1].dtype)
#print(a[1,1])
