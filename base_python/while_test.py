guess = int(input("please enter a number between 1 and 6"))
diceRoll = 4

while guess != diceRoll:
    print("incorrect guess again")
    guess = int(input())
print("correct, you guessed right!")