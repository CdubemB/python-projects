# TEXT ANALYSER IN PYTHON BY CdubemB

filename = input("ENTER THE NAME OF A FILE \n")

with open(filename) as f:
   text = f.read() #reads the file that is input

print(text)

def charcount(text, char): # function will show how much of a certain letter is in the text
    count = 0
    for o in text:
        if o == char:
            count += 1
    return count 

print(charcount(text, "o"))
for char in "abcdefghijklmnopqrstuvwxyz":

  percent = 100 * charcount(text, char) / len(text) #divides the amount of a certain letter by the total number of characters to get the percentage
  print("{0} - {1}%".format(char, round(percent, 2))) # writes the letter and the percentage