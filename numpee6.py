import numpy as np

l1 = [1,2,3,4,5]
l2 = [6,7,8,9,0]

a1 = np.array(l1)
a2 = np.array(l2)

print(l1 + l2)
print(a1 + a2)

#not + because of an integer value and also because it is concatenation
#diffrence between numpy and the python list