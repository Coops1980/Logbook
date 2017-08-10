import sqlite3

def create_table(db_name,table_name,sql):
    with sqlite3.connect(db_name) as db:
       cursor = db.cursor()
       cursor.execute("Select name from sqlite_master where name=?",(table_name,))
       result = cursor.fetchall()
       keep_table = True
       if len(result) == 1:
           response = input("The table {0} already exists, do you wish to recreate it (y\n): ".format(table_name))
           if response == "y":
               keep_table = False
               print("The {0} table will be recreated - all existing data will be lost".format(table_name))
               cursor.execute("drop table if exists {0}".format(table_name))
               db.commit()
           else:
               print("The existing table was kept")
       else:
           keep_table = False
       if not keep_table:
           cursor.execute(sql)
           db.commit()
        
if __name__ == "__main__":
    db_name = ("Flying_logbook.db")
    table_name = input("Name: ")
    sql = """
        CREATE TABLE """ + table_name + """(
        [Date]               DATETIME PRIMARY KEY,
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
        [IF Approach Number] INTEGER
        );"""
    create_table(db_name,table_name,sql)
