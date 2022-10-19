from tkinter import *

def Start_Scanning():
#***********Text box***********************
    def submit():
        barcode = entry.get() #gets entry text
        print(barcode)

    def delete():
        entry.delete(0,END) #Deletes line of text

    Input_Window = Toplevel(root)
    Input_Window.title("Barcode Scanner")
    Input_Window.geometry("500x30")

    #Creating descriptive label
    label = Label(Input_Window,text="Barcode: ")
    label.config(font=("Consolas",20))
    label.pack(side=LEFT)

    #Creating Enter button
    submit = Button(Input_Window,text="Enter",command=submit)
    submit.pack(side=RIGHT)

    #Creating Delete button
    delete = Button(Input_Window,text="Re-Do",command=delete)
    delete.pack(side=RIGHT)

    #Creating text box
    entry = Entry(Input_Window)
    entry.config(font=('Comic Sans', 20)) #changing font
    #entry.insert(0,'Scanned Barcode Here') #Default text
    entry.config(state=NORMAL) #ACTIVE/DISABLED the input
    entry.pack()

#***********Text box END***********************






root = Tk()
root.title('Simple Barcode Duplication Checker')
#root.iconbitmap('database_logo.png') #creates an icon
root.geometry("800x500")
root.config

#Define image
bg = PhotoImage(file = "Dup_Check_Backgnd.png")

#Create a canvas
my_canvas = Canvas(root, width=800, height=500)
my_canvas.pack(fill="both", expand=True)

# Set image in canvas
my_canvas.create_image(0,0, image=bg, anchor="nw")

#   Add a label
my_canvas.create_text(400, 150, text="Welcome!", font=("Arial rounded", 30), fill="white")
my_canvas.create_text(400, 250, text="Press the \"Start Scanning\" button to scan a barcode", font=("Arial rounded", 15), fill="red")

# Add buttons
button1 = Button(root, text="Start Scanning", command=Start_Scanning)
button2 = Button(root, text="Exit", command=exit)

button1_window = my_canvas.create_window(300, 300, anchor="nw", window=button1)
button2_window = my_canvas.create_window(450, 300, anchor="nw", window=button2)


root.mainloop()