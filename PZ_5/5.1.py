#Составить программу, в которой функция генерирует четырехзначное число и определяет, есть ли в числе одинаковые цифры.
import random # импортируем модуль random для генерации случайных чисел

def generate_number():
    return random.randint(1000, 9999) # генерируем четырехзначное случайное число

def check_duplicates(number): # объявляем функцию check_duplicates с аргументом number
    digits = [int(a) for a in str(number)] # преобразуем число в список цифр
    return len(digits) != len(set(digits)) # возвращаем True, если есть одинаковые цифры, иначе False

number = generate_number()  # вызываем функцию generate_number и сохраняем результат в переменной number
print("Сгенерированное число:", number)

if check_duplicates(number): # проверяем наличие одинаковых цифр в числе с помощью функции check_duplicates
    print("В числе есть одинаковые цифры.")
else:
    print("В числе нет одинаковых цифр.")

