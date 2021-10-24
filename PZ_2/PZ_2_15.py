A = input("Введите трехзначное число")
while type(A) != int:
    try:
        A = int(A)
    except ValueError:
        print("Вы ввели не целое число")
        A = input("Введите целое число A")
if 1000 > A > 99:
    print(A % 10 * 10 + A % 100 // 10)
elif -1000 < A < -99:
    print(-(-A % 10 * 10 + -A % 100 // 10))
else:
    print("Введено не трехзначное число")
