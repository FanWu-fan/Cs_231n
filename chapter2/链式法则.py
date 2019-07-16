#设置输入值
x=-2
y=5
z=-4

#进行前向传播
q = x+y
f = q*z

#进行反向传播
dfdz = q
dfdq = z

#现在回传到q = x+y
dfdx = 1.0 * dfdq
dfdy = 1.0 * dfdq 
print("dfdx: ",dfdx,"dfdy: ",dfdy)