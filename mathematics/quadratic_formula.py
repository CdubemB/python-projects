#by CdubemB
from math import sqrt
#the quadratic formula (aim to have to three variables - an a, b, and c term such as in the quadratic formula - find the roots of them if values are real)

def quadFormula(a, b, c):
	input1 = int(b)
	try:
		input2 = sqrt(int(b)**2 - 4*int(a)*int(c)) 
		input3 = (2*int(a))**-1
		answer1 = (input1 + input2) * input3
		answer2 = (input1 - input2) * input3 #the previous lines of code in the try statement performs the quadtratic formula on three variables
		print(str(answer1) + "\n" + str(answer2)) #this will display the two roots given the variables inputed
	except ValueError:
		print("the answer was imaginary") #if the inputs yield an imaginary answer this will be displayed
	finally:
		print("thanks for using the calculator") #this will display regardless of inputs

selector = input("which function would you like to utilise \n\n options: quadraticformula (q), ..., ...")
if selector.lower() == "quadraticformula" or selector.lower() == "q": #this is used to ask for the following values depending on which formula the user would like to use (so far this is only the quadratic formula)
	num1 = input("what is your a value (x-squared coefficient)")
	num2 = input("what is your b value (X coefficient) ")
	num3 = input("what is your c value (constant)")
quadFormula(str(num1), str(num2), str(num3)) #this runs the function using the numbers inputed
