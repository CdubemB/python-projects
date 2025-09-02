# USEFUL FUNCTIONS IN PYTHON BY CdubemB
ingredients = ["cheese", "egg", "ham", "siracha"]
print(", ".join(ingredients)) #the join function will print the list with the , as a seperator
ingredients2 = (", ".join(ingredients)).split(", ") #the split function converts a string wiht a certain seperator into a list
print(ingredients2)

print ("Bonjour Shofu".replace("shofu", "le monde"))#this will replace shofu with le monde

sentence = "Susan went to Mexico"
if sentence.startswith("Susan") and sentence.endswith("Mexico"):
    print("Susan truly did go to Mexico")
else:
    print("Susan may have not went to Mexico")
#the startswith and endswith function check if a sentence begins, or ends with a word respectively
 
print(sentence.lower())
print(sentence.upper())
# the .upper() function converts a sentence to capital letters whilst the .lower() does the inverse

numbers = [1, 3, 5, 7, 9]

print(min(numbers))
print(max(numbers))
print(sum(numbers))
#the min function produces the minimum value in a list, the max function produces the max and the sum function gives the sum of the list

print(abs(-44))
#the abs function gives the absolute function of a number (distance from zero)

if all(i > 1 for i in numbers):
    print("all of the numbers are greater than five") # checks for if all numbers are greater than five
else:
    print("not all of the numbers a greater than five")

if any(i > 5 for i in numbers):
    print("at least one is greater than five")#checks if any numbers are greater than five.

for e in enumerate(numbers):
    print(e) # prints all the numbers in the list in their order with given iteration.

print(list(map(lambda x: x+ 5, numbers))) 
print(list(filter(lambda x: x%3 == 0, numbers)))
'''
 the lambda function allows one to make a quick one line function and the map function 
applies this function to multiple elements in a list
The filter functoin applies a filter states by a function to a list and removes those that don't match the filter
'''
