import numpy as np

a = np.array([[1,2,3,4,5,6],
              [7,8,9,10,11,12],
              [13,14,15,16,17,18],
              [18,19,20,21,22,23],])


#a = np.concatenate((a1, a2) ,axis=1)
#print(a)

#a= np.vstack((a1,a2))
#print(a)

#a= np.hstack((a1,a2))
#print(a)

print(np.split(a, 6, axis=1))