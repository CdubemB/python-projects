#creating a calculator on python
from tkinter import * #imports the tkinter module

base = Tk()

tBar = Entry(base, width=35, fg="black", borderwidth=5) #creates a search bar
tBar.grid(row = 0, column = 0, columnspan = 3, padx = 10, pady = 10)
def button_click(number):
    tBar.delete(0, END)
    tBar.insert(0, number)

#this will define the buttons

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
button_add = Button(base, text="+", pady=20, padx=39, command=lambda: button_click())
button_equal = Button(base, text="=", pady=20, padx=91, command=lambda: button_click())
button_clear = Button(base, text="clear", pady=20, padx=79, command=lambda: button_click())

button_1.grid(row=1, column=0)
button_2.grid(row=1, column=1)
button_3.grid(row=1, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)

button_0.grid(row=4, column=0)
button_add.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=2)# due to it spanning two lines
button_clear.grid(row=4, column=1, columnspan=2)# due to it spanning two lines
base.mainloop()
