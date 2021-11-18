# Описать функцию Swap(X, Y), меняющую содержимое переменных X и Y
# (X и Y — вещественные параметры, являющиеся одновременно входными и выходными).
# С ее помощью для данных переменных A, B, C, D последовательно поменять содержимое следующих пар:
# A и B, C и D, B и C и вывести новые значения A, B, C, D .

import random


def Swap(k):
    k[0], k[1] = k[1], k[0]
    return k


A = random.randrange(-100, 100)
B = random.randrange(-100, 100)
C = random.randrange(-100, 100)
D = random.randrange(-100, 100)

print("A = ", A)
print("B = ", B)
print("C = ", C)
print("D = ", D)
print()

k = [A, B]
A, B = Swap(k)
k = [C, D]
C, D = Swap(k)
k = [B, C]
B, C = Swap(k)

print("A = ", A)
print("B = ", B)
print("C = ", C)
print("D = ", D)
