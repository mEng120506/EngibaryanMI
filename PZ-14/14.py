#В исходном текстовом файле(Dostoevsky.txt) найти все варианты фамилии Достоевского (т.е. с различными окончаниями,
# например, Достоевский, Достоевского) в единственном экземпляре.

import re

with open('Dostoevsky.txt', 'r') as file:
    text = file.read()

matches = re.findall(r'Достоевск\w+', text)

unique_matches = list(set(matches))

for match in unique_matches:
    print(match)