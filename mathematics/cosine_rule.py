"""
cosie rule calculator
by CdubemB

"""
from math import *


def cosForSides(a, b, C):#gets the value of two sides and an angle
	cSquar = a**2 + b**2 - (2*a*b*cos(pi / 180 * C)) #works out c side squared
	lilc = sqrt(cSquar) #square roots it
	return lilc#prints the answer


def cosForAngles(a, b, c):
	p1 = a**2 + b**2 - c**2 #will get the numerator of the equation
	p2 = 2*a*b #will get the denominator of the equation
	cosC = p1/p2#gets the value of the cos of c
	C = acos(cosC) * 180/pi # gets the value of the angle
	return C#prints it

calcDone = False

while calcDone == False:
    a1 = str(input("would you like to find out the size of an angle or side (type exit to exit programme)\n"))
    if a1.lower() == "angle" or a1 == "1": #wil work out the size of an angle
        sA = int(input("side a:"))
        sB = int(input("\nside b:"))
        sC = int(input("\nside c:"))
        print(cosForAngles(sA, sB, sC))
        calcDone = True
    elif a1.lower() == "side" or a1 == "2": #will work out the size of a side
        sA = int(input("side a:"))
        sB = int(input("\nside b:"))
        aC = int(input("\nangle C:"))
        print(cosForSides(sA, sB, aC))
        calcDone = True
    elif a1.lower() == "exit":#will exit the programme
        calcDone == True
        exit()
    else:#will loop if invalid answer chosen
        print("choose a valid input")