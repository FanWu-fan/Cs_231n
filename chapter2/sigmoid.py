import math
w = [2,-3,-3]
x = [-1,-2]

#前向传播
dot = w[0]*x[0] + w[1]*x[1] + w[2]
f = 1.0/(1+math.exp(-dot))

#对神经元反向传播
ddot = (1-f) *f
dx = [w[0]*ddot,w[1]*ddot] #回传到x
dw = [x[0]*ddot,x[1]*ddot,1.0*ddot]

print(dx,dw)