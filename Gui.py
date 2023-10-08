from tkinter import *
from tkinter import ttk
import random

count = 0
x = 'user.txt'

root = Tk()
root.title("Менеджер паролей")
root.geometry("300x300")


def win():
    return True


def start_game():
    window1 = Toplevel()
    window1.title("Сначала набери 5 очков!")
    c = Canvas(window1, width=500, height=500, bg="white")
    p = Canvas(window1, width=500, height=100, bg="blue")
    lbl = ttk.Label(window1, text="КЛИКАЙ НА ШАРИКИ!", font="Arial 30", anchor="s")
    c.pack()
    p.pack()
    lbl.pack()
    window1.grab_set()
    colors = ["red", "blue", "green", "yellow", "orange"]

    def ball():
        c.delete(ALL)
        x = random.randint(20, 480)
        y = random.randint(20, 480)
        r = 30
        new_ball = c.create_oval(x - r, y - r, x + r, y + r, fill=random.choice(colors), width=0)
        c.tag_bind(new_ball, "<Button-1>", click_ball)
        window1.after(1000, ball)

    def click_ball(event):
        global count
        count += 1
        p.delete(ALL)
        p.create_text(80, 30, font="Arial 20", text="Points:")
        p.create_text(180, 30, font="Arial 22", text=str(count))
        if count >= 5:
            window1.destroy()

    ddd = win()
    ball()
    btn.config(state="normal")
    print(ddd)
    return ddd


def PasswordsDisplay(x):
    if x == '':
        return False
    else:
        with open(x, "r") as file:
            text = file.read()
            file.close()
        return text


btn = ttk.Button(text="Показать пароли", command=lambda: PasswordsDisplay(x), state="disabled")
btn.pack()  # размещение в окне
btn1 = ttk.Button(text="Выполнить задание", command=start_game)
btn1.pack()

root.mainloop()
