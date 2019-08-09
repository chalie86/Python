import random
import time

print(
"""
=========================================
* * * * * Guess the Number Game * * * * *
=========================================
Please enter an integer between 1-50!
""")

number = random.randint(1,50)
numberofGuesses = 0

name = input("What is your name?")

print("Hi",name,"I'm thinking of a whole number between 1 to 50! Can you guess what it is?")

while (numberofGuesses < 8):
    try:
        guess = int(input("Take a guess:"))

        numberofGuesses += 1
        guessesLeft = 8 - numberofGuesses
        print("Checking...")
        time.sleep(1)

        if (guess < number):
            print("Your guess is too low! You have " + str(guessesLeft) + " guesses left!")
        if (guess > number):
            print("Your guess is too high! You have "+ str(guessesLeft) + " guesses left!")
        if (guess == number):
            break
    except ValueError:
        print("Please enter a valid number!")
    else:
        if (guess < 1) or (guess > 50):
            print("Please enter a number between 1-50!")

if (guess == number):
    print("Congratulations! You guessed the number in" + str(numberofGuesses) + " tries :)")

else:
    print("Sorry! The number I was thinking was " +str(number) + " :)")
