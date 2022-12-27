import os
from time import sleep

# def keyword

# function declaration
def getInput():
    userInput = input("Enter: ")
    displayInput(userInput)

def displayInput(value):
    print("Output:",value)

# function invocation
getInput()

# sleep
sleep(1)

#clear screen
os.system('cls')

# built-in function
# max(string) returns the max character
# min(string) returns the min character