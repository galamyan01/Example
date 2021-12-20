# Даны два списка А и Б одинакового рамера N. Сформировать новый список С того же размера,
# каждый элемент которого равен максимальному из элементов сипска А и B.
import random

n = int(input("Задайте рамеры списков: "))

a = []
b = []
c = []
while n > 0:
    a.append(random.randrange(0, 100))
    b.append(random.randrange(0, 100))
    n -= 1

s = max(a)
d = max(b)
c.append(s)
c.append(d)

print(a)
print(b)

print(max(a))
print(max(b))
print(list (c))
