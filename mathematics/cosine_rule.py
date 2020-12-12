"""
cosine rule calculator 
by DcubemB

"""
from math import *
def cosForSides(a, b, C):
    cSquar = a**2 + b**2 - (2*a*b*cos(pi / 180 * C)) # works out c side squared
    lilc = sqrt(cSquar)
    return lilc

def cosForAngles(a, b, c):
    p1 = a**2 + b**2 - c**2
    p2 = 2*a*b
    cosC = p1/p2
    C = acos(cosC) * 180/pi
    return C
print(cosForSides(9, 7, 22))
print(cosForAngles(20, 17, 12))