import numpy as np

print("1. Создать вектор размером 10 состоящий из единиц")
print(np.ones(10), '\n')

print("2. Создать массив 4x4 заполненный случайными числами от 0 до 1")
print(np.random.random((4, 4)), '\n')

print("3. Создать массив 5x3 заполненный случайными целыми числами от 0 до 100")
A = np.random.randint(0, 100, (5, 3))
print(A, '\n')

print("4. Поменять форму предыдущего массива на 3х5, а тип на float")
A.reshape((3, 5))
A = A.astype(float)
print(A, '\n')

print("5. Найти сумму, максимум и среднее значение массива из пункта 3")
print("сумма =",     A.sum())
print("максимум =",  A.max())
print("ср. знач. =", A.mean(), '\n')

print("6. Создать функцию который меняет элементы массива на следующее выражение: sin(x)+cos(x)")
def sinpcos(a):
    np.sin(a, out = a)
    a += np.cos(a)
sinpcos(A)
print(A, '\n')

print("7. Создать функцию вычисляющий: a*b+c, где a,b,c - массивы с размером nxn")
def abc(a, b, c):
    return a.dot(b)+c
n = 5
a = np.random.randint(0, 10, (n, n))
print("a=", a)
b = np.random.randint(0, 10, (n, n))
print("b=", b)
c = np.random.randint(0, 10, (n, n))
print("c=", c)
print("a*b+c=", abc(a, b, c), '\n')
    
print("8. Найти определитель матрицы 3x3, если определитель положительный, то найти QR 9. разложение иначе найти обратную матрицу.")
B = 2*np.random.random((3, 3))-1
det = np.linalg.det(B)
print(det)
if det > 0:
    print("QR разложение:\n", np.linalg.qr(B))
else:
    print("Обратная матрица:\n", np.linalg.inv(B), '\n')
   
print("9. Сделать скалярное и матричное умножение двух матриц nxm")
n = 3
m = 4
A = np.random.randint(0, 10, (n, m))
print("A =", A)
B = np.random.randint(0, 10, (n, m))
print("B =", B)
x = np.random.randint(1, 10)
print("x =", x)
print("скалярное умножение x*A:\n", x*A)
B = B.transpose()
print("матричное умножение A*B:\n", A.dot(B), '\n')

print("10. Решить систему линейный уравнений Ax = b, где А(nxn) и b(n) задаются случайно.")
n = 3
A = np.random.random((n,n))
print("A=", A)
b = np.random.random(n)
print("b=", b)
x = np.linalg.solve(A, b)
print("x=", x)