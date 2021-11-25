from tkinter import *
from openpyxl import *
from datetime import datetime

database = load_workbook("SAREE DATABASE.xlsx")
database_sheet = database.active
Win = Tk()
Win["bg"] = "grey"
#
billed_saree = []
sarees_detail = dict()
total = 0
for a in "ABCDEFG":
    #  append the value to dict as in form as
    __ = [a.value for a in database_sheet[a]]
    sarees_detail[__[0]] = __[1:]
# print(sarees_detail)
"""
PURCHASE PRICE	COLOUR	DESIGN	SALE PRICE	DATE OF SALE	CUSTOMER NAME	CUSTOMER NUM	ADDRESS	BILL NUMBER	PROFIT

"""
saree_no_list = [str(a) for a in sarees_detail["SAREE NUMBER"]]
# def login():
#     d = Tk()
#     Button(d, text="hi", command=lambda: d.destroy()).pack()
#     Win.after(1000, func=login)
#
customer_name = Entry(Win, relief="sunken", justify="center")
customer_name.grid(column=1, row=1)
#
customer_number = Entry(Win, relief="sunken", justify="center")
customer_number.grid(column=3, row=1)
#
customer_address = Entry(Win, width=40, relief="sunken", justify="center")
customer_address.grid(column=1, row=2, columnspan=4)
#
saree_no_entry = Entry(Win)
saree_no_entry.grid(column=1, row=3)
#

# labels
Label(Win, text="Abirami silks", bg="grey", font=("algerian", 43)).grid(column=0, row=0, columnspan=200)
Label(Win, text="Name:", bg="grey").grid(column=0, row=1)
Label(Win, text="Number:", bg="grey").grid(column=2, row=1)
Label(Win, text="Address:", bg="grey").grid(column=0, row=2)
Label(Win, text="Sno").grid(column=0, row=4)
Label(Win, text="colour").grid(column=1, row=4)
Label(Win, text="design").grid(column=2, row=4)
Label(Win, text="price").grid(column=3, row=4)


# Label(Win, text="Saree No:", bg="grey").grid(column=0, row=3)


# function
def bill_():
    d = datetime.now()
    date = str(d.strftime("%d")) + str(d.strftime("%b")) + str(d.strftime("%Y"))
    global total
    for ab in range(1, len(billed_saree) + 1):
        billed_saree[ab - 1] += [float(globals()[str(ab) + "price"].get())]
        total += float(globals()[str(ab) + "price"].get())
        database_sheet["G" + str(billed_saree[ab - 1][0] + 2)] = float(globals()[str(ab) + "price"].get())
        database_sheet["H" + str(billed_saree[ab - 1][0] + 2)] = date
        database_sheet["I" + str(billed_saree[ab - 1][0] + 2)] = customer_name.get()
        database_sheet["J" + str(billed_saree[ab - 1][0] + 2)] = customer_number.get()
        database_sheet["K" + str(billed_saree[ab - 1][0] + 2)] = customer_address.get()

    Label(text=str(total)).grid(column=10, row=1000)
    # print(billed_saree)
    database.save("SAREE DATABASE.xlsx")


def saree_no():
    saree_number = saree_no_entry.get()
    saree_no_entry.delete(0, END)
    saree_number = saree_no_list.index(saree_number)
    sno = len(billed_saree) + 1
    colour = sarees_detail["COLOUR"][saree_number]
    design = sarees_detail["DESIGN"][saree_number]
    Label(text=str(sno)).grid(column=0, row=5 + (len(billed_saree)))
    Label(text=colour).grid(column=1, row=5 + (len(billed_saree)))
    Label(text=design).grid(column=2, row=5 + (len(billed_saree)))
    globals()[str(sno) + "price"] = Entry(Win)
    globals()[str(sno) + "price"].grid(column=3, row=5 + (len(billed_saree)))
    billed_saree.append([saree_number, colour, design])

    # print(billed_saree)


#  buttons
saree_entry = Button(text="saree no", command=saree_no)
saree_entry.grid(column=0, row=3)
bill = Button(Win, text="BILL", command=bill_).grid(column=1000, row=1000)
#
Win.mainloop()
