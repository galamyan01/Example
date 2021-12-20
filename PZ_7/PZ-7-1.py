#Дано целое число N (>0) и строка S. Преобразовать строку S в строку длины N
#следующим образом: если длина строки S больше N, то отбросить первые символы,
#если длина строки S меньше N, то в ее начало добавить символы «.» (точка).

import random
ru_letters = u"абвгдежзийклмнопрстуфхцчшщъыьэюяАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
en_letters = u"abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
tj_letters = u"ғӣқӯҳҷҒӢҚӮҲҶ"
digits = u"0123456789"
letters = ru_letters + en_letters + tj_letters + digits
N = random.randrange(1,21)
K = random.randrange(1,21)
S = ''.join(random.choice(letters) for _ in range(K))
print("N:",N)
print("K:",K)
print("S:",S)
S_length = len(S)
print("Length of S:",S_length)
if S_length > N:
    x = S_length - N
    S_new = S[x:]
    #print(x,":",S[x:])
else:
    x = N - S_length
    S_new = '.'*x + S
    #print(x,":",'.'*x,":",S)
print("\nNew S:",S_new)
print("Length of new S:",len(S_new))