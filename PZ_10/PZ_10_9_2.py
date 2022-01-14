# Из предложенного текстового файла (text18-9.txt) вывести на экран его содержимое,
# количество букв в нижнем регистре. Сформировать новый файл, в который поместить текст
# в стихотворной форме предварительно поставив последнюю строку фразой введенной
# пользователем.

mal = 0

for i in open('text18-9.txt', encoding='UTF-8'):
    print(i, end='')
    for m in i:
        l = m.islower()
        if l:
            mal += 1
print("\nКоличество букв в нижнем регистре :", mal)

d = input("Введите фразу , которая будет последней строкой : ")
l = open("text.txt", "w", encoding="UTF-8")
for i in open('text18-9.txt', encoding='UTF-8'):
    l.write(i)

f1 = open('text18-9.txt', encoding='UTF-8')
l = f1.readlines()
l[6] = d
f1.close()

f2 = open('text.txt', "w", encoding='UTF-8')
f2.writelines(l)
f2.close()
