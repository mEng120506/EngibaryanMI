#Для задачи из блока 1 создать две функции, save_def и load_def, которые позволяют сохранять информацию из экземпляров
# класса (3 шт.) в файл и загружать ее обратно. Использовать модуль pickle для сериализации и десериализации объектов
#Python в бинарном формате.

import pickle

class Zdanie:
    def __init__(self, adres, kolvo_etaj):
        self.adres = adres
        self.kolvo_etaj = kolvo_etaj

def save_def(info_zdanie, fname):
    with open(fname, 'wb') as f:
        pickle.dump(info_zdanie, f)

def load_def(fname):
    with open(fname, 'rb') as f:
        info_zdanie = pickle.load(f)
    return info_zdanie

    def info(self):
        print(f'Адрес: {self.adres}, Количество этажей: {self.kolvo_etaj}')

zdanie1 = Zdanie('ул.Черепахина 29', 18)
zdanie2 = Zdanie('ул.Янтарная 14', 13)
zdanie3 = Zdanie('ул.Пушкинская 8', 7)

info_zdanie = [zdanie1, zdanie2, zdanie3]
save_def(info_zdanie, 'zdanie.pkl')

loaded = load_def('zdanie.pkl')
for i in loaded:
    print(f'Адрес: {i.adres}, Количество этажей: {i.kolvo_etaj}')




