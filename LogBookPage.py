import tkinter as tk

def ReturnMainPage():
    from Controller import LoadMainPage
    LoadMainPage(lbPage)

def CreateLogBookPage():
    global lbPage
    lbPage = tk.Tk()
    lbPage.configure(background="midnight blue")
    lbPage.title("Log Book")

    Return_btn= tk.Button(text = "Return", fg ="black", command=ReturnMainPage)
    Return_btn.grid(row=8,column=1,columnspan=2,)
    
    lbPage.mainloop()
