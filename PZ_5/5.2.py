# Описать функцию Swap(X,Y), меняющую содержимое переменных Х и У (Х и У- вещественные параметры,являющиеся одновременно
# входными и выходными). С ее помощью для данных переменных А, B, C, D последовательно поменять содержимое следующих
# пар: А и В, С и D, В и С и вывести новые значения А, В, С, D.
def Swap(X, Y):
    return Y, X #возвращает в обратном порядке

def Change():
    A = 1.7
    B = 2.8
    C = 3.2
    D = 4.1

    A, B = Swap(A, B)
    C, D = Swap(C, D)
    B, C = Swap(B, C)

    print("Новые значения переменных:")
    print("A =", A)
    print("B =", B)
    print("C =", C)
    print("D =", D)

Change()
