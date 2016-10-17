'''
   Filename: lab10.py  
     Author: Zhengchao Yu 
       Date: 11/10/2014
    Section: 4
     E-Mail: zy3@umbc.edu
Description: Program Design 
Design and implement a simple program to control a bank account. 
This program will have the following options: 
1) Deposit 
2) Withdraw 
3) View Balance 
4) Quit

Rule 1: 
The account must have at least $5.00 in it. 
If the balance ever dips below $5, bank will close account. 

Rule 2: 
If the account ever has above $500.00 you need to calculate interest. 
Your bank gets 1% interest. Calculate interest and add it to balance. 

Rule 3: 
If the balance in the account is ever exactly $1337.00. 
You get robbed of all your money and the program exits. 

Rule 4: 
This program must have 6 functions besided main. 
'''
import math 

def menu():
    print("1) Deposit ")
    print("2) Withdraw ")
    print("3) View balance ")
    print("4) Quit ")
    print("\n")

def deposit(balance): 
    string = "How much would you like to deposit: "
    transaction = inputs(string)
    balance = (transaction + balance)
    interest(balance)
    print("Your new balance is " + str(balance))
    return balance

def interest(balance):
    if(balance > 500):
        print("Since you had more than $500.00 you get interest!")
        balance = (balance + (balance * 0.01))
    return balance

def inputs(string):
    valid = False
    transaction = 0
    while not valid:
        try:
            transaction = float(input(string))
            if(transaction > 0):
                return transaction
        except:
            print("Enter a valid number: ")
    return transaction
        
def withdraw(balance):
    string = "How much would you like to withdraw: "
    transaction = inputs(string)
    balance = (balance - transaction)
    interest(balance)
    print("Your new balance is " + str(balance))
    return balance

def viewAccountBalance(balance):
    print("Your account balance is: " + str(balance))

def userChoice():
    while True:
        try:            
            choice = int(input("Enter menu option: "))
            return choice
        except:
            print("Choice needs to be a valid number")

def main():

    flag = True 
    choice = 0 
    balance = 100.00

    while flag:
        menu()
        choice =  userChoice()        
        if (choice == 1):
            balance =  deposit(balance)
            if balance <= 0: 
                flag = False 
        elif (choice == 2):
            balance = withdraw(balance)
            if balance <= 0:
                flag = False 
        elif (choice == 3):
            viewAccountBalance(balance)
        elif (choice == 4):
            flag = False
        if(balance == 1337.00):
            balance = 0.00
            flag = False
            print("You have been robbed of all your money!")
        elif(balance < 5):
            print("You're Broke!! We're kicking you out of the bank.")
           
main()
