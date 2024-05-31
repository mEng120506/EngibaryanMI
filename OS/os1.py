import os

#print("Текущая директория:", os.getcwd())

#os.mkdir("folder")

if not os.path.isdir("folder"):
    os.mkdir("folder")

#os.chdir("folder")
#print("Текущая директория изменилась на folder:", os.getcwd())

#os.chdir("..")
#print("Текущая директория изменилась на:", os.getcwd())

#os.makedirs("nested1/nested2/nested3")


#text_file = open("text.txt", "w")
#text_file.write("Это текстовый файл")
#text_file.close()

#os.rename("text.txt", "renamed-text.txt")

#os.replace("renamed-text.txt", "folder/renamed-text.txt")

#print("Все папки и файлы: ", os.listdir())

#for dirpath, dirnames, filenames in os.walk("."):
 #   for dirname in dirnames:
  #      print("Каталог: ", os.path.join(dirpath, dirname))

#for filename in filenames:
 #   print("Файл: ", os.path.join(dirpath, filename))

#os.remove("folder/renamed-text.txt")

#os.rmdir("folder")

#os.removedirs("nested1/nested2/nested3")

#print(os.stat("text.txt"))

#print("Размер файла:", os.stat("text.txt").st_size)
