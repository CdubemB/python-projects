#WRITTEN BY CdubemB

"""
create a programme that can:

gather a sample text with variables
gather variable defintions from the user
decode the text

a tkinter user interface is adviced
"""
from tkinter import 

base =  Tk()

def main():#will run all the following functions
    text_gather()
    translate()
    result()
    base.mainloop()

def text_gather():#will get the text input with the variables from the user
	uLabel = Label(base, text="enter your paragraph with the variables")
	uLabel.pack()
    tBar = Entry(base, width=35, fg="black", borderwidth=5) #creates a text bar for the box
    tBar.grid(row = 0, column = 0, columnspan = 3, padx = 10, pady = 50) #puts the text bar in a specific place
    
def translate():#will translate the given variables that the user inserts
    pass

def result():#will output the translated text
    pass

main()