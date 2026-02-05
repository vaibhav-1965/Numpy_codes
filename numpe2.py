import numpy as np

d={'1':'A'}

a = np.array([[1,2,3],
              [4,5,6],
              [7,8,"Hello"]],dtype ="<U2")

print(a.dtype)
print(type(a[1][0]))

