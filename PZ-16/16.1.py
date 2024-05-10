#Создайте класс "Здание" с атрибутами "адрес" и "количество этажей". Напишите метод, который выводит информацию о
# здании в формате "Адрес: адрес, Количество этажей: этажи".

class Zdanie:
    def __init__(self, adres, kolvo_etaj):
        self.adres = adres
        self.kolvo_etaj = kolvo_etaj

    def info(self):
        print(f'Адрес: {self.adres}, Количество этажей: {self.kolvo_etaj}')


zdanie1 = Zdanie('ул.Черепахина 29', 18)
zdanie2 = Zdanie('ул.Янтарная 14', 13)
zdanie1.info()
zdanie2.info()