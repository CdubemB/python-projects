#WRITTEN BY CdubemB

"""
create a programme that can:

gather a sample text with variables
gather variable defintions from the user
decode the text

a tkinter user interface is adviced
"""
from tkinter import *

def renewel():
    count1 = 0
    while count1 < 9:
        list ["1","2","3","4","5","6","7","8","9"]
        return list[count1]
        count1 += 1


base =  Tk()

def main():#will run all the following functions
    text_gather()
    translate()
    print(result(text))
    base.mainloop()

def text_gather():#will get the text input with the variables from the user
    uLabel = Label(base, text="enter your paragraph with the variables")
    global tBar
    tBar = Entry(base, width=35, fg="black", borderwidth=5) #creates a text bar for the box
    tBar.grid(row = 2, column = 0, columnspan = 3, padx = 10, pady = 50) #puts the text bar in a specific place
    uLabel.grid(row = 1, column = 1, columnspan = 3, padx = 10, pady = 50)
    
def translate():#will translate the given variables that the user inserts
    global text
    text = list(tBar.get())
    askCount = 0
    while askCount < 10:
        print("what does", str(askCount), "equal")
        answer = str(input())
        userVariables = open("variables.txt", "a+")
        userVariables.write(answer + "\n")
        askCount += 1
    variables = []
    for myline in userVariables:
        variables.append(myline)
    text.replace("0", variables[0])
    text.replace("1", variables[1])
    text.replace("2", variables[2])
    text.replace("3", variables[3])
    text.replace("4", variables[4])
    text.replace("5", variables[5])
    text.replace("6", variables[6])
    text.replace("7", variables[7])
    text.replace("8", variables[8])
    text.replace("9", variables[9])

def result(s):#will output the translated text
    str = ''

    for e in text:
        str += e

    return str



main()