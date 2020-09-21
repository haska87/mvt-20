import numpy as np
import math
import random
#1
print("#1:")
print(np.ones(10))
print("")
#2
print("#2:")
print(np.random.sample((4,4)))
print("")
#3
print("#3:")
a = np.random.randint(0,100,(5,3))
print(a)
print("")
#4
print("#4:")
a.shape = (3,5)
a = a.astype('float64')
print(a)
print("")
#5
print("#5:")
print(np.sum(a))
print(np.max(a))
print(np.sum(a)/a.size)
print("")
#6
print("#6:")
def sincos(a):
    t = np.empty(0)
    for row in a:
        for x in row:
            t = np.append(t,math.sin(x)+math.cos(x))
    t.shape = a.shape
    return(t)
b = a.copy()
b = b.astype('int64')
print(b)
print("")
b = sincos(b)
print(b)
print("")
#7
print("#7:")
def func(a,b,c):
    return(np.dot(a,b)+c)
n = 3
a = np.random.randint(0,10,(n,n))
b = np.random.randint(0,10,(n,n))
c = np.random.randint(0,10,(n,n))
print(a)
print(b)
print(c)
print("")
print(func(a,b,c))
print("")
#8
print("#8:")
def matr(a):
    deter = linalg.det(a)
    if(deter>0):
        return(linalg.qr(a))
    else:
        return(linalg.inv(a))
print("")
#9
print("#9:")
n=2
m=4
c = np.random.randint(0,10,(n,m))
d = np.random.randint(0,10,(m,n))
scal = random.randint(0,10)
print(c)
print(d)
print(scal)
print(np.dot(scal,c))
print(np.matmul(c,d))
print("")
#10
print("#10:")
n=3
a = np.random.randint(0,10,(n,n))
b = np.random.randint(0,10, n)
x = np.linalg.solve(a,b)
print(x)
