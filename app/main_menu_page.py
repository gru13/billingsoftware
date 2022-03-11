from tkinter import *
from openpyxl import load_workbook
from datetime import datetime
from tkinter.messagebox import *
from os import startfile
from tkinter import font
from menubar import menu_bar
from bill_menu_page import bill_menu

class main_menu:
    def __init__(self, file_data):
        self.Win_main_menu = Tk()
        self.file = file_data
        self.menu = menu_bar(self.Win_main_menu, self.file, main_menu)
        self.bill_menu_button = Button(self.Win_main_menu, text="BILL MENU", font=("ARIAL", 20, "bold"),
                                       command=self.go_to_bil_menu)
        self.bill_menu_button.grid(column=0, row=0)
        self.Win_main_menu.mainloop()

    def go_to_bil_menu(self):
        self.Win_main_menu.destroy()
        bill_menu(self.file)
