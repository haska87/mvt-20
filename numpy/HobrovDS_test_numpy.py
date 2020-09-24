#1
import numpy as np
a = np.ones((10))
print(a)
#2
np.random.rand(4,4)
#3
a = np.random.randint(0,100,(5,3))
print(a)
#4
a.shape = (3,5)
a = a.astype('float64')
print(a)
#5
print(np.sum(a))
print(np.max(a))
print(np.sum(a)/(np.size(a)))
#6
n6=3
def sinpluscos(x):
    a=np.empty(0)
    for i in x.flat:
        a=np.append(a,np.sin(i) + np.cos(i))
        print(np.sin(i) + np.cos(i))
    a.shape = x.shape
    return(a)
p = np.random.randint(-10,10,(n6,n6))
print("6: do ",p)
p = sinpluscos(p)
print("poosle: ",p)

#7
print("")
def abplusc(a,b,c):
    return((np.dot(a,b)+c))
n7=3
a7 = np.random.randint(-10,10,(n7,n7))
b7 = np.random.randint(-10,10,(n7,n7))
print("a:   ",np.dot(a7,b7))
c7 = np.random.randint(-10,10,(n7,n7))
print("")
print(a7)
print(b7)
print(c7)
print("7: ",abplusc(a7,b7,c7))

#8
def matr(a):
    opred = np.linalg.det(a)
    if(opred>0):
        return(np.linalg.qr(a))
    else:
        return(np.linalg.inv(a))
v = np.random.randint(-3,3,(3,3))
print(matr(v))
#9
n9 = 2
m9 = 4
a9 = np.random.randint(0,10,(n9,m9))
b9 = np.random.randint(0,10,(m9,n9))
scalyar = np.random.randint(0,10)
print(a9)
print(b9)
print(scalyar)
print(np.dot(scalyar,a9))
print(np.matmul(a9,b9))
#10
n10 = 3
A = np.random.randint(-10,10,(n10,n10))
b = np.random.randint(-10,10,n10)
print(np.linalg.solve(A, b))


