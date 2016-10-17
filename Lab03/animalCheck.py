'''
Filename: animalCheck.py
Author: Zhengchao Yu 
Date: 9/29/14
Section: 4
E-Mail: zy3@umbc.edu
Description:
Lab 3 Simple Logic Programming
Pets
Practice comparing strings. 
'''

def main():

    # Get an input from the user. 
    animalInput = str(input("Enter Animal Name: "))

    # If the input is dog or cat, print this is a pet 
    if animalInput == 'dog' or animalInput == 'cat':
        print("This is a pet.")
        
    elif animalInput == 'snake':
        print("HELL NO, This is not a pet.")

    # If input is not dog or cat, print this is not a pet. 
    else:
        print("This is not a pet.")

main()
