#DECODER - DESIGNED BY CdubemB
from tkinter import *

def popup():
    global popup_window
    popup_window = Tk(className="popup message")
    label1= Label(popup_window, text="what does the variable ... mean")
    label1.pack()
    entry1 = Entry(popup_window, fg="#000", width=10)
    entry1.pack()
def main():
    root = Tk(className="decoder")
    root.minsize(width=1366, height="768")
    root.configure(bg="#555")
    # gives the app a name, size and background colour
    tBox1 = Text(root, width=40, borderwidth=10, bg="#fff", height=30)
    tBox2 = Text(root, width=40, borderwidth=10, bg="#fff", height=30)
    tBox1.grid(column=0, row=0)
    tBox2.grid(column=1, row=0)
    # creates the text boxes
    uButton = Button(root, text="if you have logged in click this", command=popup)
    uButton.grid(column=2, row=0)
    root.mainloop()
main()