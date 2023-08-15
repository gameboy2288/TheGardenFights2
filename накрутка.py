from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Progressbar
import time
import json
import random


with open('users.txt') as json_file2:
    users = json.load(json_file2)
with open('data.txt') as stats1:
    data = json.load(stats1)


window = Tk()
window.title("Взлом игры The Garden Fights")
window.geometry("260x200")


def clicked():
    with open('users.txt') as json_file2:
        users = json.load(json_file2)
    with open('data.txt') as stats1:
        data = json.load(stats1)
    if login.get() in users:
        index = users.index(login.get())
        if index // 4:
            if password.get() in users and users.index(password.get()) == index + 1:
                user_id_reg = users[index + 2]
                if user_id_reg in data:
                    statsindex = data.index(user_id_reg)
                    statsindex += 1
                    if statsindex // 17:
                        hack = int(money.get())
                        if type(hack) is int:
                            barv = 0
                            if barv <= 100:
                                window2 = Tk()
                                window2.title("Взлом игры The Garden Fights")
                                window2.geometry("200x150")
                                lbl5 = Label(window2, text="Загрузка...", font=(30))
                                lbl5.grid()
                                bar = Progressbar(window2, length=200)
                                bar['value'] = 0
                                bar.grid()
                            while barv <= 100:
                                time.sleep(0.006)
                                barv += 0.3
                                bar['value'] = barv
                                bar.update()
                            if barv >= 100:
                                time.sleep(0.1)
                                data[statsindex - 16] += hack
                                bann = random.randint(1, 100)
                                if bann <= 6:
                                    data[statsindex - 17] == 0
                                window2.destroy()
                                with open('data.txt', 'w') as xfile:
                                    json.dump(data, xfile)
                                messagebox.showinfo("Взлом успешен", "Вы успешно накрутили")
                        else:
                            messagebox.showerror("Ошибка", "Неверные данные")
                    else:
                        messagebox.showerror("Ошибка", "Неверные данные")
                else:
                    messagebox.showerror("Ошибка", "Неверные данные")
            else:
                messagebox.showerror("Ошибка", "Неверные данные")
        else:
            messagebox.showerror("Ошибка", "Неверные данные")
    else:
        messagebox.showerror("Ошибка", "Неверные данные")

lbl1 = Label(window, text="Чтобы взломать введите данные:", font=(20))
lbl1.grid(column=0, row=0)
lbl2 = Label(window, text="Логин:", font=(10))
lbl2.grid()
login = Entry(window, width=20)
login.grid()
lbl3 = Label(window, text="Пароль:", font=(10))
lbl3.grid()
password = Entry(window, width=20)
password.grid()
lbl4 = Label(window, text="Накрутить монет:", font=(10))
lbl4.grid()
money = Entry(window, width=20)
money.grid()
btn = Button(window, text="Взломать", width=10, command=clicked)
btn.grid()


window.mainloop()