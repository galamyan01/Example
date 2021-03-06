# Средствами языка Python сформировать текстовый файл (.txt), содержащий
# последовательность из целых положительных и отрицательных чисел. Сформировать
# новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
# обработку элементов:
# Исходные данные:
# Количество элементов:
# Индекс последнего максимального элемента:
# Меняем местами первую и последнюю трети:


# Запишем в файл data_3.txt структуру данных - список
l = ['23 6 14 -36 41 -45 10 -15']
f3 = open('data_3.txt', 'w')
f3.writelines(l)
f3.close()

# Дублируем список в новый файл data_4.txt
f4 = open('data_4.txt', 'w', encoding="utf-8")
f4.write('Исходные данные: ')
f4.write('')
f4.writelines(l)
f4.close()

# разбиваем строку и ее значения преобразуем в числа
f3 = open('data_3.txt', encoding="utf-8")
k = f3.read()
k = k.split()
for i in range(len(k)):
    k[i] = int(k[i])
f3.close()

# Ищем максимальный элемент и количество отрицательных элементов
# в файле data_3.txt и записываем в файл data_4.txt
f3 = open('data_3.txt', encoding="utf-8")
m = 0
t = 0
for i in range(len(k)):
    m = m if m > k[i] else k[i]
    if int(k[i]) < 0:
        t += 1

f4 = open('data_4.txt', 'a', encoding="utf-8")  # открываем файл для дозаписи
f4.write('\n')
print('Количество элементов: ', len(k), file=f4)
f4.close()

f4 = open('data_4.txt', 'a', encoding="utf-8")  # открываем файл для дозаписи
f4.write('')
print('Индекс последнего максимального элемента: ', k.index(max(k))+1, file=f4)
f4.close()

f4 = open('data_4.txt', 'a', encoding="utf-8")  # открываем файл для дозаписи
f4.write('')
k[0], k[5], k[1], k[6], k[2], k[7] = k[5], k[0], k[6], k[1], k[7], k[2]
print('Меняем местами первую и последнюю трети: ', k, file=f4)
f4.close()

