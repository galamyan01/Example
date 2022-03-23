# В исходном текстовом файле (Dostoevsky.txt) найти все варианты фамилии
# Достоевского (т.е. с различными окончаниями, например, Достоевский,
# Достоевского) в единственном экземпляре

import re


with open('Dostoevsky.txt', 'r', encoding='utf-8') as file:
    text = file.read()
    reg_name = re.findall(r"Достоевск[ий|ая|ие|ого]+ ", text)
    print(set(reg_name))


