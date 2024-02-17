#Дана строка, содержащая полное имя файла, то есть имя диска, список каталогов (путь), собственно имя и расширение.
# Выделить из этой строки имя файла (без расширения).
file_name = "C:/Users/Documents/example.txt"
file_parts = file_name.split("/")
full_file_name = file_parts[-1]
file = full_file_name.split(".")[0]
print(file)
