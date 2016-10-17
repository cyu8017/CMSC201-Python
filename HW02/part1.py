'''
File: part1.py
Author: Zhengchao Yu 
Date: September  18, 2014 
Section: 4
E-Mail: zy3@umbc.edu 
Assignment Description: Homework 2
This homework involves a series of exercises designed to practice 
variables, expressions, and if statements. 

Assignment Part 1:
This program will read three numbers from the user.
(you may assume the user will actually enter numbers).
Print out the average of these three numbers.
'''

import math

def main():

    print ("\n ")
    # The following line will print this program's greeting.
    print("This program will find the average of three numbers.")
    print("----------------------------------------------------")
    # The following three lines will cast the user's input into strings. 
    number1 = input("Enter your first number: ")
    number1 = float(number1)
    number2 = input("Enter your second number: ")
    number2 = float(number2)
    number3 = input("Enter your third number: ")
    number3 = float(number3)

    # This function calculates the average of the three numbers. 
    numAverage = int(( (number1) + (number2) + (number3) ) / 3) 
    print("----------------------------------------------------")
    
    # This line will print out the averaged number. 
    print ("Your average is: " + str(numAverage))

main()
