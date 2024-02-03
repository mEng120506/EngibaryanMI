#Средствами языка Python сформировать текстовый файл (.txt), содержащий
#последовательность из целых положительных и отрицательных чисел. Сформировать
#новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую обработку элементов:
#Исходные данные:
#Количество элементов:
#Элементы в обратном порядке:
#Сумма элементов последней половины:

numbers = ['1 2 3 -5 -6 8']
f3 = open('data_3.txt', 'w')
f3.writelines(numbers)
f3.close()

f4 = open('data_4.txt', 'w')
f4.write('Исходные данные: ')
f4.write('\n')
f4.writelines(numbers)
f4.close()

f3 = open('data_3.txt')
k = f3.read()
k = k.split()
for i in range(len(k)):
 k[i] = int(k[i])
f3.close()


f3 = open('data_3.txt')
reversed_k = k[::-1]
f3.close()

middle = len(k) // 2
summa = sum(k[middle:])

f4 = open('data_4.txt', 'a')
f4.write('\n')
print('Количество элементов: ', len(k), 'Элементы в обратном порядке:', reversed_k, file=f4 )
f4.write('\n')
f4.write('Сумма элементов последней половины: ' + str(summa))
f4.close()

