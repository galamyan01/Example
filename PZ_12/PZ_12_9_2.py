# Разработать программу с применением пакета tk, взяв в качестве условия одну
# любую задачу из ПЗ №№ 3 – 8.

#  Даны два целых числа: A, B . Проверить истинность высказывания: «Хотя бы одно из чисел A и B нечетное».

from tkinter import *


def count_num(event):
    t = 0
    r = 0

    n1 = int(num1.get())
    n2 = int(num2.get())

    if n1 % 2 == 0:
        t += 1
    elif n1 % 2 == 1:
        r += 1

    if n2 % 2 == 0:
        t += 1
    elif n2 % 2 == 1:
        r += 1

    positive['text'] = "Четные", t
    negative['text'] = "Нечетные", r
    res['text'] = "Истина:", r > 0


root = Tk()
root.title("Истинность высказывания: «Хотя бы одно из чисел нечетное»")
root.geometry("420x300")

Label(text="Первое число").grid(row=1, column=0)
num1 = Entry()
num1.grid(row=1, column=1)

Label(text="Второе число").grid(row=2, column=0)
num2 = Entry()
num2.grid(row=2, column=1)

button1 = Button(text="Обработать")
button1.grid(row=4, column=1)

positive = Label()
positive.grid(row=5, column=1)

negative = Label()
negative.grid(row=6, column=1)

res = Label()
res.grid(row=7, column=1)

button1.bind('<Button-1>', count_num)

root.mainloop()
