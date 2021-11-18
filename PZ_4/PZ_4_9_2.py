# Дано число A (> 1).
# Вывести наименьшее из целых чисел K, для которых сумма 1 + 1/2 + ... + 1/K будет больше A, и саму эту сумму.

import random

A = random.randrange(2, 200)
print('A = ', A)

K = 1
S = 1
while S <= A:
    K += 1
    S += K
print("K =", K, " , S =", S)
