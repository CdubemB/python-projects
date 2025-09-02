#Utilization of generators in python 
def square_value():
    counter = 0
    while counter < 10:
        val = counter**3
        yield val #this is used to define the generator
        counter += 1

cubeNums = list(square_value()) #this turns all the values that yield produces each time the function loops into a list
print(cubeNums)

for counter in square_value():
    print(counter)

#generators, like lists, can be iterated through a for loop, however, they cannot be indexed traditionally.

def decor(func):
    def wrap(): #this is the embedded function that will be applied to another
        print('I\'m the wrapper')
        func() #this is the function that is inputed into the decorator
        print('I\'m the wrapper')
    return wrap

def present():
    print('I\'m the present')

gift = decor(present) #gift is a new function that involves present that has been decorated with the addition of wrap
gift()

#decorators are used to modify functions 