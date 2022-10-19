#SQL and General imports
import pyodbc
import socket
import os
from urllib import response

#GUI Imports
import tkinter
from tkinter import *
from tkinter import messagebox

#Global variaables
scan_input = ''
Running_Scan  = 1
duplicate_flag = 0
LocalHost = 'HI-TACK-LABELS'

# Trusted Connection to Named Instance
connection = pyodbc.connect('Driver={SQL Server}; Server='+LocalHost+'\SQLEXPRESS; Database=Barcodes; Trusted_Connection=yes;')
cursor = connection.cursor()
print("Logged in as: ", (LocalHost))


#Receiving Scanner Data
while Running_Scan:
    scan_input = str(input('Scan a BARCODE: '))

    duplicate_flag = cursor.execute("SELECT * FROM Filtered_Barcodes WHERE Barcode = ?", (scan_input)).fetchone()

    if ("" == (scan_input)):
        print("Something went wrong! Please Check you're Barcode.")
    else:
        if (duplicate_flag):
            #Creating window for tkinter to show popup msg
            Dup_window = Tk()
            Dup_window.eval('tk::PlaceWindow %s center' % Dup_window.winfo_toplevel())
            Dup_window.withdraw()
            messagebox.showinfo('Error', 'Duplicate value was found')
            Dup_window.deiconify()
            Dup_window.destroy()
            Dup_window.quit()
        else:
            if  ("q" != (scan_input)):
                print("Success!")
                cursor.execute("INSERT INTO Filtered_Barcodes (Barcode) VALUES (?)", (scan_input))
                connection.commit()

    if (scan_input == "q"):
        Running_Scan = 0


connection.close()