'''
Name: part6.py
Author: Zhengchao Yu
Date: 10/1/2014
Section: 4
E-Mail: zy3@umbc.edu
Assignment Description: 
Create a program that does input validation.
Prompt the user for a positive number.
If they enter one simply print it back out.
If they enter a negative number or zero, ask for a positive number until one is entered. 
'''

def main():

    number  = 0
    
    while number < 1:

        # Prompt the user to enter a positive number. 
        number = int(input("Please enter a positive number: "))

        # This condition checks if the number entered is a positive number. 
        if number > 0:
            print("\n")

            # The following line will print the positive number back out. 
            print ("Your number was: ", number)

main()
