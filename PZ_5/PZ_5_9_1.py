# Составить программу, в которой функция генерирует четырехзначное число
# И определяет,есть ли в числе одинаковые цифры .

import random


def search_number():
    b = random.randrange(1000, 9999)
    print("Сгенерированое число = ", b)
    if b // 1000 == b % 10:    # Сравниение Первой и последней цифры
        print("Есть одинаковые числа")
    elif b // 1000 == b // 100 % 10:    # Сравнение первой и второй цифры
        print("Есть одинаковые числа")
    elif b // 1000 == b // 10 % 10:    # Сравнение первой и третьей цифры
        print("Есть одинаковые числа")
    elif b // 100 % 10 == b % 10:    # Сравнение второй и последней цифры
        print("Есть одинаковые числа")
    elif b // 100 % 10 == b // 10 % 10:    # Сравнеине второй 
        print("Есть одинаковые числа")
    elif b // 10 % 10 == b % 10:    #
        print("Есть одинаковые числа")
    else:
        print("Одинаковых чисел нет")


print(search_number())
