"""
	Creating a simple calculator
"""
function = str(input("what function do you need to use (addition, subtraction, multiplication or division) \n"))
#acuries the function from the user
y = int(input("what is the first number you wish to use \n"))
x = int(input("what is the second number you wish to use \n"))
#the numbers that will be added
def uCalc(num1, num2):
	if function == "/" or function == "division":
		print(num1 / num2)
	elif function == "*" or function == "multiplication":
		print(num1 * num2)
	if function == "+" or function == "addition":
		print(num1 + num2)
	if function == "-" or function == "subtraction":
		print(num1 - num2)

#Function carries out the equation.
uCalc(x, y)