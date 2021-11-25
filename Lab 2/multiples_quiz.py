#Task 1 - Lab 2 - Dawid Ziaja
#Multiples Quiz
from random import *
num1 = randint(1,12) # choose two numbers between 1 and 12 for the user to multiply
num2 = randint(1,12)
response = input("What is " + str(num1) + "x" + str(num2) +"?\n") #ask the user for a response
try:
    response = int(response) #try to make the user input an integer
except Exception as exception: # If an error occurs
    print("You need to input a number!")
    quit() #exit program, user input invalid
if int(response)==(num1*num2):
    print("You are correct!")
else:
    print("You are incorrect!")