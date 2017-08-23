import tkinter as tk
from tkinter import messagebox  
import sqlite3

def CreateNewUserPage():
    Sqns = ["29 Sqn", "3 Sqn", "11 Sqn", "6 Sqn", "1 Sqn", "2 Sqn"]
    Rank = ["Plt Off", "Fg Off", "Flt Lt", "Sqn Ldr", "Wg Cdr", "Gp Capt"]
    
    global Nuser_Page
    Nuser_Page = tk.Tk()                        
    Nuser_Page.configure(background="Grey82")
    Nuser_Page.title("New User")                   
    Nuser_Page.geometry('{}x{}'.format(340, 275)) 
    ColumnSpacing = tk.Label(text = "", bg="Grey82",width=1)
    ColumnSpacing.grid(column=1,sticky ='ns')
    ColumnSpacing = tk.Label(text = "", bg="Grey82",width=1)
    ColumnSpacing.grid(column=3,sticky ='ns')
    
    TitleLabel = tk.Label(text = "New User", bg="Grey82", font=("Comic Sans MS", 18), anchor = 'center')
    TitleLabel.grid(row=0,columnspan=4,sticky='ew') 
    
    global name_1stE
    Row1 = tk.Label(text = "First Name", fg="green", bg="Grey82", font=("Comic Sans MS Bold", 12), anchor = 'w')
    Row1.grid(row=1,column=0,sticky='w')
    name_1stE = tk.Entry(width=30)
    name_1stE.grid(row=1,column=2)
    
    global surnameE
    Row2 = tk.Label(text = "Surname", fg="green", bg="Grey82", font=("Comic Sans MS Bold", 12), anchor = 'w')
    Row2.grid(row=2,column=0,sticky='w')
    surnameE = tk.Entry(width=30)
    surnameE.grid(row=2,column=2)
    
    global ServiceNoE
    Row2 = tk.Label(text = "Service Number", fg="green", bg="Grey82", font=("Comic Sans MS Bold", 12), anchor = 'w')
    Row2.grid(row=3,column=0,sticky='w')
    ServiceNoE = tk.Entry(width=30)
    ServiceNoE.grid(row=3,column=2)
    
    global RankE
    Row3 = tk.Label(text = "Rank", fg="green", bg="Grey82", font=("Comic Sans MS Bold", 12))
    Row3.grid(row=4,column=0,sticky='w')
    RankE = tk.Spinbox(width = 28, values = Rank)
    RankE.grid(row=4,column=2)
   
    global DOBE
    Row4 = tk.Label(text = "Date of Birth", fg="green", bg="Grey82", font=("Comic Sans MS Bold", 12))
    Row4.grid(row=5,column=0,sticky='w')
    DOBE = tk.Entry(width=30)
    DOBE.grid(row=5,column=2)    
    
    global SqnE
    Row5 = tk.Label(text = "Squadron", fg="green", bg="Grey82", font=("Comic Sans MS Bold", 12))
    Row5.grid(row=6,column=0,sticky='w')
    SqnE = tk.Spinbox(width = 28, values = Sqns)
    SqnE.grid(row=6,column=2)
    
    global PwordE
    Row1 = tk.Label(text = "Password", fg="green", bg="Grey82", font=("Comic Sans MS Bold", 12), anchor = 'w')
    Row1.grid(row=7,column=0,sticky='w')
    PwordE = tk.Entry(width=30, show='*')
    PwordE.grid(row=7,column=2)
    
    Save_btn = tk.Button(text = "Save User", fg ="black", anchor ='w', command = input_user)
    Save_btn.grid(row=9,column=2,columnspan=1, sticky ='e')      
    Return_btn = tk.Button(text = "Return", fg ="black",command = CloseNU, anchor ='e')
    Return_btn.grid(row=9,column=2,columnspan=1, sticky ='w')
    
    Nuser_Page.mainloop()

def CloseNU():
    from Controller import LoadLoginPage
    LoadLoginPage(Nuser_Page)
    
def input_user():   
    User = (
    (name_1stE.get()),
    (surnameE.get()),
    (ServiceNoE.get()),
    (RankE.get()),
    (DOBE.get()),
    (SqnE.get()),
    (PwordE.get())
    )
    con = sqlite3.connect('Flying_logbook.db')
    with con:
        cur = con.cursor()    
        cur.execute("INSERT INTO Users VALUES(?, ?, ?, ?, ?, ?, ?)", User)       
        messagebox.showinfo("--Saved---", "User Saved", icon="info")
        table_name = (ServiceNoE.get())
        new_table_name = "Logbook_" + str(table_name)
        cur = con.cursor()    
        cur.execute("""
        CREATE TABLE if not exists """ + new_table_name + """(
        [Date]               DATETIME,
        [Aircraft Type]      STRING,
        [Aircraft Number]    STRING,
        [Captain]            STRING,
        [Copilot/2nd Pilot]  STRING,
        [Duty]               TEXT,
        [Day 1st Pilot]      TIME,
        [Day 2nd Pilot]      TIME,
        [Day Dual]           TIME,
        [Night 1st Pilot]    TIME,
        [Night 2nd Pilot]    TIME,
        [Night Dual]         TIME,
        [Total Flying]       TIME,
        [Total Captain]      TIME,
        [IF Simulated]       TIME,
        [IF Actual]          TIME,
        [IF Approach Type]   STRING,
        [IF Approach Number] INTEGER,
        [Spare]              STRING
        );""")
        con.commit()
    DeleteFields()
    CloseNU()
    
def DeleteFields():
    name_1stE.delete(0, 'end')
    surnameE.delete(0, 'end')
    ServiceNoE.delete(0, 'end')
    RankE.delete(0, 'end')
    DOBE.delete(0, 'end')
    SqnE.delete(0, 'end')
    PwordE.delete(0, 'end')
    
