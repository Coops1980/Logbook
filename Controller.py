import Login as log
import Main as Main
import LogBookPage as LB
import NewFlight as NF
import NewUser as NU

def LoadMainPage(TkinterWindow):
    TkinterWindow.destroy()
    Main.CreateMainPage()
    
def LoadNewFlightPage(TkinterWindow):
    TkinterWindow.destroy()
    NF.CreateNewFlightPage()

def LoadLogBookPage(TkinterWindow):
    TkinterWindow.destroy()
    LB.CreateLogBookPage()

def LoadNewUserPage(TkinterWindow):
    TkinterWindow.destroy()
    NU.CreateNewUserPage()
    
def LoadLoginPage(TkinterWindow):
    TkinterWindow.destroy()
    log.CreateLoginPage()
    
if __name__ == "__main__":
    log.CreateLoginPage()
# -*- coding: utf-8 -*-

