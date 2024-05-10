#Создайте базовый класс "Животное" со свойствами "вид", "количество лап", "цвет шерсти".
#От этого класса унаследуйте класс "Собака" и добавьте в него свойства "кличка" и "порода".

class Zhivotnoe:
    def __init__(self, vid, kolichestvo_lap, cvet_shersti):
        self.vid = vid
        self.kolichestvo_lap = kolichestvo_lap
        self.cvet_shersti = cvet_shersti

class Sobaka(Zhivotnoe):
    def __init__(self, vid, kolichestvo_lap, cvet_shersti, klichka, poroda):
        Zhivotnoe.__init__(self, vid, kolichestvo_lap, cvet_shersti)
        self.klichka = klichka
        self.poroda = poroda

sobaka1 = Sobaka("Собака", 4, "рыжий", "Тузик", "Такса")
print(sobaka1.vid)
print(sobaka1.kolichestvo_lap)
print(sobaka1.cvet_shersti)
print(sobaka1.klichka)
print(sobaka1.poroda)