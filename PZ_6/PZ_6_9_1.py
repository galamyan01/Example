# Дан целочисленный список размера 10. Вывести вначале все содержащиеся в данном
# списке четные числа в порядке возрастания их индексов, а затем — все нечетные числа
# в порядке убывания их индексов

import random

spisok = []
chet = []
nechet = []


for i in range(0, 10):
    spisok.append(random.randint(-100, 100))
    if spisok[i] % 2 == 0:
        chet += [spisok[i]]
    elif spisok[i] % 2 == 1:
        nechet += [spisok[i]]


print("Весь список : ", spisok)
print('Все четные числа :', chet)
nechet.reverse()
print("Все не четные числа :", nechet)

