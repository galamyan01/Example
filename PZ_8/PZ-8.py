# Дана строка 'апельсины 45 991 63 100 12 яблоки 13 47 26 0 16',
# отражающая продажи продукции по дням в кг. Преобразовать информацию из
# строки в словари, с использованием функции найти среднее значение продаж по
# каждому виду продукции, результаты вывести на экран

def poisk():
    slog = 0
    kol = 0
    for i in a[:5]:
        slog += int(i)
        kol += 1
    s1 = slog // kol
    print("Среднее значение продаж по апельсинам:", s1)
    slog1 = 0
    kol1 = 0
    for i in a[6:10]:
        slog1 += int(i)
        kol1 += 1
    s2 = slog1 // kol1
    print("Среднее значение продаж по яблокам: ", s2)

slovar = {}
fruit = ("апельсины 45 991 63 100 12 яблоки 13 47 26 0 16")    # продажи продукции по дням в кг
a = fruit.split()[1:]

slovar['Понедельник апельсины'] = a[0]
slovar['Второник апельсины'] = a[1]
slovar['Среда апельсины'] = a[2]
slovar['Четверг апельсины'] = a[3]
slovar['Пятница апельсины'] = a[4]
slovar['Понедельник яблоки'] = a[6]
slovar['Второник яблоки'] = a[7]
slovar['Среда яблоки'] = a[8]
slovar['Четверг яблоки'] = a[9]
slovar['Пятница яблоки'] = a[10]

print(slovar)
print()    # Пустой принт для переноса строки
print(poisk())