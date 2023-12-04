#Составить программу, в которой функция генерирует четырехзначное число и определяет, есть ли в числе одинаковые цифры.

import random

def check_duplicates(number):
    digits = [int(a) for a in str(number)]
    return len(digits) != len(set(digits)) #set - множество

number = random.randint(1000, 9999)
print("Сгенерированное число:", number)

if check_duplicates(number):
    print("В числе есть одинаковые цифры.")
else:
    print("В числе нет одинаковых цифр.")
