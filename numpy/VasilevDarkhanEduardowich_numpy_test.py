import numpy as np

# 1
print("N1")
vector = np.ones((1, 10))
print(vector)
print()

# 2
print("N2")
array1 = np.random.random((4, 4))
print(array1)
print()

# 3
print("N3")
array2 = np.random.randint(0, 101, (5, 3))
print(array2)
print()

# 4
print("N4")
array3 = array2.reshape((3, 5)).astype('float64')
print(array3)
print()

# 5
print("N5")
sumofarray2 = np.sum(array2)
maxofarray2 = np.max(array2)
minofarray2 = np.min(array2)
print("sum = " + str(sumofarray2))
print("max = " + str(maxofarray2))
print("min = " + str(minofarray2))
print()

# 6
print("N6")
array4 = np.sin(array2) + np.cos(array2)
print(array4)
print()

# 7
print("N7")
n = 5
a = np.random.randint(0, 101, (n, n))
b = np.random.randint(0, 101, (n, n))
c = np.random.randint(0, 101, (n, n))
print("a:")
print(a)
print("b:")
print(b)
print("c:")
print(c)
array5 = a * b + c
print("a*b + c = ")
print(array5)
print()

# 8
print("N8")
array6 = np.random.randint(0, 10, (3, 3))
print("Generated array:")
print(array6)
det = np.linalg.det(array6)
print("determinant = " + str(det))
if det != 0:
    if det > 0:
        print("determinant is greater than zero, finding qr:")
        print(np.linalg.qr(array6))
    else:
        print("determinant is lesser than zero, finding invariant:")
        print(np.linalg.inv(array6))
else:
    print("determinant is zero")

print()

# 9
print("N9")
n = 5
m = 4

array7 = np.random.randint(0, 10, (n, m))
array8 = np.random.randint(0, 10, (m, n))

print("First array:")
print(array7)
print("Second array:")
print(array8)

print("Scalar product = " + str(np.dot(array7, array8)))
print("Matrix product:")
print(np.matmul(array7, array8))
print()

# 10
print("N10")

A = np.random.randint(0, 10, (n, n))
b = np.random.randint(0, 10, n)

print("Generated matrix A:")
print(A)

print("Generated vector b:")
print(b)

x = np.linalg.solve(A, b)
print("Solution x:")
print(x)
