#В матрице элементы третьей строки заменить элементами из одномерного динамического массива соответствующей размерности.
matrix = [[x * y for x in range(2, 5)] for y in range(2, 5)]

array = [10, 11, 12]

new_matrix = [array if i == 2 else a for i, a in enumerate(matrix)]

print("Матрица с замененной третьей строкой:")
for a in new_matrix:
    print(a)
