# USEFUL FUNCTIONS IN PYTHON BY CdubemB

numbers = [1, 3, 5, 7, 9]#list of odd numbers

if all(i > 1 for i in numbers):
    print("all of the numbers are greater than five") # checks for if any numbers are greater than five
else:
    print("not all of the numbers a greater than five")

if any(i > 5 for i in numbers):
    print("at least one is greater than five")#checks if any numbers are greater than five

for e in enumerate(numbers):
    print(e) # prints all the numbers in the list in their order with given iteration