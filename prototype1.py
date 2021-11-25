import tkinter as tk
from tkinter import Entry
from tkinter.ttk import Combobox

billed = ()
bil_l = []
k = 1
l = 1
tol = 0.0
win = tk.Tk()
# Win.geometry("1500x792")
win.title("BILLING SOFTWARE")
win.config(bg="grey")


title = tk.Label(text="SRI ABIRAMI SILKS", font=("comfortaa", 60), bg="grey")
title.grid(column=0, row=0, columnspan=10)
pl = tk.Label(text="Thirubuvanam", font=("comfortaa", 30), bg="grey")
pl.grid(column=1, row=1)

tk.Label(text="NAME:", bg="grey", font=("comfortaa", 30)).grid(column=0, row=3)
name_en = tk.Entry(win, bd=10, font=("comfortaa", 15), justify=tk.CENTER, width=50)
name_en.grid(column=1, row=3, columnspan=4)

tk.Label(text="ADDRESS:", bg="grey", font=("comfortaa", 30)).grid(column=0, row=4)
add_en = tk.Entry(win, bd=10, font=("comfortaa", 15), justify=tk.CENTER, width=50)
add_en.grid(column=1, row=4, columnspan=4)

tk.Label(text="PHONE:", bg="grey", font=("comfortaa", 30)).grid(column=0, row=5)
phone_en = tk.Entry(win, bd=10, font=("comfortaa", 15), justify=tk.CENTER, width=50)
phone_en.grid(column=1, row=5, columnspan=4)

tk.Label(text="saree no", bg="grey", font=("comfortaa", 30)).grid(column=1, row=450)
tk.Label(text="price", bg="grey", font=("comfortaa", 30)).grid(column=2, row=450)

tk.Label(text=f"Sno:{l}", font=("comfortaa", 20)).grid(column=0, row=460)
saree_no = Entry(win, bd=10, font=("comfortaa", 20))
saree_no.grid(column=1, row=460)
price = Entry(win, bd=10, font=("comfortaa", 20))
price.grid(column=2, row=460)

billedc = Combobox(win, values=billed)
billedc.grid(column=1, row=480)


def add_butt():
    global tol
    global l
    global bill_b
    i = []
    a = str(saree_no.get())
    try:
        b = float(price.get())
    except:
        bill_b.config(text="number_pls")
        price.delete(0, 'end')
        add_butt()
    i.append(l)
    i.append(a)
    i.append(b)
    bil_l.append(i)
    saree_no.delete(0, 'end')
    price.delete(0, 'end')
    tol += b
    total.config(text=f"total={tol}")
    history(a, b)
    print(bil_l)
    bill_b.config(text="add")


def history(a, b):
    global billed
    global l
    i = list(billed)
    p = str(l) + " ) " + a + " /" + str(b)
    i.append(p)
    t = tuple(i)
    billed = t
    billedc["values"] = t
    billedc.set(p)
    l += 1


bill_b = tk.Button(text="add", font=("comfortaa", 20), command=add_butt)
bill_b.grid(column=2, row=480)

total = tk.Label(text=f"total={tol}", bg="grey", font=("comfortaa", 30))
total.grid(column=2, row=470)

win.mainloop()
