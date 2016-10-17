'''
Name: part2.py
Author: Zhengchao Yu 
Date: 10/1/2014
Section: 4
E-Mail: zy3@umbc.edu
Assignment Description: 
Program takes an input from the user and prints prime or not prime.
'''
import math 

def main():

    # Prompt the user to enter a prime number 
    primeNumber = int(input("Enter a prime number: "))
    prime = True
    # Set i = primeNumber
    i = primeNumber

    # This while loop will determine if the number is prime.
    # Decrement i >= 3
    while i >= 3:

        i = i - 1
        # Check to see if remainder == 0 
        if (primeNumber % i) == 0:
            prime = False

    # If primeNumber == True, print (is prime)        
    if prime == True: 
        print(primeNumber,"is prime")

    # If primeNumber == False, print (is not prime)
    else:
        print(primeNumber, "is not prime")

main()
