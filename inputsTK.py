#creating a calculator on python
from tkinter import * #imports the tkinter module

base = Tk()

e = Entry(base, width=50, fg="black", borderwidth=2) #creats a search bar
e.pack()

def uClick():
   uLabel = Label(base, text=e.get())
   uLabel.pack() #creats a string of text

uButton = Button(base, text="Enter name user NO.18", command=uClick)
uButton.pack() #creates a button which will run a function

base.mainloop()