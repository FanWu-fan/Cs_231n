def prints(*arg):
    print (arg)

prints(1,2,3,4,5,6,7)

def prints2(*arg):
    n=len(arg)
    for i in range(n):
        print(arg[i])
prints2(1,2,3,4,5,6,7,7,8)

def prints3(**arg):
    print(arg)
prints3(c=1,g=2,k=3,a=10,b=20)

def add(x,y):
    print(x+y)
para = (1,2)
add(*para)

def add(x,y):
    print (x+y)
kkwd = {'x' :1,'y':2}
add(**kkwd)