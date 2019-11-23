# UTILIZATION OF FUNCTIONS IN PYTHON

def first_func(): #the keyword def is used to create a function followed by a name and a pair of parenthisis with a colon
   pass #allows the function to be used later

first_func() #runs the function [you can also write print(first_func())]

def second_func():
   print("Hello i'm Function 2")

second_func() #this will run the print statement in the function

def third_func():
   return "hello i'm function 3"

print(third_func().upper()) #you must print the function in this way to use return (you can also apply functions to functions)

def fourth_func(greeting): #THIS CONTAINS A PARAMETER THAT MUST BE RUN
   return greeting

print(fourth_func("hello young one"))#parameter must be filled in to run the function

def checker(age, height):
   if age < 12:
      print("you are to young to go on the ride")
   else:
      if height < 150:
         print("you are to short to go on the ride")
      else:
         print("you are permited to go on the ride")

print(checker(18, 149)) #this will use the parametres given to decide what the function does