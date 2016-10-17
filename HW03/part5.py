'''
Name: part5.py
Author: Zhengchao Yu
Date: 10/1/2014
Section: 4
E-Mail: zy3@umbc.edu
Assignment Descriotion
Create a program that takes modulous without using modulous
Take two numbers of the user a and b and complete a % b.
'''

def main():

    # Prompt the user to enter the top number
    # Prompt the user to enter the bottom number 
    a = int(input("Enter top number: "))
    b = int(input("Enter lower number: "))

    # This while loop will perform subtraction, without modulous. 
    while(a >= b):
        a = a - b

    # Print remainder
    print(a)

    
main()
