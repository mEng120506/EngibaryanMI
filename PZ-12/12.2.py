#Из заданной строки отобразить только символы нижнего регистра. Использовать библиотеку string. Строка'In PyCharm,
#you can specify third-party standalone applications and run them as External Tools'.

import  string
stroka = 'In PyCharm, you can specify third-party standalone applications and run them as External Tools'
a = [i for i in stroka if i in string.ascii_lowercase]
print(a)


