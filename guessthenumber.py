# The Game Guess the number

import random

print("Enter your name")
name = input()
print("Well,"+name+" I have 1 to 20 numbers")
screateNumber = random.randint(1, 20)


for guessToken in range(1, 7):
    print("guess number")
    guess = int(input())
    if guess < screateNumber:
        print("Guess is too low..!")
    elif guess > screateNumber:
        print("Guess is too Heigh..!")
    else:
        break  # If number found..

if(guess == screateNumber):
    print("Well done,"+name+" You took " + str(guessToken)+" guesses...!")
else:
    print("I was guessing "+str(screateNumber))
