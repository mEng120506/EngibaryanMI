#В матрице найти среднее арифметическое положительных элементов.
matrix = [[x * y for x in range(2, 5)] for y in range(-1, 2)]
print("Матрица:")
for line in matrix:
    print(line)

positive_elements = [element for line in matrix for element in line if element > 0]

if positive_elements:
    sredni_positive = sum(positive_elements) / len(positive_elements)
    print("Среднее арифметическое положительных элементов: ", sredni_positive)
else:
    print("В матрице нет положительных элементов.")
