from random import *
numbertoguess = randint(1,100) #pick out a random number 1-100
guessed = False #initialise the guessed variable
while guessed==False:
    guess = input("Take a guess: ")
    try:
        guess = int(guess) #try to make the user input an integer
    except Exception as exception: # If an error occurs
        print("You need to input a number!")
        quit() #exit program, user input invalid
    if guess == numbertoguess: #check if guess is correct
        print("Well done! You guessed correctly.")
        guessed = True
    elif guess > numbertoguess: #check if guess is too high
        print("Too high!")
    elif guess < numbertoguess: #check if guess is too low
        print("Too low!")
