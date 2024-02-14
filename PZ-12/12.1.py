#.Даны две последовательности. Найти элементы, общие для двух последовательностей и их количество.
def main():
    a = list(map(int, input("Введите первую последовательность чисел через пробел: ").split()))
    b = list(map(int, input("Введите вторую последовательность чисел через пробел: ").split()))

    elements = set(a) & set(b)
    yield list(elements)
    yield len(elements)

if __name__ == "__main__":
    result = main()
    print("Общие элементы для двух последовательностей:", next(result))
    print("Количество общих элементов:", next(result))
