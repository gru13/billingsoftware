from tkinter import *
from tkinter.messagebox import showerror
from openpyxl import load_workbook

class database_input_setting:
    def __init__(self):
        self.file_data = open(r"database input file")
        self.file_data = self.file_data.read().split("||")
        self.config_window = Tk()
        #
        self.file_frame = LabelFrame(self.config_window)
        self.file_frame.grid(column=0,row=0)
        self.billing_page_name_config_frame = LabelFrame(self.config_window,text="billing_page")
        self.billing_page_name_config_frame.grid(column=0,row=1)
        self.database_page_name_config_frame = LabelFrame(self.config_window, text="database_page")
        self.database_page_name_config_frame.grid(column=1,row=1)
        #######
        #######convert the raw data
        #######
        for a in range(1, len(self.file_data)):
            de = self.file_data[a]
            de = de.split(",")
            file_dict = {}
            for b in de:
                j = b.split(":")
                file_dict[j[0]] = j[1]
            self.file_data[a] = file_dict
        print(self.file_data)
        ########
        ########
        ########d
        ########
        database_filename = self.file_data[0]
        database_name = self.file_data[1]
        # for a in (d:= database_filename):
        #     s = d[a]
        #     d[a] = Entry
        billing_page_name = self.file_data[2]
        ######
        self.config_window.title("configure")
        self.config_window.iconbitmap("Settings2.ico")
        ######
        Label(self.file_frame, text="filename:").grid(column=0, row=0)
        Label(self.file_frame, text=database_filename).grid(column=1, row=0)
        ######
        self.database_page_name_config_frame.grid(column=0, row=1)
        ######
        self.billing_page_name_config_frame.grid(column=1, row=1)
        #####
        r = 0 # this for layout the window in row and column
        #####
        d=database_name
        for a in d:
            Label(self.database_page_name_config_frame, text=a).grid(row=r,column=0)
            Label(self.database_page_name_config_frame, text=d[a]).grid(row=r,column=1)
            r += 1


        last_string = str(database_filename) + '||SAREE NO:' + str(database_name["SAREE NO"]) + ",Date:" + str(database_name['Date']) + ",Name:" + str(database_name["Name"]) + ",Design:" + str(database_name['Design']) + ",Purchase Amount:" + str(database_name["Purchase Amount"]) + ",DATE OF SALE:" + str(database_name["DATE OF SALE"]) + ",SALE PRICE:" + str(database_name["SALE PRICE"]) + ",CUSTOMER NAME:" + str(database_name["CUSTOMER NAME"]) + ",CUSTOMER NUMBER:" + str(database_name["CUSTOMER NUMBER"]) + ",ADDRESS:" + str(database_name["ADDRESS"]) + ",BILL NO:" + str(database_name["BILL NO"]) + "||BILL NO:" + str(billing_page_name["BILL NO"]) + ",SAREE NO:" + str(billing_page_name["SAREE NO"]) + ",CUSTOMER NAME:" + str(billing_page_name["CUSTOMER NAME"]) + ",DATE OF SALE:" + str(["DATE OF SALE"]) + ",DESIGN:" + str(billing_page_name["DESIGN"]) + ",SOLD PRICE:" + str(billing_page_name["SOLD PRICE"]) + ",TOTAL OF BILL:" + str(billing_page_name["TOTAL OF BILL"])
        self.config_window.mainloop()

    def save(self, file, text):
        pass