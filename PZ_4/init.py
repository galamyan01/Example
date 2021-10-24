a = int(input("Введите первое число : "))
b = int(input("Введите второе число : "))
c = int(input("Введите третье число : "))
d = int(input("Введите четвертое число : "))

k = 0
res = 0
if a < 0:
    k += 1
    res += a
if b < 0:
    k += 1
    res += b
if d < 0:
    k += 1
    res += d
if c < 0:
    k += 1
    res += c
print("количество ", k)
print("Сумма ", res)

