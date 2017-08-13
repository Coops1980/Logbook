import sqlite3

flights = (
    (input(str("Date: ")),
    input(str("A/C Type: ")),
    input(str("A/C Num: ")),
    input(str("Capt Name: ")),
    input(str("Co Name: ")),
    input(str("Duty: ")), 
    input(str("Day 1st: ")), 
    input(str("Day 2nd: ")), 
    input(str("Day Dual: ")), 
    input(str("Night 1st: ")),
    input(str("Night 2nd: ")),
    input(str("Night Dual: ")),
    input(str("Total Flight: ")),
    input(str("Total Captain: ")),
    input(str("IF Simulated: ")),
    input(str("IF Actual: ")),
    input(str("IF Approach Type: ")),
    input(str("IF Approach Numbers: "))))

con = sqlite3.connect('Flying_logbook.db')
with con:
    cur = con.cursor()    
    cur.execute("INSERT INTO Coops VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", flights)
    
# input_data working, need to find out how to enter minutes and hours
# this is the basic input, needs to be adjusted for different tables