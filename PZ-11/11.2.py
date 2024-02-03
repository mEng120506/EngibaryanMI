#Из предложенного текстового файла (text18-10.txt) вывести на экран его содержимое,
#количество букв в верхнем регистре. Сформировать новый файл, в который поместить текст
#в стихотворной форме предварительно поставив после последней строки автора и название

with open('text18-10 (1).txt', 'r', encoding='utf16') as file:
    content = file.read()
    print(content)
upper_case = sum(1 for char in content if char.isupper())
print(f"Количество букв в верхнем регистре: {upper_case}")

poem = """
Автор: М.Ю.Лермонтов
Название: "Бородино"
"""

with open('poem.txt', 'w') as file:
    file.write(content.strip() + poem)

