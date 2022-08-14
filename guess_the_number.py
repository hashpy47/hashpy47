# this is a guess the number game
import random

print("Hello, Whats your name? ")
your_name = input()

print("Hello there, " + str(your_name) + ", Im thinking of a number between 1 and 20.")
secret_number = random.randint(1,20)

for guesses in range(1, 7):
    print("Take a Guess.")
    guess = int(input())

    if guess < secret_number:
        print("Your guess is too low")
    elif guess > secret_number:
         print("Your guess is too high")
    else:
        break   # this would imply the correct number has been guessed
                #print("Well Done, " +your_name+ ", You Guessed my number in " +guesses+ " gueses!")

if guess == secret_number:
    print("Well Done, " +your_name+ ", You Guessed my number in " +str(guesses)+ " guesses!")
else:
    print("Nope, You have taken " + str(guesses) + " Guesses.With no luck.")
