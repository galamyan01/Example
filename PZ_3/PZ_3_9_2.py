# Арифметические действия над числами пронумерованы следующим образом:
# 1 — сложение, 2 — вычитание, 3 — умножение, 4 — деление.
# Дан номер действия N (целое число в диапазоне 1-4) и вещественные числа A и B (В не равно 0)
# Выполнить над числами указанное действие и вывести результат.

import random

n = int(input("Введите номер действия : "))
a = random.randrange(-100, 100)
print("Значение переменной A  = ", a)
b = random.randrange(-100, 100)
print("Значение переменной B = ", b)
if b != 0:
    if n == 1:
        print(a + b)
    elif n == 2:
        print(a - b)
    elif n == 3:
        print(a * b)
    elif n == 4:
        print(a / b)
else:
    print("Не соблюденно условие")