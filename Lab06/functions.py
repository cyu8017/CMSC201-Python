'''
Filename: functions.py
Author: Zhengchao Yu
Date: 10/13/2014
Section: 4
E-Mail: zy3@umbc.edu
Description:
Have the user enter a number.
Program will print out all prime numbers less than that number. 
'''
# Function: main():
# Description: asks the user for number, calls getPrimes, print numbers
# Input: number
# Output: prime1
def main():

    # Prompt the user to enter a number.  
    number = int(input("Enter a number: "))
   
    # Call the getPrimes() on that number. 
    prime1 = getPrimes(number)

    # Prints result. 
    print(prime1)

# Function: getPrimes(myNum)
# Description: gets a list of primes less than myNum 
# Input: myNum
# Output: Prime numbers 
def getPrimes(myNum):

    tempList = [] # This is a tempoary list 
    number = 0 # define number equals 0 

    # For every number from 1 to myNum, 
    # check to see if its a prime using the isPrime function.
    for i in range(2, myNum + 1):
        myPrime = isPrime(i)

        # If the number is prime, add it to the tempoary list.
        if myPrime == True:
            tempList.append(i)
    
    # Returns tempoary list
    return tempList
 
# Function: isPrime():
# Description: returns whether a number is prime or not. 
# Input: myNum
# Output: True, False 
def isPrime(myNum):

    # For every number between 2 and myNum, 
    # see if myNum is divisible by that number.   
    for j in range(2, myNum + 1):
        
        # If it is divisble by one of these numbers, return false. 
        if myNum % j == 0 and myNum != j:
            return False
    
    # if you exit the loop, return true. 
    return True

main()
