'''
Name: randnum.py
Author: Zhengchao Yu 
Date: 9/29/14
Section: 4
E-Mail: zy3@umbc.edu
Assignment Description:
Practice using while loops, we are going to make a program where the user
'''

import random

def main():

    # randnum list (1-10)
    randnum = random.randint(1,10)

    # Print Program Greeting 
    print("Guess a number between 1 and 10 (inclusive) and I'll tell you if you're right!")

    # Initialize a variable called choice.
    # This variable represents users choice. 
    choice = True

    # Initialize a variable called guess.
    # The variable should be initialized to 0 so that it is not in the range of correct answers. 
    usersGuess = 0
    
    # This loop executes based on the two initialized variables (choice, guess).
    while (usersGuess != randnum and choice == True):
        
        # Prompt the user for a guess and cast input to an int.  
        usersGuess = int(input("Enter your guess: "))

        # If the guess is true, print ("You Win")
        if usersGuess == randnum:
            print("You win!!!")
            choice = False

        # If the guess is incorrect, inform the user and ask if they would like to guess again. 
        # If the user would like to guess again, the condision will cause the loop to repeat. 
        else:
            usersGuess = input("NOPE. Would you like to try again? ")

            # If the user does not want to loop again,
            # Enter n to end program. 
            if(usersGuess == 'n'):
                choice = False
        
main()
