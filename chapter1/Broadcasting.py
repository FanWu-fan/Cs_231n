import numpy as np 
'''
x = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
v = np.array([1,0,1])
y = np.empty_like(x)

for i in range(4):
    y[i,:] = x[i,:] + v
print(y)
'''
'''
x = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
v = np.array([1,0,1])
vv = np.tile(v,(4,1))

print(vv)
'''

'''
#利用广播机制来进行计算
x = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
v = np.array([1,0,1])
y = x+v
print(y)
'''

a = np.array([1.0, 2.0, 3.0])
b = np.array([2.0, 2.0, 2.0])
print(a/b)


b = 2.0
print(a*b)