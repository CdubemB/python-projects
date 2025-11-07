#SIMPLE INTRODUCTION TO METACHARACTERS
import re 

if re.match(r"gr.y", "grey"):
    print("match 1")
else:
    print("no match")
if re.match(r"gr.y", "gray"):
    print("match 2")
else:
    print("no match")
if re.match(r"gr.y", "gley"):
    print("match 3")
else:
    print("no match")
#the "." metacharacter is used to match any character other than a newline

pattern = r"^.and"

if re.search(pattern, "bandlab"):
    print("match 4")
else:
    print("no match")
if re.search(pattern, "backhand"):
    print("match 5")
else:
    print("no match")

pattern2 = r"(.and)$"

if re.search(pattern2, "bandlab"):
    print("match 6")
else:
    print("no match")
if re.search(pattern2, "backhand"):
    print("match 7")
else:
    print("no match")

# the "^" metacharacter checks at the beginning of a string whereas the "$" metacharacter checks at the end of a string 
# (re.search is used becuase it searches wherever in the string)

if re.match(r"egg(spam)*", "egg"):
    print("Match 8")
if re.match(r"egg(spam)*", "eggspamspamegg"):
    print("Match 9")
if re.match(r"egg(spam)*", "spam"):
    print("Match 10")
else:
    print("no matches here")
#in order for there to be a match the string would have to start with egg followed by zero or more matches due to the metacharacter "*"
if re.match(r"egg(spam)+", "egg"):
    print("Match 11")
if re.match(r"egg(spam)+", "eggspamspamegg"):
    print("Match 12")
if re.match(r"egg(spam)+", "spam"):
    print("Match 13")
else:
    print("no matches here")
#"+"" is similar to "*" however it requires 1 or more matches
if re.fullmatch(r"egg(spam)?", "egg"):
    print("Match 14")
if re.fullmatch(r"egg(spam)?", "eggspam"):
    print("match 15")
if re.fullmatch(r"egg(spam)?", "eggspamspamegg"):
    print("Match 16")
else:
    print("definitely no matches")
if re.fullmatch(r"egg(spam)?", "spam"):
    print("Match 17")
else:
    print("no matches here")
#"?" checks if there are zero or one repitions, (fullmatch is used as match only checks for one occurance instead of a full coincision)

pattern3 = r"9{1,3}$"

if re.match(pattern3, "9"):
    print("Match 18")

if re.match(pattern3, "999"):
    print("Match 19")

if re.match(pattern3, "9999"):
    print("Match 20")
#the {x, y} checks if the expression has between x and y repitions