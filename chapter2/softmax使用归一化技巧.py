import numpy as np 
f = np.array([123,456,789])
# p = np.exp(f) / np.sum(np.exp(f))

f -= np.max(f)
print(f)
p = np.exp(f) / np.sum(np.exp(f))
print(p)