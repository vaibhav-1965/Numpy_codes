import numpy as np

a = np.array([[1,2,3,4,5],
              [6,7,8,9,10],
              [11,12,13,14,15],
              [16,17,18,19,20]])

print(a.shape)
#print(a.reshape((5,4)))
#print(a.reshape((20,)))
#print(a.reshape((20,1)))
#print(a.reshape((2,10)))
#print(a.reshape((2,2,5)))
#print(a.reshape((2,5,2)))
#print(a.reshape((5,2,2)))

#print(a.reshape((1,2,1,10,1,1)))

#a.reshape((10,2))
#print(a)

#a.resize(10,2)
#print(a)

print(a.flatten())
print(a.ravel())

#var1= a.ravel()
#var1[2]=100
#print(var1)
#print(a)

var = [v for v in a.flat]
print(var)

#print(a.T)#a.transpose()
print(a.swapaxes(0,1))
