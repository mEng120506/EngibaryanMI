#. Разработать программу с применением пакета tk, взяв в качестве условия одну любую задачу из ПЗ №№ 2 – 9.
# Дано целое число A. Проверить истинность высказывания: «Число A является положительным».
import tkinter as tk

def check_positive():
    try:
        number = int(entry.get())
        if number > 0:
            result_label.config(text="Число является положительным")
        else:
            result_label.config(text="Число не является положительным")
    except ValueError:
        result_label.config(text="Введите целое число")

root = tk.Tk()
root.title("Проверка числа на положительность")

label = tk.Label(root, text="Введите число:")
label.pack()

entry = tk.Entry(root)
entry.pack()

check_button = tk.Button(root, text="Проверить", command=check_positive)
check_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()