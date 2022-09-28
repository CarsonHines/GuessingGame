import random
from typing import Counter

def funct():
    print(">>>NEW GAME<<<")
    counter = 0
    ranNum = random.randint(1, 100)

    while True:
        userGuess = int(input("Enter Guess: "))
        
        while userGuess != ranNum:
            counter += 1

            if userGuess > ranNum:
                print("Too high, try again.")
                break

            elif userGuess < ranNum:
                print("Too low, try again.")
                break

        if userGuess == ranNum:
            print("Congrats! It took you", counter, "attempts.\n")
            funct()


funct()