from cProfile import label
from tkinter import *


def submit():
    barcode = entry.get() #gets entry text
    print(barcode)

def delete():
    entry.delete(0,END) #Deletes line of text

Input_Window = Tk()
Input_Window.title("Barcode Scanner")

#Creating descriptive label
label = Label(Input_Window,text="Barcode: ")
label.config(font=("Consolas",20))
label.pack(side=LEFT)

#Creating Enter button
submit = Button(Input_Window,text="Enter",command=submit)
submit.pack(side = RIGHT)

#Creating Delete button
delete = Button(Input_Window,text="Re-Do",command=delete)
delete.pack(side = RIGHT)

#Creating text box
entry = Entry()
entry.config(font=('Comic Sans', 20)) #changing font
entry.insert(0,'Scanned Barcode Here') #Default text
entry.config(state=NORMAL) #ACTIVE/DISABLED the input
entry.pack()
Input_Window.mainloop()