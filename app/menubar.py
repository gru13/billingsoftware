from tkinter import *
# from openpyxl import load_workbook
from datetime import datetime
from tkinter.messagebox import *
from os import startfile
from tkinter import font
from setting_page import database_input_setting
from main_menu_page import main_menu

class menu_bar:
    def __init__(self, Win, file, curent_window):
        self.file_data = file
        self.load_file = load_workbook(self.file_data)
        self.sheets = self.load_file.sheetnames
        self.curentwidow = curent_window
        self.font = font.Font(size=20, family="Times")
        self.Win = Win
        self.menubar = Menu(self.Win, activebackground="red")
        self.menubar["font"] = self.font
        self.Win.config(menu=self.menubar)#
        self.menubar.add_command(label='\u2302', command=self.go_to_main_menu)
        self.menubar.add_command(label='\u27F3', command=self.refresh)
        self.menubar.add_command(label="\u2699", command=database_input_setting)
        self.open_file = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="open", menu=self.open_file)
        self.open_file.add_command(label=f"open:{self.sheets} data base",
                                   command=lambda: startfile(self.file_data))
        self.open_file.add_separator()

    def go_to_main_menu(self):
        self.Win.destroy()
        main_menu(self.file_data)


    def refresh(self):
        self.Win.destroy()
        # self.Win.menu.destroy()
        self.curentwidow(self.file_data)
