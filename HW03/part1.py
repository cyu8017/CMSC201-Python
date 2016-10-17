'''
Name: part1.py
Author: Zhengchao Yu 
Date: September 26, 2014
Section: 4
E-Mail: zy3@umbc.edu
Assignment Description: 
This homework practices using variables, expressions, and if statements. 

Part1: 
Write a program that prints the numbers 1 to 100. (One per line) 
However, when a program is divisible by 3, print ('foo').
If it is divisible by 5, print ('bar'). 
If it is divisible by both, you should print ("baz").
'''

import math

def main():
        
    numberList = 0
    
    # Print numberList from 0 to 100  
    while numberList < 100: 
        numberList = numberList + 1        
       # print (numberList)
        
        # If the number is divisible by 3 or 5, print baz
        if (numberList % 3 == 0) and (numberList % 5 == 0): 
            print("baz")
 
        # If the number is divisible by 5, print bar 
        elif (numberList % 5 == 0):
            print("bar")
        
        # If the number is divisible by 3, print foo
        elif (numberList % 3 == 0):
            print("foo")
        
        # After changes are made, print out numberList
        else: 
            print(numberList)

main()
