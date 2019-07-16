import math
x =3
y = -4

#前向传播
sigy = 1.0 / (1 + math.exp(-y))  #(1)
num = x+sigy                     #(2)
sigx = 1.0 / (1 + math.exp(-x))  #(3)
xpy = x+y                        #(4)
xpysqr = xpy**2                 #(5)
den = sigx + xpysqr             #(6)
invden = 1.0/den                #(7)
f = num*invden                  #(8)
print(f)

#回传
dnum = invden #分子的梯度   #(8)
dinvden = num #分母的梯度       #(8)

#回传invden = 1.0 /den
dden = -(1.0 / (den**2)) * dinvden  #(7)

#回传 den = sigx + xpysqr
dsigx = (1)*dden             #(6)
dxpysqr = (1)*dden              #(6)

#回传xpysqr = xpy**2
dxpy = (xpy*2)*dxpysqr      #(5)

#回传xpy = x+y 
dx = (1)*dxpy           #(4)
dy = (1)*dxpy               #(4)

#回传 sigx = 1.0 / (1 + math.exp(-x))       
dx += ((1-sigx)*sigx)*dsigx           #(3)

#回传num = x+sigy
dx += (1)*dnum  #(2)
dsigy = (1)*dnum  #(2)

#回传sigy = 1.0 / (1 + math.exp(-y))
dy +=((1-sigy)*sigy)*dsigy  #(1) 

print("dx: ",dx,"dy: ",dy)