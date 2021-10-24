A = input("Введите целое число A")
while type(A) != int:
    try:
        A = int(A)
    except ValueError:
        print("Вы ввели не целое число")
        A = input("Введите целое число A")
if A > 0:
    pass
else:
    print("Введенно не положительное число")
B = input("Введите целое число B")
while type(B) != int:
    try:
        B = int(B)
    except ValueError:
        print("Вы ввели не целое число")
        B = input("Введите целое число B")
if B > 0:
    pass
else:
    print("Введенно не положительное число")
if A > 0 and B > 0:
    if A > B:
        print("Длина незанятой части отрезка A :", A % B)
    else:
        if A < B or A == B:  # В случае если A меньше B или A равно B :
            print("Отрезок B накладывается на отрезок A , остатка нет")
else:
    print("Не возможно выполнение , не соблюденно условие")
