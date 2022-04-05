# В матрице найти среднее арифметическое положительных элементов, кратных 3

import random

i, j = 3, 3
matrix = [[random.randrange(-10, 10) for x in range(i)] for y in range(j)]
print("Матрица имеет вид :")
for i in matrix:
    print(i)

sum = 0
kol = 0

for n in matrix:
    for b in n:
        if b > 0:
            if b % 3 == 0:
                sum += b
                kol += 1

print("Сумма элементов кратных 3 =", sum)
print("Колличество эллементов кратных 3 =", kol)
if kol == 0:
    kol = 1
print("Среднее арифметическое положительных элементов, кратных 3 = ", sum / kol)
