import tkinter as tk
import tkinter.ttk as ttk

def NewFlight():
    from Controller import LoadNewFlightPage
    LoadNewFlightPage(mainPage)

def LogBook():
    from Controller import LoadLogBookPage
    LoadLogBookPage(mainPage)
    
def CreateMainPage():
    global mainPage
    mainPage = tk.Tk()
    mainPage.configure(background="midnight blue")
    mainPage.title("RAF Flying Logbook v1")
    """mainPage.geometry('%dx%d+0+0' % (mainPage.winfo_screenwidth(),mainPage.winfo_screenheight()))
    mainPageWidth = mainPage.winfo_screenwidth()
    mainPageHeight = mainPage.winfo_screenheight()"""
    
    FrameTitle = tk.Label(text = "RAF Flight Logbook v1", fg="steel blue", font=("Comic Sans MS", 10),width=50)
    FrameTitle.grid(row=0,column=0,columnspan=4)
    
    TopSpace = tk.Label(text = "", bg="midnight blue")
    TopSpace.grid(row=1,columnspan=4,sticky='ew')
    
    LogBook_btn = tk.Button(text = "Log Book", fg ="black",command=LogBook)
    LogBook_btn.grid(row=2,column=1,columnspan=2,)  
    
    MidTopSpace = tk.Label(text = "", bg="midnight blue")
    MidTopSpace.grid(row=3,columnspan=4,sticky='ew')    
    
    NewFlight_btn = tk.Button(text = "New Flight", fg ="black",command=NewFlight)
    NewFlight_btn.grid(row=4,column=1,columnspan=2,)
    
    MidSpace = tk.Label(text = "", bg="midnight blue")
    MidSpace.grid(row=5,columnspan=4,sticky='ew')
    
    QSummary_btn= tk.Button(text = "Quarterly Summary", fg ="black")
    QSummary_btn.grid(row=6,column=1,columnspan=2,)
    
    BotSpace = tk.Label(text = "", bg="midnight blue")
    BotSpace.grid(row=7,columnspan=4,sticky='ew')
    
    ASummary_btn= tk.Button(text = "Annual Summary", fg ="black")
    ASummary_btn.grid(row=8,column=1,columnspan=2,)
    
    TableSpace = tk.Label(text = "", bg="midnight blue")
    TableSpace.grid(row=9,columnspan=4,sticky='ew')   
    
    Summary = ttk.Treeview(mainPage,height=4)
    Summary["columns"]=("one")
    Summary.heading("#0", text='Type', anchor='w')
    Summary.column("one", width=40)
    Summary.heading("one", text="Hours")
    Summary.insert("", 0,text="Approaches", values=("3"))
    Summary.insert("", 0,text="IF", values=("2"))
    Summary.insert("", 0,text="Night", values=("1"))
    Summary.insert("", 0,text="Day", values=("0"))
    Summary.grid(row=10,column=0,columnspan=3,sticky='e')
    Summary.columnconfigure(0,weight=0)
    
    
    mainPage.mainloop()