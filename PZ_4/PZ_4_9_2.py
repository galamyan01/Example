import random

A = random.randrange(2, 200)
print('A = ', A)

K = 1
S = 1
while S <= A:
    K += 1
    S += K
print("K =", K, " , S =", S)
