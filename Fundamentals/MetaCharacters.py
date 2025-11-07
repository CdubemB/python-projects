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
