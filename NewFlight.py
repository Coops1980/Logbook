import tkinter as tk
import InputCalendar as ICal
import sqlite3
from tkinter import messagebox  

def LoadCalendar(self):
    ICal.load()

def EnterDate(TkinterWindow, SelectedDay, SelectedMonth, SelectedYear):
    TkinterWindow.destroy()
    DateE.delete(0, 'end')
    DateE.insert(10, (str(SelectedDay) + " " + SelectedMonth + " " + str(SelectedYear)))

def ReturnMainPage():
    from Controller import LoadMainPage
    LoadMainPage(nfPage)

def DeleteFields():
    DateE.delete(0, 'end')
    ACTypeE.delete(0, 'end')
    ACNumE.delete(0, 'end')
    CaptainE.delete(0, 'end')
    CPilotE.delete(0, 'end')
    DutyE.delete(0, 'end')
    D1stE.delete(0, 'end')
    D2ndE.delete(0, 'end')
    DDualE.delete(0, 'end')
    N1stE.delete(0, 'end')
    N2ndE.delete(0, 'end')
    NDualE.delete(0, 'end')
    FTTotalE.delete(0, 'end')
    FTCaptainE.delete(0, 'end')
    IFSimE.delete(0, 'end')
    IFActualE.delete(0, 'end')
    IFAppE.delete(0, 'end')
    IFNoE.delete(0, 'end')
    
def SaveNewFlight():
    flights = (
    (DateE.get()),
    (ACTypeE.get()),
    (ACNumE.get()),
    (CaptainE.get()),
    (CPilotE.get()),
    (DutyE.get()),
    (D1stE.get()),
    (D2ndE.get()),
    (DDualE.get()),
    (N1stE.get()), 
    (N2ndE.get()),
    (NDualE.get()),
    (FTTotalE.get()),
    (FTCaptainE.get()),
    (IFSimE.get()),
    (IFActualE.get()),
    (IFAppE.get()),
    (IFNoE.get()),
    (SpareE.get())
    )
    con = sqlite3.connect('Flying_logbook.db')
    with con:
        cur = con.cursor()    
        cur.execute("INSERT INTO Coops VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", flights)
    messagebox.showinfo("--Saved---", "Flight Saved", icon="info")
    """from Controller import LoadMainPage
    LoadMainPage(nfPage)"""
    DeleteFields()
    

