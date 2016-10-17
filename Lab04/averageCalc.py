'''
Name: averageCalc.py
Author: Zhengchao Yu 
Date: September 29, 2014 
Section: 4
E-Mail: zy3@umbc.edu
Assignment Description: Calculate the average!
Practice using while loops. 
The user enters how many numbers they would like to take the average of. 
The numbers they would like to average, and prints out the average to the user.  
'''


def main():

    count = 1 
    total = 0 
    
    # Prompt the user to enter how many numbers they would.
    # Cast user input to an int. 
    askInput = int(input("How many numbers would you like to take the average of: "))
    
    # For every number the user wants averaged,
    # Prompt the user to enter their number of updates they current sum of numbers entered.
    while count <= askInput:
        ask = int(input("Enter number: "))
        count = count + 1
        total = total + ask
    

    # When all the numbers have been entered, print out the average to the user.
    average = (total / askInput)
    print (average)
            
main()
