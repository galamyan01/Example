# Даны два целых числа: A, B. Проверить истинность высказывания: «Хотя бы одно из чисел A и B нечетное».
import random

A = random.randrange(1, 100)
print("A =", A)
B = random.randrange(1, 100)
print("B =", B)
print("A нечетно: ", (A % 2) == 1)
print("B нечетно: ", (B % 2) == 1)
print("Хотя бы одно из чисел A и B нечетное: ", (A % 2) == 1 or (B % 2) == 1)
