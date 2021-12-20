# Найти сумму чисел ряда 1,2,3,4,... от числа n до числа m. Суммирование оформить функцией с параметрами.
# Значения n и m программа должна запрашивать.

# Ввод первого значения
n = input("Введите первое число: ")
# Блок исключения
while type(n) != int:
    try:
        n = int(n)
    except ValueError:
        print("!!!Не верный тип данных!!!")
        n = input("Введите первое число: ")

# Ввод первого значения
m = input("Введите второе число: ")
# Блок исключения
while type(m) != int:
    try:
        m = int(m)
    except ValueError:
        print("!!!Не верный тип данных!!!")
        m = input("Введите второе число: ")

# UFO
a = n

print(n, a)

# Функция
def summ(n, m, a):
    while n < m:
        n += 1
        a += n
        print(n,   a)
    return n, m, a

print (summ(n , m, a))