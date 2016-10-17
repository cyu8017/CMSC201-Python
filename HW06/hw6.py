'''
Filename: practice.py
Author: Zhengchao Yu 
Date: 10/23/2014
Section: 4
E-Mail: zy3@umbc.edu
Description:
Integrating smaller parts of a program into a larger whole. 
This program will analyze numbers for the user. 
'''

import math
import sys

# Function: GCD():
# Description:
# This function takes two integers,
# returns largest number that evenly divides both integers 
# Input: num1, num2 
# Output: largest integer 
def GCD(num1, num2):

    gcd = 0
    i = 1
    # This while loop will calculate the the two taken integers.
    # Then it will return the largest integer.
    while i < num1 and i < num2:
        if num1%i == 0 and num2%i ==0:
            gcd = i
        i = i + 1        
    return gcd

# Function: isPerfect():
# Description:
# Takes a single integer and returns
# True: is the number equal to half the sum of all of its positive divisors.
# False: otherwise 
# Input: num1
# Output: True, False 
def isPerfect(num1):

    divisior = []
    number = 0

    # Takes a single integer and returns 
    for i in range(1,num1 + 1):

        if num1 % i ==0:
            number = number + i
    number = number / 2

    if number == num1:
        return True
    return False
    
# Function: goldbach():
# Description:
# Takes a single, positive even integer greater than 2, and
# returns two primes, the sum of which is that num1. 
# Input: num1
# Output: two prime values the sum of num1.
def goldbach(num1):

    # Every even integer greater than 2
    # can be expressed as the sum of two primes.
    numbers = []
    prime = getPrimes(num1)
    for i in prime:
        for j in prime:
            if i + j == num1:
                numbers.append(i)
                numbers.append(j)
                return numbers

# Function: isPrime() 
# Description: divisible by 1 and itself 
# Input: num 
# Output: True, False 
def isPrime(num):
    for i in range(2,num):
        if num % i == 0:
            return False
    return True

# Function: getPrimes()
# Description: calculates prime numbers 
# Input: num1
# Output: get prime numbers 
def getPrimes(num1):
    prime = []
    for i in range(1, num1):
        if isPrime(i):
            prime.append(i)
    return prime
    
# Function: primeFactors():
# Description:
# Takes a single positive integer, and
# Input: num1
# Output: list of prime factors
def primeFactors(num1):

    d = 2
    prime_factors = [] # Create prime_factors empty list.
    prime = getPrimes(num1)
    for i in prime:
        if num1%i == 0:
            prime_factors.append(i)
    # Return a list of all the prime factors of the integer.
    return prime_factors
    
# Function: printMenu():
# Description:
# Prints a menu to the user 
# Input: none 
# Output: none
def printMenu():
    
    # Display Menu
    print("\n") # blank line 
    print("1. Greatest common divisor") # Choice 1 
    print("2. Perfect number check")    # Choice 2 
    print("3. Goldbach decomposition")  # Choice 3 
    print("4. Prime Factors")           # Choice 4
    print("5. Quit")                    # Choice 5 
    print("\n") # blank line line


# Function: getNumber():
# Description:
# Prints message, and then asks user for the number.
# If the number is less than min, the function will loop,
# continuing to ask the user for a number until the user enters a number
# larger than min. The function then returns that number. 
# Input: message, minimum
# Output: number
def getNumber(message, minimum):
    print(message)
    number = -1
    while number < minimum:
        number = int(input("Please enter a positive integer greater then " 
                       + str(minimum) + " "))
    return number

# Function: getNumber1():
# Description:
# Prints error message 
# Input: negative number 
# Output: number is not acceptable
def getNumber1(message):
    number = -1
    while True:
        number = int(input(message))
        if number < 0:
            print("Number is not acceptable.")
        return number

# Function: main()
# Description: Runs and tests all functions of the program 
# Input: Choice 
# Output: Result 
def main():

    # Prints message. 
    choice = -1
    message = "Please enter a positive integer: "    
    while choice != 5:

        # Print menu, and prompt user to enter choice. 
        printMenu()
        choice = int(input("Please enter a choice: "))
        
        
        while(choice > 5 or choice < 0):
            # Print Error Message 
            print("Number not acceptable")
            choice = int(input("Please enter a choice: "))

        # Choice 1:
        # Greatest common divisor 

        # This choice will acquire GCD
        if choice == 1:
            num1 = getNumber1(message)
            num2 = getNumber1(message)
            gcd = GCD(num1, num2)
            print("The greatest common divisor of " + str(num1) + 
                  " and " + str(num2) + " is " + str(gcd))
        
        # Choice 2:
        # Perfect number check 

        # This choice will check to see if number is perfect. 
        elif choice == 2:
            num1 = getNumber1(message)
            if isPerfect(num1):
                print(str(num1) + " is a perfect number")
            else:
                print(str(num1) + " is not a perfect number")
        
        # Choice 3:
        # Goldbach decoposition

        # This choice will retrieve the goldbach numbers 
        elif choice == 3:
            num1 = getNumber(message, 4)
            gold = goldbach(num1)
            print("The goldbach decomposition of " + str(num1) + " is " +
                  str(gold[0]) + " and " + str(gold[1]))
        
        # Choice 4:
        # getNumber

        # This choice will retrieve the prime factors. 
        elif choice == 4:
            num1 = getNumber1(message)
            primes = primeFactors(num1)
            print("The prime factors of " + str(num1) + " are " + str(primes))
        
        # Choice 5:
        # Quits Program

        # This choice will quit program. 
        elif choice == 5:
            print("Quitting...")
        if choice != 5:
            choice = -1

main()
