from tkinter import *
from tkinter import ttk
import random

co, count = 0, 0
x = 'user.txt'

root = Tk()
root.title("Менеджер паролей")
root.geometry("300x300")


def win():
    return True


def start_game(co):
    try:
        if co != 0:
            return False
        else:
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
    except TclError as e:
        return True


def PasswordsDisplay(x):
    try:
        if x != 'user.txt':
            return False
        editor = Text()
        editor.pack(fill=BOTH, expand=1)
        with open(x, "r") as file:
            text = file.read()
            editor.delete("1.0", END)
            editor.insert("1.0", text)
            file.close()

        # сохраняем текст из текстового поля в файл
        def save_file():
            text = editor.get("1.0", END)
            with open(x, "w") as file:
                file.write(text)

        save_button = ttk.Button(text="Сохранить файл", command=save_file)
        save_button.place(relx=1, rely=0.9, anchor='ne')

        def readnew():
            with open(x, "r") as file:
                text1 = file.read()
                file.close()
            return text1

        txt =readnew()
        return txt
    except Exception as e:
        return None



btn = ttk.Button(text="Показать пароли", command=lambda: PasswordsDisplay(x), state="disabled")
btn.pack()  # размещение в окне
btn1 = ttk.Button(text="Выполнить задание", command=lambda: start_game(co))
btn1.pack()

root.mainloop()
