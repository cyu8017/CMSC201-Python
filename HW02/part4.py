'''
Name: Part4.py
Author: Zhengchao Yu 
Date: September 18, 2014 
Section: 4
E-Mail: zy3@umbc.edu
Assignment Description: Homework
This homework involves a series of exercises designed to practice 
variables, expressions, and if statements. 

Part 4: 
This program will ask the user for the state of two switches, 
and the user will answer with y or n. 
If the user answers y for both switches or n for both switches, 
the program will print ("The generator is on") 
'''

def main():
    
    print("\n")
    print("Generator Status")
    print("----------------------------------------")
    # Prompt the user to input the status of switch 1 and 2.
    # User will enter y for yes, and n for no. 
    switch1 = input("Is switch 1 on? (y/n): ")
    switch1 = str(switch1)
    switch2 = input("Is switch 2 on? (y/n): ")
    switch2 = str(switch2)

    # This if else statments determines the status of the generator. 
    
    # If user enters y for both switches, print 'off'
    if switch1 == 'y' and switch2 == 'y':
        Generator = 'Off'
    # If user enters y and n, print 'on' 
    elif switch1 == 'y' and switch2 == 'n':
        Generator = 'On' 
    # If user enters n both switches, print 'off' 
    elif switch1 == 'n' and switch2 == 'n':
        Generator = 'Off'
    # If user enters n and y, print 'On
    elif switch1 == 'n' and switch2 == 'y':
        Generator = 'On'
    
    # The following line will print the Generator's status. 
    print ("The generator's status is: " + str(Generator))

main()