def CreateNewFlightPage():
    global nfPage
    nfPage = tk.Tk()
    nfPage.configure(background="midnight blue")
    nfPage.title("New Flight")
    
    ColumnSpacing = tk.Label(text = "", bg="midnight blue",width=1)
    ColumnSpacing.grid(column=1,sticky ='ns')
    ColumnSpacing = tk.Label(text = "", bg="midnight blue",width=1)
    ColumnSpacing.grid(column=3,sticky ='ns')
    
    TitleLabel = tk.Label(text = "New Flight", bg="red", font=("Comic Sans MS", 18), anchor = 'center')
    TitleLabel.grid(row=0,columnspan=3,sticky='ew') 
    
    Row1 = tk.Label(text = "Date Select", fg="green", bg="midnight blue", font=("Comic Sans MS Bold", 12), anchor = 'w')
    Row1.grid(row=1,column=0,sticky='w')
    global DateE
    DateE = tk.Entry(width=20)
    DateE.grid(row=1,column=2)
    DateE.bind('<Button-1>', LoadCalendar)
    
    Row2 = tk.Label(text = "Aircraft Type ", fg="green", bg="midnight blue", font=("Comic Sans MS Bold", 12))
    Row2.grid(row=2,column=0,sticky='w')
    global ACTypeE
    ACTypeE = tk.Entry(width=20)
    ACTypeE.grid(row=2,column=2)
    
    Row3 = tk.Label(text = "Aircraft Number ", fg="green", bg="midnight blue", font=("Comic Sans MS Bold", 12))
    Row3.grid(row=3,column=0,sticky='w')
    global ACNumE
    ACNumE = tk.Entry(width=20)
    ACNumE.grid(row=3,column=2)    
        
    Row4 = tk.Label(text = "Captain ", fg="green", bg="midnight blue", font=("Comic Sans MS Bold", 12))
    Row4.grid(row=4,column=0,sticky='w')
    global CaptainE
    CaptainE = tk.Entry(width=20)
    CaptainE.grid(row=4,column=2)
    
    Row5 = tk.Label(text = "Co-Pilot ", fg="green", bg="midnight blue", font=("Comic Sans MS Bold", 12))
    Row5.grid(row=5,column=0,sticky='w')
    global CPilotE
    CPilotE = tk.Entry(width=20)
    CPilotE.grid(row=5,column=2)
    
    Row6 = tk.Label(text = "Duty ", fg="green", bg="midnight blue", font=("Comic Sans MS Bold", 12))
    Row6.grid(row=6,column=0,sticky='w')
    global DutyE
    DutyE = tk.Entry(width=20)
    DutyE.grid(row=6,column=2)    
    
    Row7 = tk.Label(text = "Day Flying", fg="green", bg="midnight blue", font=("Comic Sans MS Bold", 12))
    Row7.grid(row=7,column=0,sticky='w')
    Row8 = tk.Label(text = "1st", fg="green", bg="midnight blue", font=("Comic Sans MS", 8))
    Row8.grid(row=8,column=0)
    global D1stE
    D1stE = tk.Entry(width=20)
    D1stE.grid(row=8,column=2)  
    Row9 = tk.Label(text = "2nd", fg="green", bg="midnight blue", font=("Comic Sans MS", 8))
    Row9.grid(row=9,column=0)
    global D2ndE
    D2ndE = tk.Entry(width=20)
    D2ndE.grid(row=9,column=2)  
    Row10 = tk.Label(text = "Dual", fg="green", bg="midnight blue", font=("Comic Sans MS", 8))
    Row10.grid(row=10,column=0)    
    global DDualE
    DDualE = tk.Entry(width=20)
    DDualE.grid(row=10,column=2) 

    Row11 = tk.Label(text = "Night Flying", fg="green", bg="midnight blue", font=("Comic Sans MS Bold", 12))
    Row11.grid(row=11,column=0,sticky='w')
    Row12 = tk.Label(text = "1st", fg="green", bg="midnight blue", font=("Comic Sans MS", 8))
    Row12.grid(row=12,column=0)
    global N1stE
    N1stE = tk.Entry(width=20)
    N1stE.grid(row=12,column=2)  
    Row13 = tk.Label(text = "2nd", fg="green", bg="midnight blue", font=("Comic Sans MS", 8))
    Row13.grid(row=13,column=0)
    global N2ndE
    N2ndE = tk.Entry(width=20)
    N2ndE.grid(row=13,column=2)  
    Row14 = tk.Label(text = "Dual", fg="green", bg="midnight blue", font=("Comic Sans MS", 8))
    Row14.grid(row=14,column=0)    
    global NDualE
    NDualE = tk.Entry(width=20)
    NDualE.grid(row=14,column=2) 
    
    Row15 = tk.Label(text = "Flight Time", fg="green", bg="midnight blue", font=("Comic Sans MS Bold", 12))
    Row15.grid(row=15,column=0,sticky='w')
    Row16 = tk.Label(text = "Total", fg="green", bg="midnight blue", font=("Comic Sans MS", 8))
    Row16.grid(row=16,column=0)
    global FTTotalE
    FTTotalE = tk.Entry(width=20)
    FTTotalE.grid(row=16,column=2)  
    Row17 = tk.Label(text = "Captain", fg="green", bg="midnight blue", font=("Comic Sans MS", 8))
    Row17.grid(row=17,column=0)
    global FTCaptainE
    FTCaptainE = tk.Entry(width=20)
    FTCaptainE.grid(row=17,column=2)      
    
    Row18 = tk.Label(text = "Instrument Flying", fg="green", bg="midnight blue", font=("Comic Sans MS Bold", 12))
    Row18.grid(row=18,column=0,sticky='w')
    Row19 = tk.Label(text = "Sim", fg="green", bg="midnight blue", font=("Comic Sans MS", 8))
    Row19.grid(row=19,column=0)
    global IFSimE
    IFSimE = tk.Entry(width=20)
    IFSimE.grid(row=19,column=2)  
    Row20 = tk.Label(text = "Actual", fg="green", bg="midnight blue", font=("Comic Sans MS", 8))
    Row20.grid(row=20,column=0)
    global IFActualE
    IFActualE = tk.Entry(width=20)
    IFActualE.grid(row=20,column=2)
    
    Row21 = tk.Label(text = "Instrument Approaches", fg="green", bg="midnight blue", font=("Comic Sans MS Bold", 12))
    Row21.grid(row=21,column=0,sticky='w')
    Row22 = tk.Label(text = "Type", fg="green", bg="midnight blue", font=("Comic Sans MS", 8))
    Row22.grid(row=22,column=0)
    global IFAppE
    IFAppE = tk.Entry(width=20)
    IFAppE.grid(row=22,column=2)  
    Row23 = tk.Label(text = "No", fg="green", bg="midnight blue", font=("Comic Sans MS", 8))
    Row23.grid(row=23,column=0)
    global IFNoE
    IFNoE = tk.Entry(width=20)
    IFNoE.grid(row=23,column=2)
    
    Row24 = tk.Label(text = "Spare", fg="green", bg="midnight blue", font=("Comic Sans MS Bold", 12))
    Row24.grid(row=24,column=0,sticky='w')
    global SpareE
    SpareE = tk.Entry(width=20)
    SpareE.grid(row=24,column=2)
    
    Save_btn = tk.Button(text = "Save Flight", fg ="black",command=SaveNewFlight, anchor ='w')
    Save_btn.grid(row=25,column=2,columnspan=2, sticky ='e')
    
    Return_btn = tk.Button(text = "Return", fg ="black",command=ReturnMainPage, anchor ='e')
    Return_btn.grid(row=25,column=0,columnspan=2, sticky ='w')    
       
    nfPage.mainloop()
    

