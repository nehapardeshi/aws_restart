import random
number = 10
isGuessRight = False

while isGuessRight != True:
    guess = input(" Guess a number between 1 and 10: ")
    if int(guess) == number:
        print("You guessed {}. That is correct! You win!".format(guess))
        isGuessRight = True
    else:
        print("You guessed {}. Sorry, That isn't it. Try again.".format(guess))