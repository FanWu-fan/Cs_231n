import numpy as np 
a = np.array([1,2,3])
print(type(a))
print(a.shape)

b =np.zeros((2,2))
print(b)

c = np.full((4,5),7)
print(c)

print(np.eye(8))

e = np.random.random((2,2))
print(e)
print(e.T)