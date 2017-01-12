from Tkinter import * #gives us access to everything in the Tkinter class
import tkMessageBox
from PIL import Image, ImageTk

def buttonpress1():
    entrytxt = entry1.get()
    print entrytxt
    tkMessageBox.showinfo("Here's what you typed", entrytxt)





root = Tk() #gives us a blank canvas object to work with
root.title("Tic Tac Toe")
 
button1 = Button(root, bg="light grey", command=buttonpress1)
button1.grid(row=3, column=0, columnspan=2, sticky=EW, rowspan = 10)

label1 = Label(root, bg="lavender", anchor=W)
label1.grid(row=2, column=12, sticky=EW, columnspan=3)
 
 
 
 


mainloop() #causes the windows to display on the screen until program closes