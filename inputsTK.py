#creating a calculator on python
from tkinter import * #imports the tkinter module

base = Tk()

e = Entry(base, width=50, fg="black", borderwidth=2) #creates a search bar
e.insert(0, "Enter your name:")# e.insert gives presest text in the box (0 represents the index)
e.pack()

def uClick():
   greeting = "good morrow " + e.get() #.get() gets the text inside of the Entry/text bar
   uLabel = Label(base, text=greeting)
   uLabel.pack() #creates a string of text

uButton = Button(base, text="Enter name user NO.18", command=uClick)
uButton.pack() #creates a button which will run a function

base.mainloop()