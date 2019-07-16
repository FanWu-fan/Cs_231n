#前向传播
import numpy as np 
W = np.random.randn(5,10)
X = np.random.randn(10,3)
# print(W,X)
D = W.dot(X)

#假设我们得到了D的梯度
dD = np.random.randn(*D.shape)#这个*号自动解包，解为两个参数传入
print(*D.shape)
print(D.shape)
dW = dD.dot(X.T)
dX = W.T.dot(dD)  

