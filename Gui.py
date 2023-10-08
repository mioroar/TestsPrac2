from tkinter import *
from tkinter import ttk

import random
root = Tk()
root.title("Менеджер паролей")
root.geometry("300x300")

def start_game():
    count = 0
    print('Набирание 5 очков!')
    for i in range(5):
        count += 1
    if count >= 5:
        return True
        print('Победа')
    else:
        return False


print(start_game())

def PasswordsDisplay(x):
    if x == '':
        return False
    else:
        with open(x, "r") as file:
            text = file.read()
            file.close()
        return text

print(PasswordsDisplay('user.txt'))
print(PasswordsDisplay(''))


btn = ttk.Button(text="Показать пароли", command=lambda: PasswordsDisplay(x), state="disabled")
btn.pack()  # размещение в окне
btn1 = ttk.Button(text="Выполнить задание", command=start_game)
btn1.pack()

root.mainloop()
