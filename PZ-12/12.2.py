#Из заданной строки отобразить только символы нижнего регистра. Использовать библиотеку string. Строка'In PyCharm,
#you can specify third-party standalone applications and run them as External Tools'.

import  string
str = 'In PyCharm, you can specify third-party standalone applications and run them as External Tools'
a = [i for i in str if i in string.ascii_lowercase]
print(a)


