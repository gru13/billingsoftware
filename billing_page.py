from tkinter import *
from tkinter import font


class billpage :
    def __init__(self) -> None:
        self.current_bill_detail =[]
        self.Win =Tk()
        self.Win["bg"] = None
        #------------ title--------------
        self.title = LabelFrame(self.Win,relief=SOLID, bd=1,highlightcolor="khaki",background="red1")
        self.title.pack(fill=X,padx=1,pady=1)
        Label(self.title,text="Sri ",bg="red1",fg="white" ,font=("Palatino",15,font.BOLD)).pack(anchor=NW)
        Label(self.title,text="Abirami",bg="red1",fg="khaki1",font=("Palatino",30,font.BOLD)).pack(anchor=CENTER)
        Label(self.title,text="Silks",bg="red1",fg="white", font=("Palatino",15,font.BOLD)).pack(anchor=SE)
        # -----------------------------
        # --------body-content---------
        self.body_content = LabelFrame(self.Win)
        self.body_content.pack(fill=X,expand=1)
        # 
        Label(self.body_content,text="Name",font=("planatino",15))
        self.cust_name = Entry(self.body_content)
        self.cust_name
        # 
        Label(self.body_content,text="Number",font=("planatino",15))
        self.cust_num = Entry(self.body_content)
        self.cust_num
        #    
        Label(self.body_content,text="Address",font=("planatino",15)).pack(side=BOTTOM,anchor=SW)
        self.cust_add = Entry(self.body_content,width=50)
        self.cust_add.pack(side=BOTTOM,anchor=SW)
    
        
        
        self.Win.mainloop()
billpage()    
