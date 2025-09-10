#SIMPLE INTRODUCTION TO CLASSES

class pet:
    def __init__(self, name, colour): #__init__ is used to signify an function is a method in a class
        self.name = name
        self.colour = colour


rabbit = pet("rupert", "white") #this assigns rabbit as an object using the parameters in the method within the class
print(rabbit.colour) #will be white

#Below is an example of inheritance

class job:
    def __init__(self, years, enjoyment):
        self.years = years
        self.enjoyment = enjoyment
    def joblove(self):
        return "I love my job"
#above is the superclass which will be inherited from     

class economist(job):
    def supply(self):
        print(super().joblove(), "and I love supply and demand")
#economist is the subclass which is inhertied from the class job
worker1 = economist("10", "high") #the parameters of job is still used despite economist being the class used to derive the object
worker1.supply()

