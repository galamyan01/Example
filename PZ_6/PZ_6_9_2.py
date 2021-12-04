# Дан список размера N. Найти количество участков, на которых его элементы
# монотонно убывают.

import random

n = int(input("Введите размер списка N = "))
spisok = []
i = 0

while i < n:
    spisok.append(random.randint(-100, 100))
    i += 1

print(spisok)


t = 0
for i in range(0, n):
    if spisok[i-1] < spisok[i]:
        if True:
            t += 1
        else:
            False
    else:
         False
print("Колличесвто участков с монотоным убыванием = :", t)


