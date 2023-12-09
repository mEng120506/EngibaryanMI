#Дан список размера N. Найти количество участков, на которых его элементы монотонно убывают.
def sectors(arr):
    count = 0
    for i in range(1, len(arr)):
        if arr[i] < arr[i-1]:
            count += 1
    return count

arr = [5, 4, 3, 7, 6, 5, 2, 1]
result = sectors(arr)
print("Количество участков, на которых элементы монотонно убывают:", result)