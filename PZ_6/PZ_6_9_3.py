# Дано множество A из N точек на плоскости и точка B (точки заданы своими
# координатами х, у). Найти точку из множества A, наиболее близкую к точке B.
# Расстояние R между точками с координатами (x1, y1) и (x2, у2) вычисляется по формуле:
# R = √(x2 – x1)2 + (у2 – y1)2


import random
import math

n = int(input("Введите количество точек : "))
A = []
N = []
x = []
y = []

while n > 0:
    a = random.randrange(-100, 100)
    b = random.randrange(-100, 100)
    x += [a]
    y += [b]
    N = [a, b]
    A += [N]
    n -= 1

print("Множество А из точек N : ", A)

l = random.randrange(-100, 100)
k = random.randrange(-100, 100)
B = [l, k]

print("Точка B : ", B)


so = []
sa = []
rast = []

for i in x:
    sa.append((l - i) ** 2)

for p in y:
    so.append((k - p) ** 2)


rast += [int(math.sqrt(x+y)) for x, y in zip(so, sa)]


print("Ближайшая точка к точке B под номером : ", rast.index(min(rast))+1)
print("Растояние от нее до точки B  = ", min(rast))
