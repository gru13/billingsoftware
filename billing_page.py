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
        Label(self.title,text="Sri ",bg="red1",fg="white" ,font=("Palatino",15,font.BOLD)).pack(anchor="nw")
        Label(self.title,text="Abirami",bg="red1",fg="khaki1",font=("Palatino",30,font.BOLD)).pack(anchor="center")
        Label(self.title,text="Silks",bg="red1",fg="white", font=("Palatino",15,font.BOLD)).pack(anchor="se")
        # -----------------------------
        # --------body-content---------
        self.body_content = LabelFrame(self.Win)
        self.body_content.pack(fill=X)
        # 
        Label(self.body_content,text="Name").grid(sticky=N)
        self.cust_name = Entry(self.body_content)
        self.cust_name.grid(sticky=N)
        # 
        Label(self.body_content,text="Number").grid(sticky=N)
        self.cust_num = Entry(self.body_content)
        self.cust_num.grid(sticky=N)
        # 
        Label(self.body_content,text="Address").grid(sticky=N)
        self.cust_add = Entry(self.body_content)
        self.cust_add.grid(sticky=N)
        
        
        
        self.Win.mainloop()
billpage()    
