'''
Filename: findTheMax.py
Author: Zhengnchao Yu 
Date: 10/6/2014
Section: 4
E-Mail: zy3@umbc.edu
Assignment Description: Find the Max!
Practice using lists and for loops.
Prompt the user for integer elements and then find the maximum of the elements entered by the user.
This program will not use any list methods other than .append())

Steps:

* Initialize an empty list to store uers values.
* Obtain values from the user
* Traverse through the list to find the max. 
'''
import sys

def main():

    emptyList = []
      
    Quit = 'q'
    print ("Enter a list values and I will find the maximum!")   
    number = "0"
    maximum = -1000000
    while number != "q":
        number = input("Enter a number or 'q' to find the max of the list: ")
        emptyList.append(number)
    for i in emptyList:
        if i != "q":
            number = int(i)
            if(maximum < number):
    
                maximum = number
            # If the user enters 'q', thie program will end
                
    print("The maximum is:", maximum) 
                    
main()
