import tkinter as tk
from tkinter import messagebox  
import sqlite3

def login():
    Service_NoE.get()
    password_entry.get()
    con = sqlite3.connect('Flying_logbook.db')
    with con:
        cur = con.cursor()    
        result = cur.execute("SELECT ServiceNo, password " 
                    "FROM Users WHERE ServiceNo = ?",(Service_NoE.get(),))
        result = cur.fetchone()
        if result is not None:
            Service_NoE.get() == "ServiceNo"
            if password_entry.get() == "password":
                messagebox.showinfo("--Login--", "Correct Login Details", icon="info")
                from Controller import LoadMainPage
                LoadMainPage(lpge)
            else:
                messagebox.showinfo("--User--", "There is a User, incorrect password")
                DeleteFields()
        else:
            messagebox.showinfo("--User--", " Incorrect Username")
            DeleteFields()
            
def Newuser():
     from Controller import LoadNewUserPage
     LoadNewUserPage(lpge)
    
def CreateLoginPage():
    global lpge
    lpge = tk.Tk()                        
    lpge.configure(background="Grey82")
    lpge.resizable(width=False, height=False)
    lpge.title("Login Page")                   
    lpge.geometry('{}x{}'.format(330, 200)) 
    """create all of the main containers"""
    top_frame = tk.Frame(lpge, bg='Grey82', width = 325, height=100, pady=3)
    center = tk.Frame(lpge, bg='Grey82', width=325, height=150, pady=3)
    btm_frame = tk.Frame(lpge, bg='Grey82', width = 325, height = 50, pady=3)
    btm_frame1 = tk.Frame(lpge, bg='Grey82', width = 325, height = 50)
    top_frame.grid(row=0, sticky="ew")
    center.grid(row=1, sticky="nsew")
    btm_frame.grid(row = 2, sticky="ew")
    top_frame.grid_rowconfigure(1, weight = 3)
    top_frame.grid_columnconfigure(0, weight = 3)
    center.grid_rowconfigure(1, weight = 2)
    center.grid_columnconfigure(1, weight = 2)
    btm_frame.grid_rowconfigure(1, weight = 1)
    btm_frame.grid_columnconfigure(0, weight = 3)
    btm_frame1.grid_rowconfigure(1, weight = 1)
    btm_frame1.grid_columnconfigure(1, weight = 3)
    """ create the widgets for the top frame & layout the widgets in the top frame """
    title = tk.Label(top_frame, text = "RAF Flight Logbook v1", bg="Grey82", font=("Comic Sans MS", 20), height=1, width=20)    
    instructions = tk.Label(top_frame, text = "Please Login to continue", bg="Grey82", font=("Arial", 10), pady=2)
    title.grid(row = 0, columnspan = 3)
    instructions.grid(row = 1, column = 0)
    """ create the widgets for the center frame """
    ctr_left = tk.Frame(center, bg='Grey82', width=160, height=50)
    ctr_right = tk.Frame(center, bg='Grey82', width=162, height=50)
    ctr_left.grid(row=0, column = 0, sticky="ew")
    ctr_right.grid(row=0, column = 2, sticky="ew")
    """ entry """
    global Service_NoE
    global password_entry 
    Service_NoE = tk.Entry(ctr_right, width=30)
    password_entry = tk.Entry(ctr_right, width=30, show="*") 
    Service_NoE.grid(row = 0, column = 3)
    password_entry.grid(row = 1, column = 3) 
    user = tk.Label(ctr_left, text = "Service Number", bg="Grey82", padx = 25, anchor='w')
    user.grid(row=0, column=0)
    pword = tk.Label(ctr_left, text = "Password", bg="Grey82", padx = 25, anchor='w')
    pword.grid(row=1, column=0)
    lgn_btn = tk.Button(btm_frame, text = "Login", command=login, height = 1, width = 15)
    n_user_btn = tk.Button(btm_frame, text = "New User", command = Newuser, height = 1, width = 15)
    lgn_btn.grid(row=0, column=2)
    n_user_btn.grid(row=1, column=2)
    lpge.mainloop()                            #draw the window and Start the app
        
def DeleteFields():
    Service_NoE.delete(0, 'end')
    password_entry.delete(0, 'end')
    