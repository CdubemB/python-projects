# SIMPLE INTRODUCTION TO RANDOM EXPRESSIONS, WITH SOME CHARACTER CLASSES
import re #random expressions module, part of the standard library

pattern = r'ipsum' #r before the string (raw strings) have no escape characters making RE use easier

if re.match(pattern, "ipsumipsumipsum"):
    print("match found")
else: 
    print("no matches")

if re.match(pattern, "Loremipsumdolorsitamet"):
    print("match found")
else:
    print("no matches")
#checks if the pattern "ipsum" matches the string, from the start, and prints "match" if so

if re.search(pattern, "Lorem ipsum dolor sit amet"):
    print("search found")
else:
    print("not present")
#searches the string for an instance of ipsum

print(re.findall(pattern, "ipsum ipsum dolor sit amet, ipsum consectetur"))
#returns a list of all substrings that match the pattern

search = re.search(r'ipsum', "Lorem ipsum dolor sit amet Lorem ipsum dolor sit amet Lorem ipsum dolor sit amet")

if search:
    print(search.group()) #returns the string matched
    print(search.start()) #returns the starting index of the first matched instance of the string
    print(search.end()) #returns the ending index of the first matched instance of the string
    print(search.span()) #returns a tuple of the (start, end) index of the matched string

str = "My name is John Genji, Hello John Genji"
print(str)
pattern = r"Genji"
newstr = re.sub(pattern, "Hanzo", str)
print(newstr)
#substitutes all instances of "Genji" with "Hanzo" in the newley assigned string

str2 = "My name is John Genji, My friend Hello John Genji"
print(str2)
pattern2 = r"^My"# matches only if "My" is at index 0
newstr_start = re.sub(pattern2, "your", str2)
print(newstr_start)

pattern3 = r"[A-Z][a-z][a-z][0-9][0-9]" #this is a character class
if re.search(pattern3, "Bob23"):
    print("suitable password")
else:
    print("non suitable")

if re.search(r"[^A-Z]", "this is all quiet"):
    print("quiet match")
elif re.search(r"[^A-Z]", "THIS IS ALL LOUD"):
    print("LOUD MATCH")
else:
    print("letters please do you know them")
#^ at the beginning of the character class inverts it