import random

randomNumber = random.randint(1,9)

print("Guess a number betweem 1 and 9")
usedChances = 0
while usedChances < 5:
    guess = int(input("Enter a number: "))
    if guess == randomNumber:
        print("You guessed the number!")
        break
    else:
        usedChances += 1
        if guess > randomNumber:
            print("Go Lower")
        else:
            print("Go Higher")
if usedChances == 5:
    print("You lost! , Try again")

