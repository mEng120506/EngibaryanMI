#Дан целочисленный список размера 10.Вывести вначале все содержащиеся в данном списке четные числа в порядке возрастания
# их индексов, а затем все нечетные числа в порядке убывания их индексов.
numbers = [2, 5, 8, 10, 13, 15, 17, 20, 22, 25]

even_numbers = [numbers[i] for i in range(len(numbers)) if numbers[i] % 2 == 0]
odd_numbers = [numbers[i] for i in range(len(numbers)) if numbers[i] % 2 != 0]

even_numbers.sort()
odd_numbers.sort(reverse=True)

print("Четные числа в порядке возрастания их индексов:")
for num in even_numbers:
    print(num)

print(" Нечетные числа в порядке убывания их индексов:")
for num in odd_numbers:
    print(num)