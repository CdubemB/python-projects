#creating a calculator on python
from tkinter import * #imports the tkinter module

base = Tk()

tBar = Entry(base, width=35, fg="black", borderwidth=5) #creates a search bar
tBar.grid(row = 0, column = 0, columnspan = 3, padx = 10, pady = 10)

def button_click(number):
    cCursor = tBar.get()
    tBar.delete(0, END)
    tBar.insert(0, str(cCursor) + str(number))
#This makes buttons input text

def button_clear():
     tBar.delete(0, END)
#allows the clear button to work

def button_add():
    firstNumber = tBar.get()
    global fNum
    global math
    math = "addition"
    fNum = int(firstNumber)
    tBar.delete(0, END)
#Initiates addition
def button_subtract():
    firstNumber = tBar.get()
    global fNum
    global math
    math = "subtraction"
    fNum = int(firstNumber)
    tBar.delete(0, END)
#initiates subtraction
def button_multiply():
    firstNumber = tBar.get()
    global fNum
    global math
    math = "multiplication"
    fNum = int(firstNumber)
    tBar.delete(0, END)
#initiates multiplication
def button_divide():
    firstNumber = tBar.get()
    global fNum
    global math
    math = "division"
    fNum = int(firstNumber)
    tBar.delete(0, END)
#initiates division

def button_equal():
    secondNumber = tBar.get()
    tBar.delete(0, END)
    if math == "addition":
        tBar.insert(0, fNum + int(secondNumber))
    if math == "subtraction":
        tBar.insert(0, fNum - int(secondNumber))
    if math == "multiplication":
        tBar.insert(0, fNum * int(secondNumber))
    if math == "division":
        tBar.insert(0, fNum / int(secondNumber))
# allows the four math methods to work

button_1 = Button(base, text="1", pady=20, padx=40, command=lambda: button_click(1))
button_2 = Button(base, text="2", pady=20, padx=40, command=lambda: button_click(2))
button_3 = Button(base, text="3", pady=20, padx=40, command=lambda: button_click(3))
button_4 = Button(base, text="4", pady=20, padx=40, command=lambda: button_click(4))
button_5 = Button(base, text="5", pady=20, padx=40, command=lambda: button_click(5))
button_6 = Button(base, text="6", pady=20, padx=40, command=lambda: button_click(6))
button_7 = Button(base, text="7", pady=20, padx=40, command=lambda: button_click(7))
button_8 = Button(base, text="8", pady=20, padx=40, command=lambda: button_click(8))
button_9 = Button(base, text="9", pady=20, padx=40, command=lambda: button_click(9))
button_0 = Button(base, text="0", pady=20, padx=40, command=lambda: button_click(0))
button_add = Button(base, text="+", pady=20, padx=39, command=button_add)
button_subtract = Button(base, text="-", pady=20, padx=40.5, command=button_subtract)
button_multiply = Button(base, text="x", pady=20, padx=40, command=button_multiply)
button_divide = Button(base, text="/", pady=20, padx=41, command=button_divide)
button_equal = Button(base, text="=", pady=20, padx=91, command=button_equal)
button_clear = Button(base, text="clear", pady=20, padx=79, command=button_clear)

#this creates the buttons: text is used display on the button pady and padx are for the size the command is for the button_click

button_1.grid(row=1, column=0)
button_2.grid(row=1, column=1)
button_3.grid(row=1, column=2)
#first row of buttons
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
#second  row of buttons
button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)
#third row of buttons
button_0.grid(row=4, column=0)
button_clear.grid(row=4, column=1, columnspan=2)# due to it spanning two lines
#fourth row of buttons
button_add.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=2)# due to it spanning two lines
#fith row of buttons
button_subtract.grid(row=6, column=0)
button_multiply.grid(row=6, column=1)
button_divide.grid(row=6, column=2)
#sixth row of buttons
base.mainloop()
#this runs the calculator
