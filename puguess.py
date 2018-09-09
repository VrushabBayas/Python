import random

print("Enter name:")
name=input()

print("welcome  "+name+"guess the number")
secrateNumber=random.randint(1,20)

for chances in range(0,7):
    print("guess the number")
    guess=int(input())
    if guess < secrateNumber:
        print("To small") 
    elif int(guess) > secrateNumber:
        print("Too big..!")
    else:
        break
    
if(guess == secrateNumber):
    print("Well done"+name+"Your guess is correct "+str(guess)+"  you guessed in "+str(chances))
else:
    print("Try again.. you have finished "+str(chances)+" guess") 
