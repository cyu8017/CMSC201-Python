'''
Name: part3.py
Author: Zhengchao Yu 
Date: September 24, 2014 
Section: 4
E-Mail: zy3@umbc.edu
Assignment Description: Homework 2

Medical Diagnosis Software. 
This program will ask the user if they have the following:
(A Feaver, A Rash, A Stuffy Nose, of if Your Ear Hurts) and print:
* Don't have a feaver and don't have a stuffy nose: Hypochondriac
* Don't have a feaver and have a stuffy nose: Head Cold
* Have a feaver, don't have a rash, and ear hurt's: Ear Infection
* Have a feaver, don't have a rash, and ear doesn't hurt: Flu
* Have a feaver and a rash: Measles
'''

import math

def main():

    print("\n")
    # This line will display program greeting. 
    print("Medical Diagnosis")
    print("---------------------------------------")

    # This line will prompt the user to enter y or n for the following questions.
    # User will enter y for Yes and n for No. 
    feaver = input("Do you have a feaver? (y/n): ")

    # If patient does not have a feaver and does not have a stuffy nose:
    # The patient is diagnosed with Hypochondriac. 
    if feaver == 'n':
        stuffyNose = input("Do you have a stuffy nose? (y/n): ")
        if stuffyNose == 'n':
            print("Diagnosis: You have Hypochondriac.")
            print("\n") # Print blank line 
            
        # If patient does not have a feaver and has a stuffy nose:
        # The patient is diagnosed with a head cold. 
        if stuffyNose == 'y':
            print("Diagnosis: You have a Head Cold.")
            print("\n") # Print blank line 

    # If patient has a feaver and has a rash:
    # The patient is diagnosed with measles. 
    elif feaver == 'y':
        rash = input("Do you have a rash? (y/n): ")

        if rash == 'y':
            print("Diagnosis: You have measles.")
            print("\n") # Print blank line

        # If patient has a feaver, and has an ear infection:
        # The patient is diagnosed with the Flu.
        if rash == 'n':
            earHurt = input("Do you have an ear infection? (y/n): ")                    

            if earHurt == 'n':
               print("Diagnosis: You have the Flu.")
               print("\n") # Print blank line 

            # If patient has a feaver, does not have a rash, and ear hurts:
            # The patient is diagnosed with an ear infection.
            if earHurt == 'y':
                print("Diagnosis: You have an Ear Infection.")
                print("\n") # Print blank line 
                

main()
