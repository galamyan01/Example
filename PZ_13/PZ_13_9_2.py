# Из заданной строки отобразить только символы нижнего регистра. Использовать
# библиотеку string. Строка 'In PyCharm, you can specify third-party standalone applications and
# run them as External Tools'.

from string import ascii_lowercase

b = 'In PyCharm, you can specify third-party standalone applications andrun them as External Tools'
str_1 = [i for i in b if i in ascii_lowercase]
print(b)
print(str_1)
