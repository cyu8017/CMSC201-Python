'''
File: errors.py
Author: Zhengchao Yu
Date: September 15, 2014
Section: 4
Email: zy3@umbc.edu
Assignment Description: Lab 2: A Simple Program

Debugging:
Debugging is the process of eliminating errors from your code.
The Computer will automatically reject python programs that have mistakes in their syntax.
Fix the following program.
'''

# This line will print program greeting.  
print ("This program finds the average of two integers. ")

# Python treats int and strings differently,
# we need a way to tell the porgram the input is actually an int. 
num1 = int(input("Input number one: ")) # Prompt user to enter first number 
num2 = int(input("Input number two: ")) # Prompt user to enter second number 

# Cast the input to a variable. 
average = int(((num1) + (num2)) /2) # This function calculates average. 

# This line will print average solution. 
print ("The average of the two numbers is: " + str(average))

