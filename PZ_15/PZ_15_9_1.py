# В матрице элементы второго столбца заменить элементами из одномерного
# массива соответствующей размерности

import numpy as p
import random

i, j = 4, 4
matrix = p.matrix([[random.randrange(0, 10) for x in range(i)] for y in range(j)])
print("Матрица до изменения : \n", matrix)

mas = [random.randrange(0, 10) for x in range(i)]
print("Одномерный массив :", mas)

o = 0

while o < j:
    matrix[o, 1] = mas[o]
    o += 1

print("Матрица после изменения : \n", matrix)
