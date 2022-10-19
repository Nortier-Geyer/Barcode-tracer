#SQL and General imports
from warnings import catch_warnings
import pyodbc
import socket
import os
import Tkinter
from Tkinter import *
import tkMessageBox
from six.moves import input
#Global variaables
Running_Scan  = 1
duplicate_flag = 0
LocalHost = str((socket.gethostname()).upper())

try:
    # Trusted Connection to Named Instance
    connection = pyodbc.connect('Driver={SQL Server}; Server='+LocalHost+'; Database=Barcodes; Trusted_Connection=yes;')
    cursor = connection.cursor()
    print("Logged in as: "+LocalHost)
except Exception:
    print("Couldn't connect to database.")
    Running_Scan = 0 

#Receiving Scanner Data
while Running_Scan:
    try:
        scan_input = str(raw_input('Scan a BARCODE: '))

        if (scan_input == "exit"):
            Running_Scan = 0
            break

        duplicate_flag = cursor.execute("SELECT * FROM Filtered_Barcodes WHERE Barcode = ?",(scan_input)).fetchone()

        if (duplicate_flag):
            #Creating window for tkinter to show popup msg
            Dup_window = Tk()
            Dup_window.withdraw()
            Dup_window.geometry("1x1+"+str(Dup_window.winfo_screenwidth()/2)+"+"+str(Dup_window.winfo_screenheight()/2))
            tkMessageBox.showinfo(title="Error", message="Duplicate value was found!")
            Dup_window.deiconify()
            Dup_window.destroy()
            Dup_window.quit()
        else:
            if  ((scan_input)!="exit"):
                print("Success!")
                cursor.execute("INSERT INTO Filtered_Barcodes (Barcode) VALUES (?)", (scan_input))
                connection.commit()
    except Exception as e:
        print str(e)

if (scan_input == "exit"):
    connection.close()
